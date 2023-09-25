# Remember, list comprehension produces the entire list at a time but generator expression generates one item at a time. Generator expressions have lazy execution.
# For this reason, a generator expression is much more memory efficient technique than the equivalent list comprehension.
orig = [1, 2, 3]

listcomp = [n+1 for n in orig]  # Designing list comprehension out of list
generator = (n+1 for n in orig) # Designing generator expression out of list

print(listcomp)
print(generator)  # returns generator object
# print(list(generator))  # [1, 2, 3] - but after type casting to a list, the generator would no longer be a generator object and have access to its methods as it's become a list

# Because of lazy execution, you would only be able to traverse the generator object once completely, so either for loop of __next__
# for n in generator:
#     print(n)

print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
# print(generator.__next__()) # Throws error as no item is left
# Once we run out of the items, the code throws an error: StopIteration
print('#####################')
for x in (n*2 for n in range(1, 11)): # In-line generator exp.
    print(x)

    