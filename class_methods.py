# we can add methods in a class as well as variables
class Student:
    blood_group = "B+" # CLASS OBJECT VARIABLE
    #__init__ call automatically whenever you create an object
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.followers = 0
        self.following = 0
    # self is compulsory
    # self is bind to the object on whom you are calling the method
    def display(self,subject):
        # subject is a parameter not a class variable so no need to write self.subject
        print(f"Hi I am {self.name} and I teach {subject}")

    def update_followers(self,followers):
        self.followers += followers
        print(f"You have {self.followers} followers.")
student1 = Student("John", 20)
student1.display("python")
student1.update_followers(100)
