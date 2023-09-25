file = open('input.txt')  # opening and reading file
print(file)
data = file.read()  # reading entire file as single string
print(data)  # printing the contents of file
file.close()  # closing the file

print('-----------------------------------------')

# using with operator to write to file
with open('input.txt', 'w') as file:  # added the w mode in open
    file.write('Hey! New message got written right now')  # using write method to write to file

# using with operator to read the text file contents after writing
with open('input.txt', 'r') as file:
    data = file.read()
    print(data)