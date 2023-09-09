# Shallow copy constructs a new object and then inserts references into it to the objects found in the original (to the extent possible).
# A deep copy constructs a new object and then, recursively, inserts copies into it of the objects found in the original.

# DEEP copies are more independent of their originals than shallow copies are.

# The choice between shallow and deep copying depends on your specific needs. If you want to create an independent copy of an object, including all nested objects, use deep copy.
# If you want a new container but don't need completely independent copies of the inner objects, use shallow copy.
# Deep copies tend to be less memory efficient than shallow ones.

import copy

print("----- SHALLOW -----")
grades = [["Mary", "A+"], ["Don", "C-"]]
grades3 = copy.copy(grades) # shallow copy
grades3[1][1] = "D+" # original nested object will be modified

print(grades)
print(grades3)

print("----- DEEP -----")
grades = [["Mary", "A+"], ["Don", "C-"]]
grades3 = copy.deepcopy(grades) # deep copy
grades3[1][1] = "D+" # original nested object will NOT be modified

print(grades)
print(grades3)