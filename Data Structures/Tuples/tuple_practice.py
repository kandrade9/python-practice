# Tuples - have very similar functionality as lists, except that this data structure is immutable
car = ("Ford", "Raptor", 2019, "Red")
print(car)

# Length
print(len(car))

# Indexing
print(car[1])

# Slicing
print(car[2:])

# Nested Tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)

# Search
print("Batman" in awesome_team)

# Index
print(awesome_team.index('Wonder Woman'))