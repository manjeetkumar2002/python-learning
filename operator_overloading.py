# Example 1
class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i
    def __add__(self,other):
        result = ComplexNumber(0,0)
        result.real = self.real + other.real
        result.imaginary = self.imaginary + other.imaginary
        return result

c1 = ComplexNumber(2,3)
c2 = ComplexNumber(4,5)
c3 = c1 + c2
print(c3.real,c3.imaginary)


# Example 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

p1 = Person("John", 90)
p2 = Person("John", 60)

if p1 > p2:
    print("p1 is greater than p2")
else:
    print("p2 is greater than p1")