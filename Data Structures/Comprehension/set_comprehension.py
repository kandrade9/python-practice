# Set comprehensions are created similar to dictionary comprehension
# Remember sets can't have repeated elements
print("Creating a normal set: ")
my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
my_set = set(my_list)
print(my_set)
# {1, 2, 3, 4, 5, 7, 8}

# Rewriting the code above using set comprehension
print("Rewritten with set comprehension: ")
my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
my_set = {x for x in my_list}
print(my_set)
# {1, 2, 3, 4, 5, 7, 8}

# To create a set comprehension, we basically changed the square brackets that a list comprehension uses to the curly braces that the dictionary comprehension has.
