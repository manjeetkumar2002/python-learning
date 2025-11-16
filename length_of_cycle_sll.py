#APPROACH 2: using floyd cycle detection
def lengthOfLoop(head):
    slow,fast = head,head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            count = 1
            while slow != fast:
                slow = slow.next
                count += 1
            return count
    return 0

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