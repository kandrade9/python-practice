# Information hiding refers to the concept of hiding the inner workings of a class.
# And simply providing an interface through which the outside world can interact with the class without knowing what’s going on inside.

# Data hiding can be divided into two primary components: Encapsulation & Abstraction (2 of the 4 principle of oop)

# Encapsulation in OOP refers to binding data and the methods to manipulate that data together in a single unit, that is, encapsulation is basically just a class.
# When encapsulating classes, a good convention is to declare all variables of a class private. This will restrict direct access by the code outside that class.

# Advantages of encapsulation:
# Classes make the code easy to change and maintain.
# Properties to be hidden can be specified easily.
# We decide which outside classes or functions can access the class properties.

# Getters / Setters
class User:
    def __init__(self, username=None):  # defining initializer
        self.__username = username

    def setUsername(self, x):
        self.__username = x

    def getUsername(self):
        return self.__username


Steve = User('steve1')
print('Before setting:', Steve.getUsername())
Steve.setUsername('steve2')
print('After setting:', Steve.getUsername())
