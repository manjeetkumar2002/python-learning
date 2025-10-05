# inheriting data members and behaviour from another class is called inheritance
# what and why inheritance ?
# syntax
# class derivedClass(baseClassName):
#     statements


class Human: #parent/base/superclass class
    def __init__(self, name, age):
        self.address = "delhi"
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)


class Student(Human):#derived/child/subclass
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
        self.address = "gurugram"
    #overiding the display() function
    #redefining a parent class method
    def display(self):
        # using super you can access method and attribute of base class
        # if you add extra functionality to code of base class display , use super
        super().display()
        print(self.marks)

s1 = Student("John", 24, {"Python":80, "Java":60})
s1.display()
print(s1.address)