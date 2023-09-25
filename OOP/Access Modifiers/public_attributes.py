# Public attributes are those that can be accessed inside the class and outside the class.
class Employee:
    name = 'Saul'
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.salary = salary

    def displayID(self):
        print("ID:", self.ID)
        print("Name:", self.name)

Steve = Employee(3789, 2500)
Steve.displayID()
print(Steve.salary)
