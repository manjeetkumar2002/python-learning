from DoublyLinkedList import DoublyLinkedList

def find_pairs(head,target):
    # find the tail of dll
    curr = head
    tail = None
    while curr.next is not None:
        curr = curr.next
    tail = curr
    #Apply two pointer approach
    left = head
    right = tail
    result = []
    while left != right:
        sum = left.val + right.val
        if sum == target:
            result.append([left.val,right.val])
            left = left.next
            right = right.prev
        elif sum < target:
            left = left.next
        else:
            right = right.prev

    return result

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(40)
dll.append(50)
dll.append(60)
dll.append(70)


print(find_pairs(dll.head,70))