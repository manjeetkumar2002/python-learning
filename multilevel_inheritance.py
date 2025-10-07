#parent1->child1->child2->...->child n
# we can also derive a child class from a derived class
#grandparent->parent->son

#the parent of Human class is object class
# object class is the root class
class Human(object) :
    def __init__(self):
        print("Human init")
        self.name = 'Human'
        self.age = 18
    def eat(self):
        print("eating")

    def work(self):
        print("coding")
class Male(Human) :
    def sleep(self):
        print("sleeping")

    def work(self):
        print("cooking")

class Boy (Male) :
    def work(self) :
        # Human.work(self)
        # super().work()
        print("working")
class Programmer(Boy) :
    language = 'Python' #it is a class variable
    def work(self):
        print("i write programs")

boy1 = Boy()
boy1.eat()
boy1.sleep()
boy1.work()

pro1 = Programmer()
pro1.eat()
pro1.work()
print(pro1.name)
print(pro1.age)
print(boy1.name)
print(boy1.age)

print(Programmer.mro())