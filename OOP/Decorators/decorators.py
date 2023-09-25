# A decorator in Python is a function that accepts another function as an argument.
# The decorator will usually modify or enhance the function it accepted and return the modified function.
# This means that when you call a decorated function, you will get a function that may be a little different that may have additional features compared with the base definition.
# def another_function(func):
#     """A function that accepts another function"""
#     def other_func():
#         val = "The result of %s is %s" % (func(), eval(func()))
#         return val
#
#     return other_func
#
# def a_function():
#     """A pretty useless function"""
#     return "1+1"
#
# if __name__ == "__main__":
#     value = a_function()
#     print(value)
#
#     decorator = another_function(a_function)
#     print(decorator())

# We create one function and then pass it into a second function. The second function is the decorator function.
# The decorator will modify or enhance the function that was passed to it and return the modification.
def another_function(func):
    """A function that accepts another function"""
    def other_func():
        val = "The result of %s is %s" % (func(), eval(func()))
        return val
    return other_func

@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"

if __name__ == "__main__":
    value = a_function()
    print(value)
# A decorator starts with the @ symbol followed by the name of the function that we will be using to “decorate” our regular with

