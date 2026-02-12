class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self,val):
        # case 1: SSL is empty
        # case 2: SSL is not empty
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.val)
            curr = curr.next
    def __str__(self):
        result = ""
        curr = self.head
        while curr is not None:
            result += str(curr.val) + "->"
            curr = curr.next
        return result
    def insert_at(self,position,val):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            curr = self.head
            prev = None
            count = 0
            while curr is not None and count < position:
                count = count + 1
                prev = curr
                curr = curr.next
            prev.next = new_node
            new_node.next = curr
    def delete(self,val):
        if self.head is not None:
            if self.head.val == val:
                self.head = self.head.next
                return
            else:
                temp = self.head
                prev = None
                found = False
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                if not found:
                    print("The given value is not in the list")
                else:
                    prev.next = temp.next


list1 = SinglyLinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
print(list1)
list1.insert_at(4,10)
list1.delete(1)
list1.delete(3)
print(list1)
