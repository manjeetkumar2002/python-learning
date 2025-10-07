# multiple inheritance : in this a class have multiple parents

class Human:
    def __init__(self,num_heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")

class Male:
    def __init__(self,name):
        self.name = name
    def flirt(self):
        print("i can flirt")
    def work(self):
        print("i can code")

class Boy(Human, Male):
    def __init__(self,name,language,num_heart):
        Human.__init__(self,num_heart)
        Male.__init__(self,name)
    def work(self):
        print("i can cook")

boy1 = Boy("manjeet","python",2)
boy1.eat()
boy1.flirt()
boy1.work() # Human class method is called , this order is matter (human,male)

# solution of it
# method1 change the order (Male,Human) , but this is not the best method
# method2
Male.work(boy1)

Boy.work(boy1)

boy1.work()
Human.work(boy1)
# method resolution order agar tino class me same methods h ex work
# Agar ham boy object se call karte h pahle boy class me check hoga method nhi h present then  ye order wise (human,male) class me check hoga pahle human then male
print(Boy.mro())
# This is order [<class '__main__.Boy'>, <class '__main__.Human'>, <class '__main__.Male'>, <class 'object'>]


print(boy1.num_eyes)
#print(boy1.name) AttributeError: 'Boy' object has no attribute 'name'
# problem : which init function will call , confusion , follow the same mro order , boy have no init function , it call the human init
# if you want to call male init function , write this in boy
# def __init__(self, name):
#     Male.__init__(self, name)
print(boy1.name)
#print(boy1.num_eyes) now this statement gives error , call human init also in boy init