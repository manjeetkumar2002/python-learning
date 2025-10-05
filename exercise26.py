from math import pi
class Circle :
    radius = 0.0
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return round(pi * (self.radius ** 2),2)
    def circumference(self):
        return round(2 * pi * self.radius,2)

c1 = Circle(2)
area = c1.area()
circumference = c1.circumference()
print(f"area = {area}")
print(f"circumference = {circumference}")