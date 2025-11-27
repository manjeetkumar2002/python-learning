from DoublyLinkedList import DoublyLinkedList

def reverse_dll(head):
    current = head
    prev = None

    while current:
        front = current.next
        current.next = prev
        current.prev = front
        prev = current
        current = front
    new_head = prev
    return new_head
dll = DoublyLinkedList()
dll.append(5)
dll.append(6)
dll.append(7)
dll.append(8)
print("Before Reverse dll looks like this :")

dll.traverse()
dll.head = reverse_dll(dll.head)
print("\nAfter Reverse dll looks like this :")
dll.traverse()
