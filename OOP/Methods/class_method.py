# Class methods are accessed using the class name and can be accessed without creating a class object.
# To declare a method as a class method, we use the decorator @classmethod.
# cls is used to refer to the class just like self is used to refer to the object of the class.
class Player:
    teamName = 'Liverpool'  # class variables
    def __init__(self, name):
        self.name = name  # creating instance variables

    @classmethod
    def getTeamName(cls):
        return cls.teamName
print(Player.getTeamName())  # class method accessed directly through class, no need to initialize class object