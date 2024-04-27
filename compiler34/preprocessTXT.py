def read_grammar(file_from, file_to):
    grammar_rules = {}

    with open(file_from, 'r') as file:
        input_file = open(f"{file_to}", "w")

        data = file.read().splitlines()

        print("------- Not terminals -------")

        not_term = data[0].strip(' ').strip('\n').split(' ')

        print(f"Number of not terminals: {len(not_term)}")
        input_file.write(f"{str(len(not_term))}\n")

        for n_t in not_term:
            print(n_t)
            input_file.write(f"{n_t} ")
        print(not_term)

        print("\n------- Terminals -------")

        term = data[1].strip(' ').strip('\n').split(' ')

        print(f"Number of terminals: {len(term)}")
        input_file.write(f"\n{str(len(term))}\n")

        for t in term:
            print(t)
            input_file.write(f"{t} ")
        print(term)

        print("\n------- Rules -------")

        rules = data[2:-1]
        print(f"Number of rules: {len(rules)}")

        for line in rules:
            in_rules = line.strip(' ').strip('\n').split('|')
            rule = in_rules[0].strip(' ').strip('\n').split(' ')
            leftSymb = rule[0]

            if leftSymb not in grammar_rules:
                grammar_rules[leftSymb] = [rule[2:]]
            else:
                grammar_rules[leftSymb].append(rule[2:])

            for r_rules in in_rules[1:]:
                rule = r_rules.strip(' ').strip('\n').split(' ')
                grammar_rules[leftSymb].append(rule)

        for key in grammar_rules:
            print(f"{key}: {grammar_rules[key]}")

        count = 0

        print("\nSplit rules:")
        for key in grammar_rules:
            for pair in grammar_rules[key]:
                if len(pair) > 1:
                    print(f"{key} -> {' '.join(pair)}")
                    count += 1
                else:
                    print(f"{key} -> {pair[0]}")
                    count += 1

        print(f"Number of split rules: {count}")
        input_file.write(f"\n{count}\n")

        for key in grammar_rules:
            for pair in grammar_rules[key]:
                if len(pair) > 1:
                    input_file.write(f"{key} -> {' '.join(pair)}\n")
                else:
                    input_file.write(f"{key} -> {pair[0]}\n")

        print("\n------- Start -------")
        start = data[-1]
        print(start)
        input_file.write(f"{start}\n")

        input_file.close()

    grammar = {
        'not_term': not_term,
        'term': term,
        'rules': grammar_rules,
        'start': start
    }

    return grammar


def print_grammar(message, grammar, file_to):
    result_file = open(f"{file_to}", "w")

    for not_term in grammar['not_term']:
        result_file.write(f"{not_term} ")
    result_file.write("\n")

    for term in grammar['term']:
        result_file.write(f"{term} ")
    result_file.write("\n")

    print(f"\n<<< {message} >>>")
    for symbol, production in grammar['rules'].items():
        print(f"{symbol} ->", end=' ')
        result_file.write(f"{symbol} -> ")

        for i in range(len(production)):
            for p_i in production[i]:
                print(p_i, end=' ')
                result_file.write(f"{p_i} ")

            if i < len(production) - 1:
                print('|', end=' ')
                result_file.write("| ")
        print()
        result_file.write("\n")
    print('\n')
    result_file.write(grammar['start'])

    result_file.close()


def write_grammar(grammar, file_to):
    result_file = open(f"{file_to}", "w")

    result_file.write(f"{len(grammar['not_term'])}\n")
    for n_t in grammar['not_term']:
        result_file.write(f"{n_t} ")

    result_file.write(f"\n{len(grammar['term'])}\n")
    for t in grammar['term']:
        result_file.write(f"{t} ")

    count = 0
    for key in grammar['rules']:
        for pair in grammar['rules'][key]:
            count += 1

    result_file.write(f"\n{count}\n")

    for key in grammar['rules']:
        for pair in grammar['rules'][key]:
            if len(pair) > 1:
                result_file.write(f"{key} -> {' '.join(pair)}\n")
            else:
                result_file.write(f"{key} -> {pair[0]}\n")

    result_file.write(f"{grammar['start']}\n")

    result_file.close()


# gr = read_grammar('example2.txt', 'input_grammar2.txt')
# print_grammar('Input grammar', gr)
# write_grammar(gr, 'output_grammar2.txt')