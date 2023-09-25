class DecoratorTest(object):
    """Test regular method vs @classmethod vs @staticmethod"""
    def __init__(self):
        pass

    def doubler(self, x):
        print("running doubler")
        return x*2

    @classmethod
    def class_tripler(cls, x):
        print("running tripler: %s" % cls)
        return x*3

    @staticmethod
    def static_quad(x):
        print("running quad")
        return x*4

if __name__ == "__main__":
    decor = DecoratorTest()
    print(decor.doubler(5))
    print(decor.class_tripler(3))

    print(DecoratorTest.class_tripler(3))

    print(decor.static_quad(3))
    print(DecoratorTest.static_quad(2))

    print(decor.doubler)
    print(decor.class_tripler)
    print(decor.static_quad)

# You will notice that you can call both the @classmethod and the @staticmethod decorated functions directly from the class or from an instance of the class.
# If you try to call a regular function with the class (i.e. DecoratorTest.doubler(2)) you will receive a TypeError.
# You will also note that the last print statement shows that decor.static_quad returns a regular function instead of a bound method.