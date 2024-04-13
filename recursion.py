from preprocessTXT import *


# удаление левой рекурсии (алгоритм 4.8)
def delete_left_recursion(grammar):
    print("~~~ DELETING LEFT RECURSION ~~~")
    # словарь правил из переданной грамматики
    rules = grammar['rules']
    # список всех нетерминалов из словаря правил грамматики
    not_term = list(rules.keys())
    # копия словаря нетерминалов грамматики
    new_not_term = grammar['not_term'].copy()

    # для каждого индекса в диапазоне длины списка not_term
    # двойной цикл по всем нетерминалам a_i и a_j
    for i in range(len(not_term)):
        a_i = not_term[i]

        for j in range(i):
            a_j = not_term[j]

            # УСТРАНЕНИЕ КОСВЕННОЙ РЕКУРСИИ
            print("\n~~~ Deleting indirect recursion ~~~")

            # списки правил для нетерминалов a_i и a_j
            a_i_array = rules[a_i]
            print(f"Rules for a_i = {a_i}: {a_i_array}")
            a_j_array = rules[a_j]
            print(f"Rules for a_j = {a_j}: {a_j_array}")

            # пустой список для хранения новых правил (для a_i)
            new_production_array = []

            # вложенный цикл по правилам нетерминала a_i
            for k in range(len(a_i_array)):
                new_production = []

                # проверка, равен ли первый символ текущего правила нетерминалу a_j
                if a_i_array[k][0] == a_j:
                    # вложенный цикл по правилам нетерминала a_j
                    for a_j_production in a_j_array:
                        # если последний символ правила a_j равен 'eps'
                        if a_j_production[-1] == 'eps':
                            # удаляем последний символ
                            a_j_production = a_j_production[:-1]

                        # добавление в список нового правила
                        # объединяем правило a_j и оставшуюся часть правила a_i
                        new_production_array.append(a_j_production + a_i_array[k][1:])
                        print(f"{a_j_production + a_i_array[k][1:]} added in new production for a_i")
                else:
                    # добавляем текущее правило в новые
                    new_production.extend(a_i_array[k])
                    print(f"{a_i_array[k]} added in new production")

                # если новое правило не пусто
                if len(new_production) > 0:
                    # добавляем его в список новых правил
                    new_production_array.append(new_production)
                    print(f"{new_production} added in new production for a_i")

            # обновляем словарь правил для нетерминала a_i списком новых правил
            rules[a_i] = new_production_array
            print(f"Rules for a_i = {a_i} updated: {rules[a_i]}")

        # УСТРАНЕНИЕ НЕПОСРЕДСТВЕННОЙ РЕКУРСИИ
        print("\n~~~ Deleting immediate recursion ~~")
        # для текущего нетерминала a_i устраняем непосредственную рекурсию
        new_rules, new_not_terminal = delete_immediate_recursion({a_i: rules[a_i]})
        # добавляем список новых нетерминалов в мн-во new_not_term
        new_not_term += list(new_not_terminal)
        print(f"New not_term: {new_not_term}")

        # для каждого нетерминала как ключа в словаре new_rules
        for nt in new_rules:
            # копирование правил из словаря new_rules в словарь rules
            rules[nt] = new_rules[nt]
            print(f"{nt} -> {rules[nt]}")

    grammar['rules'] = rules             # словарь правил
    grammar['not_term'] = new_not_term   # словарь новых нетерминалов

    return grammar


