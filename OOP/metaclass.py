# Classes are used to make objects. However, a class itself is an object and, just like any other object, it’s an instance of something: a metaclass
# A metaclass is the class of a class; it defines how a class behaves.

# Hence, if we want to modify the behavior of classes, we will need to write our own custom metaclass.
# The default metaclass is type. This means that just like an object is of the type class, a class itself is of the type, type.

# Object is an instance of a class and a class is an instance of a metaclass
class Foobar:
  pass

foo = Foobar()
print(type(foo))
print(type(Foobar))  # prints 'type'

print('#####################')
class Meta(type):
    # overriding the new method of the metaclass
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)

        # defining that each class with this metaclass should have a variable, x with a default value
        x.attr = 100
        return x

# defining a class with Meta as its metaclass instead of type
# by default, every class has 'type' set as its metaclass
class Foo(metaclass=Meta):
    pass

# printing the variables in our newly defined class
print(Foo.attr)

# Metaclasses propagate down the inheritance hierarchies, allowing all subclasses to inherit their attributes and methods.
# This property is particularly useful if we want our classes to have specific attributes, automatically, at the time of their creation.

