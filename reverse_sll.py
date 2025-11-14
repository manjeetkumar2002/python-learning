from Singly_LinkedList import SinglyLinkedList

list = SinglyLinkedList()
list.append(10)
list.append(20)
list.append(30)
list.append(40)
list.append(50)

def reverse_list(head):
    curr_node = head
    prev_node = None
    next_node = None
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node

list.head = reverse_list(list.head)
print(list)