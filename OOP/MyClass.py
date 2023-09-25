class MyClass:
    pass

obj = MyClass()  # creating a MyClass Object
print(obj)

###########################################

class MyClass:
    name = "I'm actually OBJ"
    def __init__(self, name=name):
        self.name = name

    def __repr__(self):
        return ":)"


obj = MyClass(8)  # creating a MyClass Object
print(obj.name)
print(obj)
print(obj.name)