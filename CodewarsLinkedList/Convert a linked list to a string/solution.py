def stringify(node):
    if not isinstance(node, Node):
        return 'None'
    output = ""
    while node.next is not None:
        output += str(node.data)
        output += " -> "
        node = node.next
    output += str(node.data)
    output += " -> "
    output += "None"
    return output