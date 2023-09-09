# Lambdas are very useful for when we need functions as arguments. Below we have a simple function using functions as arguments then how it can be simplified using a lambda function.
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function
result = calculator(multiply, 10, 20)
print(result)

# LAMBDA APPROACH
# Leveraging functions as arguments and single-line function
def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function

multiplication = lambda n1, n2: n1 * n2
result = calculator(multiplication, 10, 20)
print(result)

addition = lambda n1, n2: n1 + n2
sum_result = calculator(addition, 10, 20)
print(sum_result)
# The code looks much shorter now! We can define the operation on the go whenever we want.
# This is the beauty of lambdas. They work really well as arguments for other functions.
