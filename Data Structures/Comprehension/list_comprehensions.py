# List comprehensions provide an alternative that is more declarative than a loop and often clearer than using a map function


# EXAMPLE 1: Create a list of length 24, filled with the strings, '0’ to ‘24’

# USING A FOR LOOP - this solution is the most verbose (wordy) and the least declarative
# It is a loop that just happens to be building up a list according to a simple pattern. But since it is a loop, it could be doing anything
# The code is in an imperative style, meaning it doesn’t just tell Python what sort of list you need, it tells Python exactly how to create that list
# Imperative code is more flexible, but that can be a disadvantage when you only need to do something simple and boring
# You have to double-check the code to make sure it isn’t doing something more complicated than you think

a = []
for i in range(24):
    a.append(str(i))
print(a)
print("####################\n")

# USING MAP()
# The map case is more declarative in style. It says that you want to map the str function onto the numbers, 0 to 24 and make a list out of the result
# These are all standard Python functions, applied in a standard way. In this particular case, there isn’t much to fault this solution
a = list(map(str, range(24)))
print(a)
print("####################\n")

# USING LIST COMPREHENSION
#  List comprehensions exist for the specific purpose of creating a list from another iterable, so when you see that syntax, you know exactly what the code is doing
a = [str(i) for i in range(24)]
print(a)

# We can read the code above like an English sentence: make a list of str(i) for all values of i in range(24)

# EXAMPLE 2: Take a list of numbers and create a new list, where the numbers have been rounded to the nearest 5

# USING A FOR LOOP
k = [12, 33, 49, 57]
a = []
for x in k:
    a.append(round(x/5)*5)
print(a)
print("####################\n")

# USING MAP()
k = [12, 33, 49, 57]
a = list(map(lambda x: round(x/5)*5, k))
print(a)

# USING LIST COMPREHENSION
k = [12, 33, 49, 57]
a = [round(x/5)*5 for x in k]
print(a)

# In this case, the list comprehension benefits from not having to use a lambda function, which makes it marginally less complex



