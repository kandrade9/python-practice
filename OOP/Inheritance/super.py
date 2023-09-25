# The use of super() comes into play when we implement inheritance. It is used in a child class to refer to the parent class without explicitly naming it.
# It makes the code more manageable, and there is no need to know the name of the parent class to access its attributes.
class Vehicle:
    fuelCap = 90

class Car(Vehicle):
    fuelCap = 50

    def display(self):
        print("Fuel cap from the Vehicle Class:", super().fuelCap)
        print("Fuel cap from the Car Class:", self.fuelCap)


obj1 = Car()
obj1.display()
print("##################################")

class Vehicle:
    def display(self):
        print("I am from the Vehicle Class")

class Car(Vehicle):
    def display(self):
        super().display()
        print("I am from the Car Class")

obj1 = Car()
obj1.display()
print('###################################')

class ParentClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b


class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        self.c = c
        super().__init__(a, b)


obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
