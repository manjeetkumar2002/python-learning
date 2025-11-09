class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount
        print("Amount withdrawn successfully")
        print("current balance is",self.balance)
    def deposit(self,amount):
        if amount < 0:
            print("Invalid amount")
        self.balance += amount
        print("Amount deposited successfully")
        print("current balance is",self.balance)
    def show(self):
        print("Your name is : ",self.name)
        print("Your balance is :",self.balance)
    def change_name(self,new_name):
        self.name = new_name
    def get_balance(self):
        return self.balance
    def get_name(self):
        return self.name
    def __str__(self):
        return f"Your name is {self.name}\nYour balance is {self.balance}"

acc1 = BankAccount("John",100)
acc1.deposit(100)
acc1.withdraw(50)
print(acc1)
acc1.change_name("jenny")
print(acc1)
acc1.withdraw(1000)
print(acc1)
