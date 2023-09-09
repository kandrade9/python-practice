# Leveraging range method to track index of elements as our iterator i
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
for i in range(0, len(float_list)):  # Iterator i traverses to the last index of the list
    float_list[i] = float_list[i] * 2
print(float_list)

# For loop example
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
count_greater = 0
for num in float_list:  # Iterator num traverses to the last index of the list
    if num > 10:
        count_greater += 1
print(count_greater)

# NESTED FOR LOOP
n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]
for n1 in num_list:
    for n2 in num_list:  # Now we have two iterators
        if (n1 != n2):
            if (n1 + n2 == n):
                print(n1, n2)

# BREAK KEYWORD
n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]
found = False  # This bool will become true once a pair is found

for n1 in num_list:
    for n2 in num_list:
        if (n1 != n2):
            if (n1 + n2 == n):
                found = True  # Set found to True
                break
    if found:
        print(n1, n2)
        break  # Break outer loop if a pair is found

# CONTINUE KEYWORD
num_list = list(range(0, 10))
for num in num_list:
    if num == 3 or num == 6 or num == 8:
        continue  # keyword that basically just skips the current iteration the iterator is on
    print(num)

# PASS KEYWORD
# Keyword to assist you when you haven’t written a piece of code but still need your entire program to execute
num_list = list(range(20))
for num in num_list:
    pass
print(len(num_list))

# WHILE LOOP
# A while loop is not always restricted to a fixed range. Its execution is based solely on the condition associated with it
n = 2  # Could be any number
power = 0
val = n
while val < 1000:
    power += 1
    val *= n
    print(power, val)
print(power)

# Sum first and last digit of any integer
n = 249
last = n % 10  # Finding the last digit
first = n  # Set it to `n` initially
while first >= 10:
    first //= 10  # Floor division assignment
    print(first)  # Keep dividing by 10 until the leftmost digit is reached
result = first + last
print(result)


# EXERCISES
# 1
def check_balance(brackets):  # The argument is a string
    opening = 0
    closing = 0
    for char in brackets:
        if char == "[":
            opening += 1
        elif char == "]":
            closing += 1
    if opening == closing:
        return True
    return False
print(check_balance('[[[[[[]]]]]]]]]]]][][][[][]['))


# 2
def check_sum(num_list):
    length = len(num_list)
    for first_num in range(length):
        for second_num in range(first_num + 1, length):
            if num_list[first_num] + num_list[second_num] == 0:
                return True
    return False
num_list = [10, -14, 26, 5, -3, 13, -5]
print(check_sum(num_list))

# 3 - Fibonacci Sequence w while loop
# Find nth value in the Fibonacci sequence
def fib(n):
    # The first and second values will always be fixed
    first = 0
    second = 1
    if n < 1:
        return -1
    if n == 1:
        return first
    if n == 2:
        return second

    count = 3  # Starting from 3 because we already know the first two values
    while count <= n:
        fib_n = first + second
        first = second
        second = fib_n
        count += 1  # Increment count in each iteration
    return fib_n
n = 7
print(fib(n))