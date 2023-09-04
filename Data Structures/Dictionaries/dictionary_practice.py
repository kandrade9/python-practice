# A dictionary stores key-value pairs, where each unique key is an index which holds the value associated with it.
# Unlike Lists, Dictionaries are unordered because the entries are not stored in a linear structure.

# Create dictionary
empty_dict = {}  # Empty dictionary
phone_book = {"Batman": [468426, 34], "Cersei": 237734, "Ghostbusters": 44678}
print(phone_book)

# Alternatively, can create dictionary with its constructor dict()
phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# dict() constructor can also take an iterable
phone_book = dict([('Batman', 468426), ('Cersei', 237734), ('Ghostbusters', 44678)])
print(phone_book)
# Two keys can have the same value. However, it is crucial that all keys are unique

# Accessing values
print(phone_book["Cersei"])
print(phone_book.get("Ghostbusters"))

# Adding / Updating Entries
phone_book["Godzilla"] = 46394  # New entry
print(phone_book)

phone_book["Godzilla"] = 9000  # Updating entry
print(phone_book)

# Removing Entries
del phone_book["Batman"]
print(phone_book)
# If we want to use the deleted value, the pop() or popitem() methods would work better
cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)

lastAdded = phone_book.popitem()
print(lastAdded)

# Length
print(len(phone_book))

# Checking Key Existence
print("Batman" in phone_book)
print("Godzilla" in phone_book)

# Copying Contents
second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}
# Add second phone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)

# For Loop Approach
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
print(houses.items())
new_houses = {}
for n, house in houses.items():
    key = n**2
    value = house + "!"
    new_houses[key] = value
print(new_houses)

# Dictionary Comprehension
dict_comp = {n**2: house + "!" for (n, house) in houses.items()}
print(dict_comp)
