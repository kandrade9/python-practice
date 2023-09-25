class Vehicle:
    def setTopSpeed(self, speed):
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)

class Car(Vehicle):
    # @staticmethod  # we have the option to make this function static since the logic within is not interacting w the class whatsoever
    def openTrunk(self):
        print("Trunk is now open.")


corolla = Car()  # creating an object of the Car class
corolla.setTopSpeed(220)  # accessing methods from the parent class
corolla.openTrunk()  # accessing method from its own class