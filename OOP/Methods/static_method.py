# Static methods are methods that are usually limited to class only and not their objects. They have no direct relation to class variables or instance variables and cannot modify class attributes.
# They are used as utility functions inside the class or when we do not want the inherited classes to modify a method definition.
class Player:
    teamName = 'Liverpool'  # class variables
    def __init__(self, name):
        self.name = name  # creating instance variables

    @staticmethod
    def demo():  # static methods do not take a self or cls argument
        # print(self.name)  # this would cause an error bc a static method has no relation w the class variables or state and so doesn't even know what self means
        print("I am a static method.")

p1 = Player('lol')
p1.demo()  # method accessed through object
Player.demo()  # method accessed through class

# The purpose of a static method is to use its parameters and produce a useful result.
class BodyInfo:
    @staticmethod
    def bmi(weight, height):
        return weight / (height ** 2)

weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))