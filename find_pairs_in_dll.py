from DoublyLinkedList import DoublyLinkedList

def find_pairs(head,target):
    left = head
    right = head
    result = []
    while right.next is not None:
        right = right.next
    #Apply two pointer approach
    while left is not None and  right is not None and left.val < right.val:
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


print("pairs are :",find_pairs(dll.head,70))