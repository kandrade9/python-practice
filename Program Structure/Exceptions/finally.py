# Most of the time when an exception occurs, you will need to alert the user by printing to the screen or logging the message.
# Depending on the severity of the error, you may need to exit your program. Sometimes you will need to clean up before you exit the program.
# For example, if you have opened a database connection, you will want to close it before you exit your program or you may end up leaving connections open.
# Another example is closing a file handle that you have been writing to. We also need to learn how to clean up after ourselves.
# This is facilitated with the finally statement.
my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["d"]
except KeyError:
    print("A KeyError occurred!")
finally:
    print("The finally statement has executed!")




