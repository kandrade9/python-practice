# Duck typing extends the concept of dynamic typing in Python.
# Dynamic typing means that we can change the type of an object later in the code.

###################
# Dynamic nature of Python
x = 5  # type of x is an integer
print(type(x))

x = "Educative"  # type of x is now string
print(type(x))
###################
# Implementing Duck Typing
class Dog:
    def Speak(self):
        print("Woof woof")


class Cat:
    def Speak(self):
        print("Meow meow")


class AnimalSound:
    # Type of animal is determined when the method is called,
    # so it does not matter which object type you are passing as a parameter in the Sound() method,
    # what matters is that the Speak() method should be defined in all the classes whose objects are passed in the Sound() method.
    def Sound(self, animal):  # type of animal is not defined in method definition as you can see
        animal.Speak()


sound = AnimalSound()
dog = Dog()
cat = Cat()

# If it sounds like a dog, it's a dog. Same for cat.
sound.Sound(dog)  # Here, AnimalSound object sound is a dog
sound.Sound(cat)  # Here, AnimalSound object sound is a cat

# The animal object does not matter in the definition of the Sound method as long as it has the associated behavior, Speak(), defined in the object’s class definition.
# In layman terms, since both the animals, dogs and cats, can speak like animals, they both are animals. This is how we have achieved polymorphism without inheritance.


