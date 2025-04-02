def loop_size(node):
    visited = {}
    index = 0
    current = node

    while current:
        if current in visited:
            return index - visited[current]
        
        visited[current] = index
        index += 1
        current = current.next