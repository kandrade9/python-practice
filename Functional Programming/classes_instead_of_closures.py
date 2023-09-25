# __call__ is one of the special methods that Python provides to allow user-defined objects to support Python operators.
# All the methods have two underscores before and after their names to distinguish them from normal methods.
# For that reason, they are sometimes called “dunder” methods (double underscore), or, alternatively, magic methods. The __call__ method supports function calling.

# The example code is shown below. We modify the class called Format, to include a __call__ method instead of the previous format method.
# Now we create an object, format3, as before. But, this time, in order to invoke it, we just need to use the same syntax as we would use to call a function
class Format:
    def __init__(self, precision):
        self.p = precision

    def __call__(self, x):
        return '{:.{prec}f}'.format(x, prec=self.p)

format3 = Format(3)
print(format3(1.2345678))

print(Format(5)(1.2345678))
# Notice that format3 is not a function object; it is a Format object. But because it supports __call__, we can use function notation to call it.
# And, of course, we can still create an object like Format(5) and call it directly.
# Now our object can be used in a very similar way to the closure.
# It’s not usually worth doing, though, because defining a simple class is more of a hassle than defining a simple closure.

# Prefer classes for complex initialization requirements
class Format():

  def __init__(self):
    self.p = 0
    self.w = 0

  def prec(self, n):
    self.p = n
    return self

  def width(self, n):
    self.w = n
    return self

  def __call__(self, x):
    return '{:{width}.{prec}f}'.format(x, width=self.w, prec=self.p)

format3 = Format().width(10).prec(3)
print(type(format3))
print(format3)

print(format3(1.2345678))  # Format(1.2345678)
# In this class example, the instance variable that are initialized are eventually getting manipulated by the other function within the Format class


