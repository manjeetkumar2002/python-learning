#queue using array

class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, item):
        self.arr.append(item)

    def dequeue(self):
        return self.arr.pop(0)

    def isEmpty(self):
        return self.arr == []

    def __str__(self):
        result = ""
        while not self.isEmpty():
            result = str(self.arr.pop())+" " + result
        return result

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(f"Queue: {q}")
