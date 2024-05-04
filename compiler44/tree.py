import os


def parse_tuple(t, new_tuple):
    if isinstance(t, tuple):
        parent = t[0]
        children = t[1:]
        child_t = [child[0] if isinstance(child, tuple) else child for child in children]

        for i in range(len(child_t)):
            new_tuple.append((parent, child_t[i]))
            # print(f"{parent} -- {child_t[i]}")

        for child in children:
            parse_tuple(child, new_tuple)

    return new_tuple


def transform_array(input_array):
    node_dict = {}
    node_counter = 1

    def get_node_number(node):
        nonlocal node_counter
        if node not in node_dict:
            node_dict[node] = f'n{str(node_counter).zfill(3)}'
            node_counter += 1
        return node_dict[node]

    output_list = []
    output_labels = []
    transformed_labels = ""

    for pair in input_array:
        nodes = pair.split(' -- ')
        transformed_pair = f'{get_node_number(nodes[0])} -- {get_node_number(nodes[1])}'
        output_list.append(transformed_pair)
        if f'{get_node_number(nodes[0])} [label="{nodes[0]}"] ;\n\t' not in transformed_labels:
            transformed_labels += f'{get_node_number(nodes[0])} [label="{nodes[0]}"] ;\n\t'
        if f'{get_node_number(nodes[1])} [label="{nodes[1]}"] ;\n\t' not in transformed_labels:
            transformed_labels += f'{get_node_number(nodes[1])} [label="{nodes[1]}"] ;\n\t'

    output_labels.append(transformed_labels)

    return output_list, output_labels


def convert_to_graph_expression(expression, result):
    pairs = []
    parse_tuple(result, pairs)
    #print(pairs)

    parents = []
    for pair in pairs:
        parents.append(f"{pair[0]} -- {pair[1]}")

    # print(parents)

    output_dict, output_labels = transform_array(parents)
    # print(output_dict)
    # print(output_labels)

    gv_file = open("graph_expr.gv", "w")

    gv_file.write(f'graph ""\n\t{{\n\t')
    gv_file.write(f'label="{expression}"\n\t')

    for pairs in output_dict:
        gv_file.write(f'{pairs} ;\n\t')
    for item in output_labels:
        gv_file.write(f'{str(item)}')

    gv_file.write('}\n')
    gv_file.close()

    os.system("dot -Tsvg graph_expr.gv -o graph_expr.svg")
    os.system("explorer graph_expr.svg")


def create_tree(expression, polish_notation):
    gv_file = open("tree.gv", "w")

    gv_file.write(f'graph ""\n\t{{\n\t')
    gv_file.write(f'label="{expression}"\n\t')

    clear_expr = polish_notation.replace(" ", "")
    #print(clear_expr)

    pairs = []
    for i in range(len(clear_expr)-1, 0, -1):
        if clear_expr[i] == "!" or clear_expr[i] == "&":
            if clear_expr[i-1] != "~":
                pairs.append((clear_expr[:i-1], clear_expr[i-1]))
            else:
                pairs.append((clear_expr[:i-2], clear_expr[i-2:i]))
        if clear_expr[i] == "~":
            pairs.append((clear_expr[:i-1], clear_expr[i-1:i]))
    #print(pairs)

    pairs = [(pair[0], pair[1]) for pair in pairs if not (pair[0].isalpha() and pair[1].isalpha())]
    #print(pairs)

    for pair in pairs:
        for char in pair:
            if len(char) == 2 and char[0].isalpha() and char[1] == "~":
                pairs.append((pair[1][0], pair[1][1]))
                break
    #print(pairs)

    num = 1

    gv_file.write(f'n{str(num).zfill(3)} [label="{polish_notation}"] ;\n\t')
    num += 1

    num_a = 1

    for pair in pairs:
        for char in pair:
            gv_file.write(f'n{str(num).zfill(3)} [label="{" ".join(char)}"] ;\n\t')
            num += 1
        gv_file.write(f'n{str(num_a).zfill(3)} -- n{str(num_a + 1).zfill(3)};\n\t')
        gv_file.write(f'n{str(num_a).zfill(3)} -- n{str(num_a + 2).zfill(3)};\n\t')
        num_a += 2

    gv_file.write('}\n')
    gv_file.close()

    os.system("dot -Tsvg tree.gv -o tree.svg")
    os.system("explorer tree.svg")