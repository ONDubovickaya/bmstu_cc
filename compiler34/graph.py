import os


def parse_tuple(t, new_tuple):
    if isinstance(t, tuple):
        parent = t[0]
        children = t[1:]
        child_t = [child[0] if isinstance(child, tuple) else child for child in children]

        for i in range(len(child_t)):
            new_tuple.append((parent, child_t[i]))
            print(f"{parent} -- {child_t[i]}")

        for child in children:
            parse_tuple(child, new_tuple)

    return new_tuple


def transform_dict(input_dict):
    node_dict = {}
    node_counter = 1

    def get_node_number(node):
        nonlocal node_counter
        if node not in node_dict:
            node_dict[node] = f'n{str(node_counter).zfill(3)}'
            node_counter += 1
        return node_dict[node]

    output_dict = {}
    output_labels = {}
    for key, value_list in input_dict.items():
        output_list = []
        labels_list = []
        transformed_labels = ""
        for value_pair in value_list:
            nodes = value_pair.split(' -- ')
            transformed_pair = f'{get_node_number(nodes[0])} -- {get_node_number(nodes[1])}'
            output_list.append(transformed_pair)
            if f'{get_node_number(nodes[0])} [label="{nodes[0]}"] ;\n\t' not in transformed_labels:
                transformed_labels += f'{get_node_number(nodes[0])} [label="{nodes[0]}"] ;\n\t'
            if f'{get_node_number(nodes[1])} [label="{nodes[1]}"] ;\n\t' not in transformed_labels:
                transformed_labels += f'{get_node_number(nodes[1])} [label="{nodes[1]}"] ;\n\t'
        labels_list.append(transformed_labels)
        node_dict = {}
        output_dict[key] = output_list
        output_labels[key] = labels_list

    return output_dict, output_labels


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
    print(pairs)

    parents = []
    for pair in pairs:
        parents.append(f"{pair[0]} -- {pair[1]}")

    print(parents)

    output_dict, output_labels = transform_array(parents)
    print(output_dict)
    print(output_labels)

    gv_file = open("graph_expr2.gv", "w")

    gv_file.write(f'graph ""\n\t{{\n\t')
    gv_file.write(f'label="{expression}"\n\t')

    for pairs in output_dict:
        gv_file.write(f'{pairs} ;\n\t')
    for item in output_labels:
        gv_file.write(f'{str(item)}')

    gv_file.write('}\n')
    gv_file.close()

    os.system("dot -Tsvg graph_expr2.gv -o graph_expr2.svg")
    os.system("explorer graph_expr2.svg")


def convert_to_graph_program(expression, result):
    dict_for_result = {}
    for i in range(len(result)):
        if i % 2 == 0:
            dict_for_result[result[i]] = result[i + 1]
    print(dict_for_result)

    num = 1
    new_tuple = []
    new_dict = {}

    for key, value in dict_for_result.items():
        print(f"operator{num}")
        parse_tuple(value, new_tuple)
        num += 1
        new_dict[key] = new_tuple
        new_tuple = []
    print(new_dict)

    parents = []
    parents_dict = {}

    for key, value in new_dict.items():
        for pair in value:
            parents.append(f"{pair[0]} -- {pair[1]}")
        parents_dict[key] = parents
        parents = []

    print(parents_dict)

    transformed_dict, trans_labels = transform_dict(parents_dict)
    print(transformed_dict)
    print(trans_labels)

    gv_file = open("graph_prog2.gv", "w")

    cluster_num = 1
    node_num = 0

    gv_file.write(f'graph ""\n\t{{\n\t')
    gv_file.write(f'label="{expression}"\n')

    for operator, pairs in transformed_dict.items():
        node_num += 1
        gv_file.write(f'\n\tsubgraph cluster{cluster_num:02}\n\t{{\n\t')
        gv_file.write(f'label="{operator}"\n\t')
        gv_file.write(f'n{node_num:03} ;\n\t')
        for pair in pairs:
            gv_file.write(f'{pair} ;\n\t')
            node_num += 1
        for item in trans_labels[operator]:
            gv_file.write(f'{str(item)}')
        gv_file.write('}\n')
        cluster_num += 1

    gv_file.write('\t}\n')
    gv_file.close()

    os.system("dot -Tsvg graph_prog2.gv -o graph_prog2.svg")
    os.system("explorer graph_prog2.svg")