def f(x, a, v):
    def g(e):
        print(x, a, v, e)
    return g

c = f(5, 6, 7)
c(2)  # g(2)

print(dir(c))  # provides a list of names of the attributes of a closure

# The variables that are passed into f are called free variables. In other words, variables that are used by f but not defined within f.
print(c.__code__.co_freevars)  # prints free variables of f

# get variable values
print(c.__closure__)
print(type(c.__closure__))
print(type(c.__closure__[0].cell_contents))
print(c.__closure__[0].cell_contents)
print(c.__closure__[1].cell_contents)
print(c.__closure__[2].cell_contents)

for i, name in enumerate(c.__code__.co_freevars):
    print(name+":", c.__closure__[i].cell_contents)

