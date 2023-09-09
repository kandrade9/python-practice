# filter() - filters elements from a list if the elements satisfy the condition that is specified in the argument function; requires a function and a list.
numList = [30, 2, -15, 17, 9, 100]

lambda_arg = lambda n: n > 10
greater_than_10 = filter(lambda_arg, numList)
print(greater_than_10)
print(list(greater_than_10))

