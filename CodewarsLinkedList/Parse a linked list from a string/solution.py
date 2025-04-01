def linked_list_from_string(s):
    if not isinstance(s, str):
        return 'None'

    s = s.split(" -> ")

    nodes_list = []

    for index, data in enumerate(s):
        if index == len(s) - 1:
            pass
        else:
            nodes_list.append(Node(int(data)))

    for index, node in enumerate(nodes_list):
        if index + 1 == len(nodes_list):
            node.next =  None
        else:
            node.next = nodes_list[index + 1]

    return nodes_list[0] if nodes_list else None
