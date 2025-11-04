class Student:
    def __init__(self,name,age,rollNo):
        self.__name = name
        self.__age = age
        self.__rollNo = rollNo
    def __display(self):
        print("Name:",self.__name)
        print("Age:",self.__age)
        print("Roll No:",self.__rollNo)
    def displayPrivateData(self):
        self.__display()
    # getters methods use to get the private members
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getRollNo(self):
        return self.__rollNo

    # setters methods set a new value to private members
    def setName(self,name):
        self.__name = name
    def setAge(self,age):
        self.__age = age
    def setRollNo(self,rollNo):
        self.__rollNo = rollNo

s1 = Student("John",19,22)
s1.displayPrivateData()
# s1.__display()
# print(s1.__name)

print(s1.getName())
print(s1.getAge())
print(s1.getRollNo())

# using name mangling
print(s1._Student__name)
print(s1._Student__age)
print(s1._Student__rollNo)


s1.setName("manjeet")
s1.setAge(23)
s1.setRollNo(13)
s1.displayPrivateData()