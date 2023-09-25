# In hierarchical inheritance, more than one class extends, as per the requirement of the design, from the same base class.
# The common attributes of these child classes are implemented inside the base class.

# A Car IS A Vehicle
# A Truck IS A Vehicle

class Vehicle:
    def setTopSpeed(self, speed):
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

corolla = Car()
corolla.setTopSpeed(220)

volvo = Truck()
volvo.setTopSpeed(180)




