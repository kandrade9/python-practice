import math


def codestr(c):
    return (hex(ord(c)))

h = codestr('a')
print(h)  # '0x61'

# Defining a function is a procedural way of doing things. A more functional way would be to build a function to do the job for us, as shown below.
def compose(f, g):
    def fn(x):
        return f(g(x))
    return fn

codestr = compose(hex, ord)
h = codestr('a')  # fn('a') - hex(ord('a))
print(h)  # '0x61'

# generic function
def codestr(c):
    return(hex(ord(c)))

# equivalent functional code
codestr = compose(hex, ord)

# The code looks fairly similar, but the functional code demonstrates the intent much more clearly.
# The new function composes hex and ord; it says so right there! In the original code, that intent is expressed as a function that could be doing anything.
# You need to read the code to be sure. It might seem like a minor difference, but, with more complex code, the cognitive burden can add up.

# A related aspect is that, provided you trust compose, hex, and ord, the functional solution has to work. How could it not? It’s just three trusted functions doing what they do.
# With the original code, you have two trusted functions and a brand new function that, for all you know, could have a bug.
# Again, not very likely, but these things can add up in a more complex program.

# Another advantage is that we can use compose to create anonymous functions. For example, we can use map to apply our composed function to a string and produce a list of hex values.
# This saves us an ugly lambda expression. And function composition can be used to create anonymous functions
def compose(f, g):
    def fn(x):
        return f(g(x))
    return fn

s = 'xyz'
b = map(compose(hex, ord), s)  # map(fn, s)
print(list(b))  # ['0x78', '0x79', '0x7a']

print("#####################################")
# Finally, we can use our compose function to create other functions. Here is how we would create a function to calculate the square of the sine of x:
def compose(f, g):
    def fn(x):
        return f(g(x)) # lambda(math.sin(2))
    return fn

b = compose(lambda x: x*x, math.sin)
print(b(2))  # fn(2)

