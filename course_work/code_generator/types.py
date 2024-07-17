import llvmlite.ir as ir

from code_generator.util import parse_escape
from code_generator.errors import SemanticError


class TinyCTypes(object):
    # определение типов данных
    int = ir.IntType(32)
    short = ir.IntType(16)
    char = ir.IntType(8)
    bool = ir.IntType(1)
    float = ir.DoubleType()
    double = ir.DoubleType()
    void = ir. VoidType()

    # словарь типов данных
    str2type = {
        "int": int,
        "short": short,
        "char": char,
        "long": int,
        "bool": bool,
        "float": float,
        "double": double,
        "void": void
    }

    # словарь экранированных символов с их ASCII кодами
    ascii_mapping = {
        '\\a': 7,
        '\\b': 8,
        '\\f': 12,
        '\\n': 10,
        '\\r': 13,
        '\\t': 9,
        '\\v': 11,
        '\\\\': 92,
        '\\?': 63,
        "\\'": 39,
        '\\"': 34,
        '\\0': 0,
    }

    # преобразование строкового представления константы const_value в соответствующее представление LLVM для ctype
    # cls -- класс определения (родительский класс)
    @classmethod
    def get_const_from_str(cls, ctype, const_value, ctx):
        # если const_value это строка
        if type(const_value) is str:
            # если тип ctype - символ
            if ctype == cls.char:
                if len(const_value) == 3:
                    # возвращаем экземпляр cls.char, полученный из Unicode-кодовой точки символа
                    return cls.char(ord(str(const_value[1:-1])))
                elif len(const_value) == 1:
                    # конвертируем строковую переменную в число
                    # возвращаем константу в виде символьного значения
                    return cls.char(int(const_value))
                else:
                    # присваиваем value значение переменной
                    value = const_value[1:-1]
                    if value in cls.ascii_mapping:
                        # если значение переменной value находится в словаре ascii_mapping
                        # возвращаем символьное значение из словаря
                        return cls.char(cls.ascii_mapping[value])
                    else:
                        raise SemanticError(ctx=ctx, msg=f"Unknown char value: {value}")

            # если тип ctype - с плавающей точкой
            elif ctype in [cls.float, cls.double]:
                return ctype(float(const_value))

            # если тип ctype - целочисленный
            elif ctype in [cls.short, cls.int]:
                return ctype(int(const_value))

            # если тип ctype - массив и его эл-ты - символы
            elif isinstance(ctype, ir.ArrayType) and ctype.element == cls.char:
                # извлекаем значение из const_value
                # начиная со 2-ого символа и заканчивая предпоследним, чтобы убрать кавычки по краям строки
                # с помощью parse_escape обрабатываем экранированные символы в строке
                # добавляем символ '\0' в конец строки
                str_val = parse_escape(const_value[1:-1]) + '\0'

                # создаём новую константу типа ctype с помощью ir.Constant,
                # передаём в нее массив байтов, представляющих строку str_val с кодировкой 'ascii'
                return ir.Constant(ctype, bytearray(str_val, 'ascii'))

            else:
                raise SemanticError(msg=f"No known conversion: {const_value} to {ctype}")
        else:
            raise SyntaxError(msg=f"get_const_from_str doesn't support const_value which is a {str(type(const_value))}", ctx=ctx)

    # проверка на целочисленный тип данных
    @classmethod
    def is_int(cls, type):
        return type in [cls.int, cls.short, cls.char]

    # проверка на тип данных с плавающей точкой
    @classmethod
    def is_float(cls, type):
        return type in [cls.float, cls.double]

    # приведение значения определённого типа к другому типу
    @classmethod
    def cast_type(cls, builder, target_type, value, ctx):
        # если тип value совпадает с целевым target_type
        if value.type == target_type:
            return value

        # если тип value - целочисленный или булевый
        if cls.is_int(value.type) or value.type == cls.bool:
            # если целевой тип - целочисленный
            if cls.is_int(target_type):
                # проверка ширины значения value относительно целевого типа target_type
                if value.type.width < target_type.width:
                    # расширение value до целевого типа
                    return builder.sext(value, target_type)
                else:
                    # свёртка value до целевого типа
                    return builder.trunc(value, target_type)

            # если целевой тип - с плавающей точкой
            elif cls.is_float(target_type):
                # преобразование value в тип с плавающей точкой с помощью sitofp
                return builder.sitofp(value, target_type)

            # если целевой тип - булевый
            elif target_type == cls.bool:
                # проверка value на неравенство нулю
                # возвращаем результат проверки
                return builder.icmp_unsigned('!=', value, cls.bool(0))

            # если целевой тип - указатель
            elif type(target_type) == ir.PointerType:
                # преобразование value в указатель с помощью inttoptr
                return builder.inttoptr(value, target_type)

        # если тип value - с плавающей точкой
        elif cls.is_float(value.type):
            if cls.is_float(target_type):
                if value.type == cls.float:
                    return builder.fpext(value, cls.double)
                else:
                    return builder.fptrunc(value, cls.float)
            
            elif cls.is_int(target_type):
                return builder.fptosi(value, target_type)

        # если тип value - указатель и тип target_type - целочисленный
        elif type(value.type) == ir.PointerType and type(target_type) == ir.IntType:
            # с помощью метода ptrtoint() конвертируем указатель в целочисленное значение
            # возвращаем это значение
            return builder.ptrtoint(value, target_type)

        # если тип value - массив и тип target_type - указатель
        elif type(value.type) == ir.ArrayType and type(target_type) == ir.PointerType and value.type.element == target_type.pointee:
            # создание константы нуля
            zero = ir.Constant(cls.int, 0)
            # создание временного указателя на массив
            tmp = builder.alloca(value.type)
            # запись во временный указатель значения value
            builder.store(value, tmp)
            # возвращаем индекс эл-та массива с индексом 0
            return builder.gep(tmp, [zero, zero])

        # если обе переменные являются массивами и их эл-ты одинаковы
        elif isinstance(value.type, ir.ArrayType) and isinstance(target_type, ir.ArrayType) and value.type.element == target_type.element:
            # преобразование типов с помощью метода bitcast()
            # приводим массив одного типа к другому типу
            return builder.bitcast(value, target_type)

        # если оба типа являются указателями
        elif isinstance(value.type, ir.PointerType) and isinstance(target_type, ir.PointerType):
            # преобразование типов с помощью метода bitcast()
            # приводим указатель одного типа к другому типу
            return builder.bitcast(value, target_type)

        raise SemanticError(msg=f"No known conversion from {value.type} to {target_type}", ctx=ctx)
