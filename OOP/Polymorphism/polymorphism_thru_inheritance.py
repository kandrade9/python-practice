# What if we want our derived class to inherit a method from the base class and have a different implementation for it?
# That is when polymorphism, a fundamental concept in the OOP paradigm, comes into play.

# Consider the example of a Shape class, which is the base class while many shapes like Rectangle and Circle extending from the base class are derived classes.
# These derived classes inherit the getArea() method and provide a shape-specific implementation, which calculates its area.

# Polymorphism: having specialized implementations of the same methods for each class.
class Shape:
    def __init__(self):
        self.sides = 0

    def getArea(self):
        pass

# Rectangle IS A Shape with a specific width and height
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return self.width * self.height

# Circle IS A Shape with a specific radius
class Circle(Shape):  # derived form Shape class
    # initializer
    def __init__(self, radius):
        self.radius = radius
        super().__init__()
        
    # method to calculate Area
    def getArea(self):
        return self.radius * self.radius * 3.142

shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Area of circle is:", str(shapes[1].getArea()))

# The example above can also be considered method overriding

# Advantages and key features of method overriding:
# The derived classes can give their own specific implementations to inherited methods without modifying the parent class methods.
# For any method, a child class can use the implementation in the parent class or make its own implementation.
# Method overriding needs inheritance, and there should be at least one derived class to implement it.
# The methods in the derived classes usually have a dissimilar implementation.
