# модуль для выполнения декодирования
import codecs


# Декодирование escape-последовательностей в строке 's':
# принимает строку 's' в качестве аргумента,
# преобразует ее в байтовую строку с кодировкой ASCII,
# декодирует escape-последовательности с помощью codecs.escape_decode,
# возвращает декодированную строку с кодировкой ASCII
def parse_escape(s):
    return codecs.escape_decode(bytes(s, "ascii"))[0].decode("ascii")


# Проверка соответствия правила объекта ctx:
# принимает объект ctx и правило rule в качестве аргументов
# p.s: проверяет, существует ли у объекта ctx метод getRuleIndex()
def match_rule(ctx, rule):
    if hasattr(ctx, 'getRuleIndex'):
        return ctx.getRuleIndex() == rule
    else:
        return False


# Проверка присутствия определенного текста в объекте ctx:
# принимает объект ctx и список текстов texts в качестве аргументов
# p.s: проверяет, существует ли у объекта ctx метод getText()
def match_texts(ctx, texts):
    if hasattr(ctx, 'getText'):
        return ctx.getText() in texts
    else:
        return False


# Проверка присутствия конкретного текста в объекте ctx:
# принимает объект ctx и текст text в качестве аргументов
# в качестве аргумента передаётся текст в виде списка [text]
def match_text(ctx, text):
    return match_texts(ctx, [text])
