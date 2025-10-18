# we use abc module
from abc import ABC,abstractmethod
# ABC is a class from abc module
# if you want to make vehicle class abstract inherit ABC class

class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyre = n
    # now start method is abstract method
    @abstractmethod
    def start(self):
        pass
    def display(self):
        print(self.no_of_tyre)

class Bike(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("Bike start with kick")

class Scooty(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("Scooty start with self")

class Car(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("Car start with key")

#v = Vehicle(10) #TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract method 'start'

bike = Bike(2)
bike.display()
bike.start()

car = Car(4)
car.display()
car.start()
