def removeNthFromEnd(head, n):
    len = 0
    temp = head
    while temp is not None:
        len += 1
        temp = temp.next
    if n == len:
        new_head = head.next
        del head
        return new_head

    position_to_stop = len - n
    count = 1
    temp = head
    while count < position_to_stop:
        temp = temp.next
        count += 1

    temp.next = temp.next.next
    return head

def removeNthFromEnd2(head, n):
    slow = head
    fast = head
    for i in range(n):
        fast = fast.next

    if fast is None:
        return head.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head

