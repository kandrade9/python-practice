# Dictionary comprehension is similar to a list comprehension in the way that they are organized
# print({i: str(i) for i in range(5)})
# {0: '0', 1: '1', 2: '2', 3: '3', 4: '4'}
# Thi is a straightforward comprehension. Basically it is creating an integer key and string value for each item in the range


# Using dictionary comprehension for swapping the dictionary's keys and values
my_dict = {1: "dog", 2: "cat", 3: "hamster"}
print({value:key for key, value in my_dict.items()})
# {'hamster': 3, 'dog': 1, 'cat': 2}

# This will only work if the dictionary values are of a non-mutable type, such as a string. Otherwise, you will end up causing an exception to be raised
# A dictionary comprehension can also be useful for creating a table out of class variables and their values.
