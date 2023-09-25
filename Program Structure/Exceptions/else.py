# The else will only run if there are no errors raised
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["a"]
    print(value)
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")

print('#############################')

my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")
finally:
    print("The finally statement ran!")

# good usage of the else statement is where you want to execute a second piece of code that can also raise an error.
# if an error is raised in the else, then it won’t get caught though.