# устранение непосредственной рекурсии
def delete_immediate_recursion(rules):
    # копия правил грамматики
    new_rules = rules.copy()
    # пустое мн-во для хранения нетерминалов
    new_not_term = set()

    # итерация по эл-там словаря правил грамматики
    # left -- левый символ
    # right -- список правил для этого символа
    for left, right in rules.items():
        # индекс для создания новых символов
        add_index = 1
        # пустой список для хранения alpha-частей правил
        alpha = []
        # пустой список для хранения оставшихся правил
        betta = []

        # итерация по правилам символа
        for i in range(len(right)):
            # проверка, начинается ли текущее правило с левого символа
            # и имеет ли оно длину больше или равную 1
            if right[i][0] == left and len(right[i]) >= 1:
                # добавим alpha-часть правила в список
                # [1:] -- добавляем все эл-ты right[i] кроме первого
                alpha.append(right[i][1:])
                print(f"{right[i][1:]} added in alpha-parts of rules")
            else:
                betta.append(right[i])
                print(f"{right[i]} added in betta")

        if len(betta) == 0:
            # если список betta пуст, добавляем в него пустой список
            betta.append([])
            print("[] added in betta")

        # если список alpha не пустой
        if len(alpha) > 0:
            # создаём новый символ для замены непосредственной рекурсии
            new_symbol = left + str(add_index)
            # добавляем его в мн-во новых нетерминалов
            new_not_term.add(new_symbol)
            print(f"{new_symbol} added in new not_term")

            # в словаре new_rules создаём пустые списки правил
            # для символов left и new_symbol
            new_rules[left] = []
            new_rules[new_symbol] = []

            # для каждого индекса в диапазоне длины списка betta
            for i in range(len(betta)):
                # присваиваем текущий символ из списка betta переменной symbol
                symbol = betta[i]

                if betta[i] == ['eps']:
                    # присваиваем пустой список переменной symbol
                    symbol = []

                # для символа left в словарь добавляем правило symbol + [new_symbol]
                new_rules[left].append(symbol + [new_symbol])
                print(f"{symbol + [new_symbol]} added in new rules for 'left'")

            # для каждого индекса в диапазоне длины списка alpha
            for i in range(len(alpha)):
                # для символа new_symbol в словарь добавляем правило alpha[i] + [new_symbol]
                new_rules[new_symbol].append(alpha[i] + [new_symbol])
                print(f"{alpha[i] + [new_symbol]} added in new rules for '{new_symbol}'")

            # для символа new_symbol в словарь добавляем правило [epsilon]
            new_rules[new_symbol].append(['eps'])
            print(f"'eps' added in new rules for '{new_symbol}'")

    return new_rules, new_not_term


