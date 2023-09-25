# BAD EXAMPLE OF ENCAPSULATION
class User:
    def __init__(self, userName=None, password=None):
        self.userName = userName
        self.password = password

    def login(self, userName, password):
        if ((self.userName.lower() == userName.lower())
                and (self.password == password)):
            print("Access Granted!")
        else:
            print("Invalid Credentials!")

Steve = User("Steve", "12345")
Steve.login("steve", "6789")
Steve.password = "6789"  # THE FACT THAT THIS IS POSSIBLE IS VERY BAD
Steve.login("steve", "6789")

print("####################################")
# GOOD EXAMPLE OF ENCAPSULATION
class User:
    def __init__(self, userName=None, password=None):
        self.__userName = userName
        self.__password = password

    def login(self, userName, password):
        if self.__userName.lower() == userName.lower() and self.__password == password:
            print("Access Granted against username:", self.__userName.lower(),
                  "and password:", self.__password)
        else:
            print("Invalid Credentials!")

Steve = User("Steve", "12345")
Steve.login("steve", "12345")  # Grants access because credentials are valid

# does not grant access since the credentials are invalid
Steve.login("steve", "6789")
# print(Steve.__password)  # compilation error will occur due to this line

# For encapsulating a class, all the properties should be private and any access to the properties should be through methods such as getters and setters.

