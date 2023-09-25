# If your code is raising an exception, we can now wrap it in such a way that you can catch the error and exit gracefully or continue without interruption.
try:
    1 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")

# Bare except - not recommended
try:
    1 / 0
except:
    print("You cannot divide by zero!")

print("######################################")
# Good example
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except KeyError:
    print("That key does not exist!")

my_list = [1, 2, 3, 4, 5]
try:
    my_list[6]
except IndexError:
    print("That index is not in the list!")

print("######################################")
my_dict = {"a":1, "b":2, "c":3}
try:
    value = 1/0
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other error occurred!")

print("######################################")
my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["d"]
except (IndexError, KeyError):
    print("An IndexError or KeyError occurred!")