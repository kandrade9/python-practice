# If the user believes it is absolutely necessary to access a private property or a method, they can access it using the _<ClassName> prefix for the property or method
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

Steve = Employee(3789, 2500)
print(Steve._Employee__salary)  # accessing a private property