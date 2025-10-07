# A single parent can have multiple children

class Human(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("eating")
    def showDetails(self):
        print(self.name,self.age,)
class Male(Human):
    def __init__(self,name,age,location):
        # super().__init__(name,age)
        Human.__init__(self,name,age)
        self.location = location
    def sleep(self):
        print("sleeping")
    def showDetails(self):
        super().showDetails()
        print(self.location)

class Female(Human):
    def dance(self):
        print("dancing")


female1 = Female("jenny",22)
female1.eat()
female1.dance()

male1 = Male("amit",43,"gurugram")
male1.sleep()
male1.eat()

female1.showDetails()
male1.showDetails()