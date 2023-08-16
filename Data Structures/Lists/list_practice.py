# string slicing
my_string = "This is MY string"
print(my_string[0:7:2])  # string[start: end: step]
print(my_string[7:0:-1])
print(my_string[-2])  # reverse slicing
print(my_string[:8])  # all the characters before M
print(my_string[::-1])  # the whole string in reverse

### LISTS ###
jon_snow = ["Jon Snow", "Winterfell", 30]
print(jon_snow[0])  # index
print(len(jon_snow))  # length
jon_snow[2] += 3
print(jon_snow[2])  # lists are mutable and are not bound to one type of data

num_seq = range(0, 10)  # a sequence from 0 to 9
num_list = list(num_seq)  # list casts the sequence into a list
print(num_list)

num_seq = range(3, 20, 3)  # a sequence from 3 to 19 with a step of 3
print(list(num_seq))

### 2D Lists ###
world_cup_winners = [[2006, "Italy"], [2010, "Spain"], [2014, "Germany"], [2018, "France"]]
print(world_cup_winners[1])
print(world_cup_winners[1][1])  # Accessing 'Spain'
print(world_cup_winners[1][1][0])  # Accessing 'S'

# Merging lists
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
merged_list = part_A + part_B
print(merged_list)

# OR Extend
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)

# Append
num_list = []
num_list.append(1)
num_list.append(2)
print(num_list)

# Insert
num_list = [1, 2, 3, 5, 6]
num_list.insert(3, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
print(num_list)

# Pop
num_list.pop()  # Removes last element in list

# Remove
num_list.pop()  # Removes last element in list
num_list.remove(1)  # Removes element specified

# List slicing
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5])
print(num_list[0::2])

print(num_list.index(4))  # searches index of element

print(2 in num_list)
print(19 in num_list)
print(10 not in num_list)

# Sort
num_list = [20, 40, 10, 50.4, 30, 100, 5]
num_list.sort()
print(num_list)

# List comprehension a technique that uses a for loop and a condition to create a new list from an existing one
# [expression for loop if condition]
# The expression is an operation used to create elements in the new list.
# The for loop will iterate an existing list. The iterator will be used in the expression.
# New elements will only be added to the new list when the if condition is fulfilled. This component is optional.

# creating a new list whose values are the doubles of an existing list
nums = [10, 20, 30, 40, 50]
nums_double = []
for n in nums:
    nums_double.append(n * 2)
print(nums)
print(nums_double)

# List comprehension approach to doubling values in nums list if element divisible by 4 (condition necessary in list comprehensions)
comprehension_nums_double = [n * 2 for n in nums if n % 4 == 0]
print(nums)
print(comprehension_nums_double)

# list comprehension using multiple lists
list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]
sum_list = [[n1, n2] for n1 in list1 for n2 in list2 if n1 + n2 > 100]
print(sum_list)
