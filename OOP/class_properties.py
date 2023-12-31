# Implementation of a class with only properties/fields/class variables/attributes
class Employee:
    # defining the properties
    ID = None
    salary = None
    department = "hr"


# creating an object of the Employee class
Steve = Employee()

# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"

# creating a new attribute for Steve
Steve.title = "Manager"

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Title:", Steve.title)
