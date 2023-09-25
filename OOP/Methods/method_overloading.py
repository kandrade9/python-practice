# Overloading refers to making a method perform different operations based on the nature of its arguments.
# Below we see the same method behaving differently when encountering different types of inputs.
# Under the hood, overloading saves us memory in the system. Creating new methods is costlier compared to overloading a single one.
# Method Overloading plays a vital role in polymorphism
class Employee:
    # defining the properties and assigning them None
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    # method overloading
    def demo(self, a, d=5, e=None):
        print("a =", a)
        print("d =", d)
        print("e =", e)

    def tax(self, title=None):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)

Steve = Employee()

print("Demo 1")
Steve.demo(1)
print("\n")

print("Demo 2")
Steve.demo(1, 2)
print("\n")

print("Demo 3")
Steve.demo(1, 2, 3)

# ADVANTAGES
# Increases execution speed
# Makes code cleaner and readable
# Allows the implementation of polymorphism
# Same method name saves memory