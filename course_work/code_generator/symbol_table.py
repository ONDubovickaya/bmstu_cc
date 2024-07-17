# пользовательское исключение
# возникает при попытке повторного определения символа
class RedefinitionError(Exception):
    def __init__(self, name):
        self.name = name


# таблица символов с поддержкой вложенных областей видимости
class SymbolTable:
    def __init__(self):
        # список словарей, представляющих таблицы символов на разных уровнях области видимости
        self.__tables = [{},]
        # уровень текущей области видимости
        self.__level = 0

    # получение значения символа по ключу
    def __getitem__(self, item):
        for level in range(self.__level, -1, -1):
            if item in self.__tables[level]:
                return self.__tables[level][item]
        return None

    # установка значения символа по ключу
    # * с проверкой повторного определения символа на текущем уровне
    def __setitem__(self, key, value):
        if key in self.__tables[self.__level]:
            raise RedefinitionError(key)
        self.__tables[self.__level][key] = value

    # проверка наличия символа в таблицах символов на разных уровнях области видимости
    def __contains__(self, item):
        for level in range(self.__level, -1, -1):
            if item in self.__tables[level]:
                return True
        return False

    # переход на следующий уровень области видимости
    def enter_scope(self):
        self.__level += 1
        self.__tables.append({})

    # покидание текущего уровня области видимости
    def exit_scope(self):
        if self.__level == 0:
            return
        self.__tables.pop(-1)
        self.__level -= 1
