# The word Polymorphism is a combination of two Greek words, Poly meaning many and Morph meaning forms.
# In programming, polymorphism refers to the same object exhibiting different forms and behaviors.

# For example, take the Shape Class. The exact shape you choose can be anything. It can be a rectangle, a circle, a polygon, or a diamond.
# While, these are all shapes, their properties are different. This is called polymorphism.

# Assume there is a parent class named Shape from which the child classes Rectangle, Circle, Polygon, and Diamond are derived.
#
# Suppose your application will need methods to calculate the area of each specific shape.
# The area for each shape is calculated differently, which is why you can’t have a single implementation.
# You could throw in separate methods in each class (for instance, getSquareArea(), getCircleArea() etc.). But this makes it harder to remember each method’s name.

# Make things simpler with polymorphism. It would be better if all specific area calculation methods could be called getArea().
# You would only have to remember one method name and when you call that method, the method specific to that object would be called.
# This can be achieved in object-oriented programming using polymorphism. The base class declares a function without providing an implementation.
# Each derived class inherits the function declaration and can provide its own implementation

# Consider that the Shape class has a method called getArea(), which is inherited by all subclasses mentioned.
# With polymorphism, each subclass may have its own way of implementing the method.
# For example, when the getArea() method is called on an object of the Rectangle class, the method will respond by displaying the area of the rectangle.
# On the other hand, when the same method is called on an object of the Circle class, the circle’s area will be calculated and displayed on the screen.
class Rectangle():
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return self.width * self.height


class Circle():
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    def getArea(self):
        return self.radius * self.radius * 3.142


shapes = [Rectangle(6, 10), Circle(7)]
print("Sides of a rectangle are", str(shapes[0].sides))
print("Area of rectangle is:", str(shapes[0].getArea()))

print("Sides of a circle are", str(shapes[1].sides))
print("Area of circle is:", str(shapes[1].getArea()))
# Area print statements look identical, but different methods are called. Thus, we have achieved polymorphism.

