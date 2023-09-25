# Find the square root of every value in a list, but you want to ignore any negative values so that they don’t even appear in the output list
import math

k = [-1, 16, 9, -4, 0, 25]
a = []
for x in k:
    if x >= 0:
        a.append(math.sqrt(x))
print(a)
print("###################\n")
# The code above excludes negative numbers so the list returned is of 4 values

# USING MAP()
# Filter is used below to remove the negative values before we take the square root
# import math^
k = [-1, 16, 9, -4, 0, 25]
a = list(map(math.sqrt, filter(lambda x: x >= 0, k)))
print(a)
print("###################\n")

# LIST COMPREHENSION
k = [-1, 16, 9, -4, 0, 25]
a = [math.sqrt(x) for x in k if x >= 0]
print(a)
print("###################\n")
# We can read the code above like : we make a list of sqrt(X) for all values of x in k but only if x >= 0
