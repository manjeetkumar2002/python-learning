class A:
    def display(self):
        print("Display from class A")

class B(A):
    pass
    # def display(self):
    #     print("Display from class B")
class C(A):
    pass
    # def display(self):
    #     print("Display from class C")

class D(B,C):
    pass
    # def display(self):
        # print("Display from class D")


D1 = D()
D1.display()
print(D.mro()) #[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.__mro__) #(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)