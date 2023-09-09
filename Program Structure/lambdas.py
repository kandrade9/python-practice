# A lambda is an anonymous function that returns some form of data - a special class of functions for which we do not need to specify function names
# format --> lambda parameters : expression
triple = lambda num: num * 3  # Assigning the lambda to a variable
print(triple(10))  # Calling the lambda and giving it a parameter, variable name essentially being the function or lambda name

concat_strings = lambda a, b, c: a[0] + b[0] + c[0]
print(concat_strings("World", "Wide", "Web"))

# Lambdas are simpler and more readable than normal functions. But this simplicity comes with a limitation.
# A lambda cannot have a multi-line expression. This means that our expression needs to be something that can be written in a single line.
# Hence, lambdas are perfect for short, single-line functions.

# Conditionals in Lambdas
my_func = lambda num: "High" if num > 50 else "Low"
print(my_func(60))
# When using conditional statements in lambdas, the if-else pair is necessary. Both cases need to be covered, otherwise, the lambda will throw an error


