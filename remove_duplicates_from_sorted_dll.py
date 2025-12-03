    from DoublyLinkedList import DoublyLinkedList

    def remove_duplicates(head):
        if head is None:
            return None
        current = head
        while current.next is not None:
            if current.next.val == current.val:
                duplicate = current.next
                current.next = duplicate.next

                if duplicate.next is not None:
                    duplicate.next.prev = current
            else:
                current = current.next
        return head
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(4)
    dll.append(5)
    dll.head = remove_duplicates(dll.head)
    dll.traverse()