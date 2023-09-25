# ASSOCIATION
# In object-oriented programming, association is the common term for both the has-a and part-of relationships but is not limited to these.
# Two objects are in an association relationship is a generic statement, which means that we don’t worry about the lifetime dependency between the objects

# PART OF
# In this relationship, one class object is a component of another class object
# An instance of the component class can only be created inside the main class.
# class B and class C have their own implementations, but their objects are only created once a class A object is created.
# Because of this, part of relationship is a dependent relationship. The existence of certain class objects are dependent on the existence of the owner

# COMPOSITION
# The practice of accessing other class objects in your class
# The class which creates the object of the other class is known as the owner and is responsible for the lifetime of that object


# Composition relationships are Part-of relationships where the part must constitute a segment of the whole object.
# We can achieve composition by adding smaller parts of other classes to make a complex unit

class Engine:
    def __init__(self, capacity=0):
        self.capacity = capacity

    def printDetails(self):
        print("Engine Details:", self.capacity)

class Tires:
    def __init__(self, tires=0):
        self.tires = tires

    def printDetails(self):
        print("Number of tires:", self.tires)

class Doors:
    def __init__(self, doors=0):
        self.doors = doors

    def printDetails(self):
        print("Number of doors:", self.doors)

class Car:
    def __init__(self, eng, tr, dr, color):
        self.eObj = Engine(eng)  # Once a Car object is initialized, it will also initialize the other dependent classes
        self.tObj = Tires(tr)
        self.dObj = Doors(dr)
        self.color = color

    def printDetails(self):
        self.eObj.printDetails()
        self.tObj.printDetails()
        self.dObj.printDetails()
        print("Car color:", self.color)


car = Car(1600, 4, 2, "Grey")
# del car.eObj # if we ran this line, the program would fail to compile
car.printDetails()

# Car class is responsible for their lifetime, i.e., when Car dies, so does tire, engine, and doors too

