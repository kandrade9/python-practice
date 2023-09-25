# ASSOCIATION
# In object-oriented programming, association is the common term for both the has-a and part-of relationships but is not limited to these.
# Two objects are in an association relationship is a generic statement, which means that we don’t worry about the lifetime dependency between the objects

# HAS A
# Class A and class B have a has-a relationship if one or both need the other’s object to perform an operation, but both class objects can exist independently of each other
# This implies that a class has a reference to an object of the other class but does not decide the lifetime of the other class’s referenced object

# AGGREGATION
# In aggregation, the lifetime of the owned object does not depend on the lifetime of the owner
# The parent object can get deleted but the owned object can continue to exist in the program
# In aggregation, the parent only contains a reference to the child, which removes the child’s dependency

class Country:
    def __init__(self, name=None, population=0):
        self.name = name
        self.population = population

    def printDetails(self):
        print("Country Name:", self.name)
        print("Country Population", self.population)


class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def printDetails(self):
        print("Person Name:", self.name)
        self.country.printDetails()


c = Country("Wales", 1500)
p = Person("Joe", c)  # the reference to the Country object gets passed in
p.printDetails()

# deletes the object
del p
print("")
c.printDetails()
# The Country object c lives on even after we delete the Person object p.
# This creates a weaker relationship between the two classes.


