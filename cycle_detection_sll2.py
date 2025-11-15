def detectCycle(head):
    my_set = set()
    temp = head
    while temp:
        if temp in my_set:
            return temp
        my_set.add(temp)
        temp = temp.next
    return None

def detectCycle2(head):
    slow,fast = head,head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast is None or fast.next is None:
        return None

    slow = head
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return slow