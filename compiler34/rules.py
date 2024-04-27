from preprocessTXT import *


def delete_chain_rules(grammar):
    print(f"~~~ DELETING CHAIN RULES ~~~")
    rules = grammar['rules']
    not_term = grammar['not_term']

    chain_pairs = []

    for nt in not_term:
        chain_pairs.append((nt, nt))

    print(f"Chain pairs for every not_term: {chain_pairs}")

    all_chain_rules = []
    print("Chain rules: ")
    for key in rules:
        for rule in rules[key]:
            if len(rule) == 1 and rule[0] in not_term:
                all_chain_rules.append((key, rule[0]))
                print(f"{key} -> {rule[0]}")

    for pair in all_chain_rules:
        for c_p in chain_pairs:
            if pair[0] == c_p[1]:
                chain_pairs.append((c_p[0], pair[1]))

    print(f"New chain pairs: {chain_pairs}")

    filtered_pairs = [pair for pair in chain_pairs if pair[0] != pair[1]]
    print(f"Filtered pairs: {filtered_pairs}")

    new_rules = grammar['rules'].copy()
    print(f"Copy rules: {new_rules}")

    for pair in filtered_pairs:
        for key in new_rules:
            if pair[0] == key:
                for r in rules[pair[1]]:
                    new_rules[key].append(r)

    print(f"New rules: {new_rules}")

    for pair in filtered_pairs:
        for key in new_rules:
            if [pair[1]] in new_rules[key]:
                new_rules[key].remove([pair[1]])

    print(f"Filtered new rules: {new_rules}")
    grammar['rules'] = new_rules

    return grammar


gr = read_grammar('print423.txt', 'chain_rules423.txt')
print_grammar('Input grammar', gr, 'print4231.txt')

chain = delete_chain_rules(gr)
print_grammar('Result grammar', chain, 'print4232.txt')

write_grammar(chain, 'output_grammar423.txt')