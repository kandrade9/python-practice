# This allows you to turn a class method into a class attribute
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property  # This allows you to turn a class method into a class attribute
    def full_name(self):
        """Return the full name"""
        return "%s %s" % (self.first_name, self.last_name)

person = Person("Mike", "Driscoll")
print(person.full_name)
print(person.first_name)
# person.full_name = "Jackalope"  # while the decorator makes the method full_name a property, you cannot set the property using full_name since it's not an instance variable
                                  # you will only be able to change the full_name property by manipulating the first and last name instance variables
                                  # so full_name can only be changed indirectly
person.first_name = "Dan"
print(person.full_name)
