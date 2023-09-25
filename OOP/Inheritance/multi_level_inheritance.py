# When a class is derived from a class which itself is derived from another class, it is called multilevel inheritance.
# We can extend the classes to as many levels as we want to.

# A Car IS A Vehicle
# A Hybrid IS A Car
class Vehicle:
    def setTopSpeed(self, speed):
        self.topSpeed = speed  # constructors aren't always necessary in classes
        print("Top speed is set to", self.topSpeed)

class Car(Vehicle):
    def openTrunk(self):
        print("Trunk is now open.")


class Hybrid(Car):
    def turnOnHybrid(self):
        print("Hybrid mode is now switched on.")


priusPrime = Hybrid()  # creating an object of the Hybrid class
priusPrime.setTopSpeed(220)  # accessing methods from the parent class
priusPrime.openTrunk()  # accessing method from the parent class
priusPrime.turnOnHybrid()  # accessing method from the child class

