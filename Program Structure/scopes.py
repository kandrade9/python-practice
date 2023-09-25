# NONLOCAL SCOPE
# The nonlocal keyword adds a scope override to the inner scope, see below:
def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer
c = counter()

print(c)
print(c())
print(c())
print(c())

# This type of function is known as a closure, it's basically a block of code that “closes” nonlocal variables.
# The idea behind a closure is that we can reference variables that are defined outside our function.
# Basically nonlocal will allow us to assign to variables in an outer scope, but not in a global scope.
# So we can’t use nonlocal in our counter function because then it would try to assign to a global scope.
# Give it a try & we will quickly get a SyntaxError. Instead we must use nonlocal in a nested function.

# GLOBAL SCOPE
# The global statement declares a variable as being available for the code block following the statement
