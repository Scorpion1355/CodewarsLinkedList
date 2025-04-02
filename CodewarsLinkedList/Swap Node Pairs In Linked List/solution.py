
def swap_pairs(head):

    if not head or not head.next:
        return head
    
    second = head.next
    
    head.next = swap_pairs(second.next)
    
    second.next = head

    return second