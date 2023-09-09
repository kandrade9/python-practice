# map() - creates a map object using an existing list and a function as its parameters. This object can be converted to a list using the list() function
num_list = [0, 1, 2, 3, 4, 5]
double_list = map(lambda n: n * 2, num_list)
print(num_list)
print(double_list)
print(list(double_list))
# We could have created a function that doubles a number and used it as the argument in map(), but the lambda made things simpler.



