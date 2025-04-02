def alternating_split(head):
    if head is None or head.next is None:
        raise TypeError

    odd = head
    even = head.next

    first = odd
    second = even


    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = None

    return Context(first, second)