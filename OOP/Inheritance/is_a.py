# Inheritance provides a way to create a new class from an existing class.
# The new class is a specialized version of the existing class such that it inherits all the non-private fields (variables) and methods of the existing class.
# The existing class is used as a starting point or as a base to create the new class.

# Wherever we come across an IS A relationship between objects, we can use inheritance.
# Car IS A Vehicle
# Python IS A Programming Language
# Square IS A Shape

# In Python, whenever we create a class, it is, by default, a subclass of the built-in Python object class.
# This makes it an excellent example of inheritance in Python.
# This class has very few properties and methods, but it does provide a strong basis for object-oriented programming in Python.

# Parent Class (Super Class or Base Class): This class allows the reuse of its public properties in another class.
# Child Class (Sub Class or Derived Class): This class inherits or extends the superclass.
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # calling the constructor from parent class
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors:", self.doors)


obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()


