from Singly_LinkedList import SinglyLinkedList

list = SinglyLinkedList()
list.append(10)
list.append(20)
list.append(30)
list.append(40)
list.append(50)

def middle_element(head):
    if head is None:
        return -1
    slow = head
    fast = head
    while fast.next  is not None and fast is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.val

print("middle element is :",middle_element(list.head))