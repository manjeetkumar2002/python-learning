from DoublyLinkedList import DoublyLinkedList

def del_all_occurences_of_key_dll(head,key):
    if head.next is None and head.val == key:
        return None
    temp = head
    prev = None
    new_head = head
    while temp is not None:
        if temp.val == key:
            if prev is not None:
                prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = prev
            if temp == new_head:
                new_head = new_head.next
            temp = temp.next
        else:
            prev = temp
            temp = temp.next
    return new_head
dll = DoublyLinkedList()
dll.append(5)
dll.append(3)
dll.append(1)
dll.append(1)
dll.append(1)
dll.append(2)
dll.append(1)
dll.head = del_all_occurences_of_key_dll(dll.head,1)
dll.traverse()