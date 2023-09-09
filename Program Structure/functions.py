# Keyword Arguments
def keyword_function(a=1, b=2):
    return a+b
result = keyword_function(a=4, b=5)
print(result)
result = keyword_function()
print(result)

def mixed_positional_and_kw(a, b=2, c=3):
    return a+b+c
result = mixed_positional_and_kw(1, b=4, c=5)
print(result)

# ARGS & KWARGS
# functions can accept any number of arguments or keyword arguments
# args and kwargs are arbitrary, they could be called anything as long as they have the appropriate asterisks
def many(*ted, **kwargs):
    print(ted)
    print(kwargs)

many(1, 2, 3, "kev", 1.9, name="Mike", job="programmer")

# FUNCTION SCOPE
# When mutable data is passed to a function, the function can modify or alter it. These modifications will stay in effect outside the function scope as well. An example of mutable data is a list.
# In the case of immutable data, the function can modify it, but the data will remain unchanged outside the function’s scope. Examples of immutable data are numbers, strings, etc.
num = 20
def multiply_by_10(n):
    n *= 10
    num = n  # Changing the value inside the function
    print("Value of num inside function:", num)
    return n
multiply_by_10(num)
print("Value of num outside function:", num)  # The original value remains unchanged

# Function scope exercise
num_list = [10, 20, 30, 40]
print(num_list)
def multiply_by_10(my_list):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10
multiply_by_10(num_list)
print(num_list)  # The contents of the list have been changed

# Immutable objects are unaffected by the working of a function.
# If we really need to update immutable variables through a function, we can simply assign the returning value from the function to the variable.
n = 9
m = n
m += 1
print(n)
print(m)

# String Functions
random_string = "This is a string"
print(random_string.find("is"))  # First instance of 'is' occurs at index 2
print(random_string.find("is", 9, 13))  # No instance of 'is' in this range

# Replace
a_string = "Welcome to In-n-Out!"
new_string = a_string.replace("Welcome to", "Greetings from")
print(a_string)
print(new_string)

# Join
llist = ['a', 'b', 'c']
print('>>'.join(llist))  # joining strings with >>
print('<<'.join(llist))  # joining strings with <<
print(', '.join(llist))  # joining strings with comma and space

# Format
string1 = "Learn Python {} at {cname}".format(3, cname="Educative")
string2 = "Learn Python {0} at {1}".format(3, "Educative")
string3 = "Learn Python {} at {}".format(3, "Educative")
print(string1)
print(string2)
print(string3)
# The placeholders can be identified using named indexes {cname}, numbered indexes {0}, or even empty placeholders {}.

# Type Conversion or Casting
print(int("12") * 10)  # String to integer
print(int(20.5))  # Float to integer
print(int(False))  # Bool to integer
# print (int("Hello")) # This wouldn't work!

# ord() - convert char to unicode val
print(ord('a'))
print(ord('0'))

# float()
print(float(24))
print(float('24.5'))
print(float(True))

# bool()
# Strings are always converted to True, except if the string is empty
print(bool(10))
print(bool(0.0))
print(bool("Hello"))
print(bool(""))