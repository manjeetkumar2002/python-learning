from Singly_LinkedList import SinglyLinkedList

list = SinglyLinkedList()
list.append(10)
list.append(20)
list.append(30)
list.append(40)
list.append(50)
list.append(60)

#opitimal approach
def middle_element(head):
    if head is None:
        return -1
    slow = head
    fast = head
    while fast.next  is not None and fast is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.val

# Brute force
def middle_element1(head):
    curr = head
    count = 0
    while curr is not None:
        count += 1
        curr = curr.next

    curr = head
    for i in range(0,count//2):
        curr = curr.next
    return curr.val
print("middle element is :",middle_element1(list.head))