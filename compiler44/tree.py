import os
from parsing import *


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

    gv_file = open("graph_expr3.gv", "w")

    gv_file.write(f'graph ""\n\t{{\n\t')
    gv_file.write(f'label="{expression}"\n\t')

    for pairs in output_dict:
        gv_file.write(f'{pairs} ;\n\t')
    for item in output_labels:
        gv_file.write(f'{str(item)}')

    gv_file.write('}\n')
    gv_file.close()

    os.system("dot -Tsvg graph_expr3.gv -o graph_expr3.svg")
    os.system("explorer graph_expr3.svg")


def create_tree(expression):
    gv_file = open("tree3.gv", "w")

    gv_file.write(f'graph ""\n\t{{\n\t')
    gv_file.write(f'label="{expression}"\n\t')

    nodes = mass[::-1]

    for i in range(len(nodes)):
        if len(nodes[i][2]) == 1 and len(nodes[i][1]) > 1:
            nodes[i] = (nodes[i][0], nodes[i][2], nodes[i][1])
    #print(nodes)

    num = 1
    num_a = 1
    lables = ""

    for pair in nodes:
        for char in pair:
            if f'[label="{" ".join(char)}"] ;\n\t' not in lables:
                lables += f'n{str(num).zfill(3)} [label="{" ".join(char)}"] ;\n\t'
                num += 1
    gv_file.write(lables)

    for i in range(len(nodes)):
        gv_file.write(f'n{str(num_a).zfill(3)} -- n{str(num_a + 1).zfill(3)};\n\t')
        gv_file.write(f'n{str(num_a).zfill(3)} -- n{str(num_a + 2).zfill(3)};\n\t')
        num_a += 2

    gv_file.write('}\n')
    gv_file.close()

    os.system("dot -Tsvg tree3.gv -o tree3.svg")
    os.system("explorer tree3.svg")