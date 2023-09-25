# map - accepts a function object and a sequence (e.g., a list). It applies the function to each element of the list
a = [2.2, 5.6, 1.9, 0.1]
b = map(round, a)
print(type(b))
print(list(b))
# Note that map uses lazy iteration, so we will use the list function to turn the result into a list that we can print

# Using lambda anonymous function
a = [1, 3, 0, 6]
b = map(lambda x: x + 1, a)
print(list(b)) # [2, 4, 1, 7]
print("##################################")
# We can use a closure to create an anonymous function, instead of a lambda
def addn(n):
    def add(x):
        return x + n
    return add

a = [1, 3, 0, 6]
b = map(addn(1), a)  # this is essentially map(add, a) and every value in a will be the argument x when calling add
print(type(b))
print(list(b))  # [2, 4, 1, 7]
# This involves more code than just using a lambda because the closure has to be defined, but it has several advantages:
# If you need to use the function in more than one place, it might be better to define a closure.
# The closure allows you to create a family of related anonymous functions; for example, addn(2) creates a function that adds 2 to its arguments.
# The function inside a closure can be as complex as you like, whereas a lambda is limited to a single expression. If you need a complex function, a closure is a good choice.

