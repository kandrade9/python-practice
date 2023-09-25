# Creating a 2D list -
print("Creating a 2D List using nested comprehensions: ")
a = [[x for x in range(3)] for y in range(4)]
print(a)
print("#####################\n")
# We know that [x for x in range(3)] gives [0, 1, 2]. So, we are really calculating [[0, 1, 2] for y in range(4)]
# Which, of course, evaluates to: [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
# We are simply creating an outer list of four elements, where each of those elements is a list of three elements


print("Creating a 2D list using nested comprehension but making the output element depend on x and y: ")
a = [[x + 10*y for x in range(3)] for y in range(4)]  # Here we are making the output element depend on x and y
print(a)
print("#####################\n")
# Above the inner array is going to be different every time. It will be equal to: [10*y, 1+10*y, 2+10*y], where y is the row number


# Below uses similar implementation as above, but instead we are creating a 2D list using a nested for loop, where the elements are dependent on loop counters
print("Creating a 2D list using for loops but making the output element depend on x and y: ")
b = []
for y in range(4):
    c = []
    for x in range(3):
        result = x + 10*y  # This is where we are making the output element depend on x and y
        c.append(result)
    b.append(c)
print(b)
print("#####################\n")


# Below we make use of a nested list comprehension in which the range of x depends on y
print("Creating a 2D list using nested comprehension but making the range of x depend on y: ")
a = [[x + 10*y for x in range(y)] for y in range(4)]
print(a)
print("#####################\n")


# Below uses similar implementation as above, but instead we are creating a 2D list using a nested for loop, where the elements are dependent on loop counters
print("Creating a 2D list using for loops but making the range of x depend on y: ")
b = []
for y in range(4):
    c = []
    for x in range(y):
        result = x + 10*y
        c.append(result)
    b.append(c)
print(b)
print("#####################\n")


# Creating a flat list
print("Creating a flat list using comprehension with two for loops: ")
a = [x + 10*y for x in range(3) for y in range(4)]
print(a)
print("#####################\n")
# We are only creating one flat list here rather than a list of lists (there is only one [] pair).
# But we are still looping over y from 0 to 3, and, for each y, we are looping over x from 0 to 2.


print("Creating a flat list using a nested for loop: ")
b = []
for x in range(3):
    for y in range(4):
        result = x + 10*y
        b.append(result)
print(b)
# The leftmost loop in the comprehension corresponds to the outer loop in the for loop version.
# This might seem to contradict the previous example, but in that example, we had two separate list comprehensions, one inside the other
