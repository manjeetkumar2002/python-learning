# APPROACH 1
def hasCycle_1(head):
    my_set = set()
    ptr = head
    while ptr is not None and ptr.next is not None:
        if ptr in my_set:
            return True
        my_set.add(ptr)
        ptr = ptr.next

    return False
# APPROACH 2
def hasCycle_2(head):
    slow,fast = head,head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
