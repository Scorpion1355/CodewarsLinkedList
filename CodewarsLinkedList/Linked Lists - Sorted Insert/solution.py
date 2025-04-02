def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    if head is None or data < head.data:
        node = Node(data)
        node.next = head
        return node

    current = head.next
    prev_node = head

    while current is not None and current.data < data:
        prev_node = current
        current = current.next
    
    node = Node(data)
    node.next = current
    prev_node.next = node
        
    return head
        