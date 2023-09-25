# Duck typing is useful as it simplifies the code and the user can implement the functions without worrying about the data type.
# But this may not be the case all the time. The user might not follow the instructions to implement the necessary steps for duck typing.
# To cater to this issue, Python introduced the concept of abstract base classes, or ABC.

# Abstract base classes define a set of methods and properties that a class must implement in order to be considered a duck-type instance of that class.
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

shape = Shape()
square = Square(4)

# Shape class should just provide a blueprint for its child classes to implement methods in it.
# To prevent the user from making a Shape class object, we use abstract base classes.

# To define an abstract base class, we use the abc module.
# The abstract base class is inherited from the built-in ABC class.
# We have to use the decorator @abstractmethod above the method that we want to declare as an abstract method.
from abc import ABC, abstractmethod

class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def hello(self):
        return 'Hello, world!'

class Square(Shape):
    def __init__(self, length):
        self.length = length

    # UNCOMMENT WHEN YOU WANT TO HAVE SUCCESSFUL COMPILE
    # def area(self):
    #     return (self.length * self.length)
    #
    # def perimeter(self):
    #     return (4 * self.length)
    #
    # def hello(self):
    #     return super().hello()

# shape = Shape()  # this code will NEVER compile since Shape has abstract methods without method definitions in it
# square = Square(4)  #this will code will not compile since abstract methods have not been defined in the child class, Square
# print(square.hello())

# We allow the user to have a free hand over the definition of the methods while also making sure that the methods are defined.
# Methods with @abstractmethod decorators must be defined in the child class.
# Abstract methods must be defined in child classes for proper implementation of inheritance.
