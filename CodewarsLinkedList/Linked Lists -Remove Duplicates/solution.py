def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    
    if head is None:
        return None
    
    previous = head
    
    current = head.next
    while current:
        if current.data == previous.data:
            previous.next = current.next
        else:
            previous = current
            
        current = current.next
            
    return head