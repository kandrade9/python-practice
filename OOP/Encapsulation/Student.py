# Here is an example where we do not use initializers to initialize the properties. Instead, we use the set methods to do so.
class Student:
    __name = None
    __rollNumber = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber


demo1 = Student()
demo1.setName("Alex")
print("Name:", demo1.getName())
demo1.setRollNumber(3789)
print("Roll Number:", demo1.getRollNumber())
