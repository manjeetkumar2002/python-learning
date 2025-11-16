#APPROACH 2: using floyd cycle detection
def lengthOfLoop(head):
    slow,fast = head,head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast is None or fast.next is None:
        return 0

    slow = head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    # find the length
    temp = slow.next
    length = 0
    while temp != slow:
        length = length + 1
        temp = temp.next
    length = length + 1
    return length

#APPROACH 1: using dictionary
def lengthOfLoop(head):
    my_dict = dict()
    temp = head
    travel = 0
    while temp is not None:
        if temp in my_dict:
            return travel - my_dict[temp]
        my_dict[temp] = travel
        travel = travel + 1
        temp = temp.next

    return 0