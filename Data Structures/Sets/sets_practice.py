# Set
# A set is an unordered collection of data items
# Mutable data doctors like lists or dictionary, can't be added to a set however, adding a double is perfectly fine.
# It's perfect when we simply need to keep track of the existence of items, it doesn't allow duplicates, which means that we can convert another data structure to a set to remove any duplicates.
random_set = {"Educative", 1408, 3.142, (True, False), 1408}
print(random_set)
print(len(random_set))

# Set constructor
empty_set = set()
print(empty_set)
random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)

# Adding Elements
empty_set.add(1)  # when adding a single item, just use add method
print(empty_set)

empty_set.update([2, 3, 4, (2.3 ,"hi"), 5, 6])  # when appending multiple elements, use update
print(empty_set)

# Deleting elements
# The remove() method generates an error if the item is not found, unlike the discard() method.
random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)

random_set.discard(1408)
print(random_set)

random_set.remove((True, False))
print(random_set)

# Union
# A union of two sets is the collection of all unique elements from both sets
# It's on unique be performed using either the pipe operator '|' or the union() constructor method
set_A = {1, 2, 3, 4, 'a'}
set_B = {'a', 'b', 'c', 'd'}

print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))

# Intersection
# Section of two sets is a collection of unique elements, which are common between them
# In Python, intersection can be performed using either the & operator or the intersection() method:
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}

print(set_A & set_B)
print(set_A.intersection(set_B))
print(set_B.intersection(set_A))

# Difference
# In Python, the difference between two sets can be found using either the - operator or the difference() method.
# Do keep in mind that the difference operation is not associative, i.e., the positions of the sets matter.
# set_A - set_B returns the elements which are only present in set_A.
# set_B - set_A would do the opposite
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}


print(set_A - set_B)
print(set_A.difference(set_B))

print(set_B - set_A)
print(set_B.difference(set_A))

