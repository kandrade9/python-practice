# If we observe closely, there are several similarities between iteration and recursion. In recursion, a function performs the same set of operations repeatedly but with different arguments.
# A loop does the same thing except that the value of the iterator and other variables in the loop’s body change in each iteration.
# Recursion is useful when we need to divide data into different chunks. Iteration is useful for traversing data and also when we don’t want the program’s scope to change.

# Recursion is the process in which a function calls itself during its execution. Each recursive call takes the program one scope deeper into the function.
# The recursive calls stop at the base case. The base case is a check used to indicate that there should be no further recursion.

# Imagine recursive calls as nested boxes where each box represents a function call.
# Each call makes a new box. When the base case is reached, we start moving out of the boxes one by one
def rec_count(number):
    print(number)
    # Base case
    if number == 0:
        return 0
    rec_count(number - 1)  # A recursive call with a different argument
    print("see")
rec_count(3)

# Recursion can significantly reduce the runtime of certain algorithms, which makes the code more efficient

def fib(n):
    # The base cases
    if n <= 1:  # First number in the sequence
        return 0
    elif n == 2:  # Second number in the sequence
        return 1
    else:
        # Recursive call
        return fib(n - 1) + fib(n - 2)
print(fib(5))

# First, we handle our base cases. We know that the first two values are always 0 and 1, so that is where we can stop our recursive calls.
# If n is larger than 2, then it will be the sum of the two values before it.

