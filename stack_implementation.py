# using array

class Stack :
    def __init__(self):
        self.arr = []

    def push(self,value):
        self.arr.append(value)

    def pop(self):
        if self.isEmpty() :
            return None
        return self.arr.pop()

    def top(self):
        return self.arr[-1]

    def isEmpty(self):
        return len(self.arr)==0

    def __str__(self) :
        result = ""
        while not s.isEmpty():
            result += str(self.pop()) + " "
        return result

s = Stack()
s.push(1)
s.push(2)
s.push(3)


print(s)
