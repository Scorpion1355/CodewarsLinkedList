def reverse(head):
    # your code goes here.
    if head is None or head.next is None:
        return head
    
    linked_list = reverse(head.next)
    
    head.next.next = head
    head.next = None
    
    return linked_list