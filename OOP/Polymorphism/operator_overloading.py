# Operators in Python can be overloaded to operate in a certain user-defined way.
# Whenever an operator is used in Python, its corresponding method is invoked to perform its predefined function.
# For example, when the + operator is called, it invokes the special function, __add__, in Python, but this operator acts differently for different data types.
# For example, the + operator adds the numbers when it is used between two int data types and merges two strings when it is used between string data types.

# We are going to implement a class that represents a complex number.“ A complex number consists of a real part and an imaginary part.
# When we add a complex number, the real part is added to the real part, and the imaginary part is added to the imaginary part.

# Example:
# a=3+7i  <--  a is considered a complex number
# b=2+5i  <--  a is considered a complex number
# a+b=(3+2)+(7+5)i=5+12i
class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imaginary = imag

    def __add__(self, other):  # overloading the `+` operator
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        temp = Complex(r, i)
        return temp

    def __sub__(self, other):  # overloading the `-` operator
        temp = Complex(self.real - other.real, self.imaginary - other.imaginary)
        return temp


obj1 = Complex(3, 7)
obj2 = Complex(2, 5)

obj3 = obj1.__add__(obj2)  # without using the '+' this is what is happening
obj4 = obj1 - obj2

print("real of obj3:", obj3.real)
print("imag of obj3:", obj3.imaginary)
print("real of obj4:", obj4.real)
print("imag of obj4:", obj4.imaginary)

# You can name the second argument anything, but as per convention, we will be using the word other to reference the other object.

