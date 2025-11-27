class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at(self,val,position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return
        else:
            current = self.head
            count = 0
            while current and count < position-1:
                current = current.next
                count += 1
            if current is None:
                print("Position %d is out of bounds" % position)
                return
            new_node.next = current.next
            new_node.prev = current

            if current.next:
                current.next.prev = new_node
            current.next = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.val,end="->")
            current = current.next
#
# dll = DoublyLinkedList()
# dll.append(5)
# dll.append(6)
# dll.append(7)
# dll.insert_at_head(4)
# dll.insert_at(10,2)
# dll.traverse()