# левая факторизация (алгоритм 4.10)
def left_factorization(grammar):
    print("\n~~~ Left factorizing ~~")
    # пустой словарь новых правил грамматики
    rules = {}
    # пустой словарь для символов, для которых применима пустая цепочка
    epsilon = {}

    # для каждого эл-та словаря правил грамматики
    # symbol -- символ грамматики
    # rule -- список правил для этого символа
    for symbol, rule in grammar['rules'].items():
        # для символа symbol устанавливаем значение False в словаре epsilon
        epsilon[symbol] = False
        # определяем самый длинный префикс для списка правил rule
        prefix = get_longest_prefix(rule)
        print(f"\nLongest prefix: {prefix}")

        if len(prefix) == 0:
            # если длина префикса равна 0
            # переходим к следующей итерации цикла
            continue

        # новый символ, который будет использоваться для замены левой рекурсии
        new_symbol = symbol

        # пока есть префикс
        while len(prefix) > 0:
            # добавляем к новому символу единицу
            new_symbol += "1"
            # пустой список для хранения правил с alpha-частью
            alpha_arr = []
            # пустой список для хранения оставшихся правил
            betta_arr = []

            # итерация по правилам символа
            for r in rule:
                # проверка, совпадает ли префикс с началом правила r
                if prefix == r[:len(prefix)]:
                    # выделение alpha-части правила r
                    alpha = r[len(prefix):]

                    # проверка, больше ли нуля длина alpha-части
                    if len(alpha) > 0:
                        # в список alpha_arr добавляем alpha-часть правила
                        alpha_arr.append(alpha)
                        print(f"{alpha} added in alpha-parts of rules")
                    else:
                        # установка флага пустой цепочки для нового символа
                        epsilon[new_symbol] = True
                else:
                    # в список betta_arr добавляем правило r
                    betta_arr.append(r)
                    print(f"{r} added in betta")

            # добавляем новый символ по ключу нетерминалов грамматики
            grammar['not_term'].append(new_symbol)
            print(f"{new_symbol} added not_terms")

            # обновление правил для текущего символа
            # добавляем новый символ в начало и оставшиеся правила
            rules[symbol] = [prefix + [new_symbol]] + betta_arr
            print(f"For {symbol} added rules {rules[symbol]}")

            # установка новых правил из alpha_arr для нового символа
            rules[new_symbol] = alpha_arr
            print(f"For {new_symbol} added rules {rules[new_symbol]}")

            # получение правил для символа из словаря правил
            production = rules[symbol]
            print(f"For {symbol} updated production: {production}")

            # получение самого длинного префикса для обновлённых правил
            prefix = get_longest_prefix(production)

    # для каждого нетерминала в словаре правил
    for symbol in rules:
        # в словарь правил грамматики для данного символа
        # присваиваем правила по текущему нетерминалу из словаря правил rules
        grammar['rules'][symbol] = rules[symbol]
        print(f"For {symbol} added rules: {rules[symbol]}")

        # если текущий нетерминал содержится в словаре epsilon
        # и соответсвующее значение не равно пустому списку
        # (т.е данный нетерминал можно заменить на eps)
        if symbol in epsilon and epsilon[symbol]:
            # добавление eps-правила к списку правил
            # для текущего символа в словаре правил грамматики
            grammar['rules'][symbol].append(['eps'])
            print(f"For {symbol} added 'eps' in rules")

    return grammar


def get_longest_prefix(rules):
    # список, содержащий строки правил производства
    production_string_array = []

    # для каждого правила из списка правил
    for r in rules:
        s = ""
        # для каждого индекса в диапазоне длины правила
        for i in range(len(r)):
            s += r[i] + "|"

        # добавляем строку s в список правил производства
        production_string_array.append(s)
    # сортируем список по возрастанию
    production_string_array.sort()

    max_prefix = ""

    # для каждого индекса в диапазоне до длины списка - 1
    for i in range(len(production_string_array) - 1):
        prod1 = production_string_array[i]
        prod2 = production_string_array[i+1]

        prefix = ""

        # для каждого индекса в диапазоне до минимальной из длин prod1 и prod2
        for j in range(min(len(prod1), len(prod2))):
            if prod1[j] == prod2[j]:
                # если символы в текущем индексе совпали
                # символ добавляем к текущему префиксу
                prefix += prod1[j]
            else:
                # иначе
                if len(prefix) > len(max_prefix):
                    # если текущий префикс длиннее чем самый длинный
                    # обновляем самый длинный префикс с помощью текущего
                    max_prefix = prefix

                # сбрасываем текущий префикс и прерываем внутренний цикл
                prefix = ""
                break

        # после завершения вложенного цикла
        # проверка, не превышает ли текущий префикс самый длинный
        if len(prefix) > len(max_prefix):
            max_prefix = prefix

    # создаём массив символов самого длинного общего префикса
    # разделяем по символу '|' и удаляем последний эл-т (пустую строку)
    # [:-1] -- начало среза эл-тов отсчитывается с конца (-1 -- последний эл-т списка)
    max_prefix_arr = max_prefix.split("|")[:-1]
    # print(f"Max prefix: {max_prefix_arr}")
    return max_prefix_arr


gr = read_grammar('example3.txt', 'input_grammar3.txt')
print_grammar('Input grammar', gr)

gr1 = delete_left_recursion(gr)
print_grammar('Grammar after deleting LR', gr1)

out_gr = left_factorization(gr1)
print_grammar('Left factorization', out_gr)

write_grammar(out_gr, 'output_grammar3.txt')
