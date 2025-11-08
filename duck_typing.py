class Duck:
    def swim(self):
        print("I am duck and i can swin")
    def speak(self):
        print("Quack Quack")
class Dog:
    def swim(self):
        print("I am Dog and i can swin")
    def speak(self):
        print("woof woof")

class Demo :
    def display(self,obj):
        obj.swim()
        obj.speak()
        print("Info displayed successfully")

demo = Demo()
demo.display(Dog())
demo.display(Duck())