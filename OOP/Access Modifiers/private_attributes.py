# Private attributes cannot be accessed directly from outside the class but can be accessed from inside the class.

# The aim is to keep it hidden from the users and other classes.
# Unlike in many languages, it is not a widespread practice in Python to keep the data members private since we do not want to create hindrances for the users.
class Employee:
    def __init__(self, salary):
        self.__salary = salary  # salary is a private property
    def get_salary(self):
        return self.__salary

Steve = Employee(2500)
print(Steve.get_salary())
# print("Salary:", Steve.__salary)  # this will cause an error
# To ensure that no one from the outside knows about this private property, the error does not reveal its identity.