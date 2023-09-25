class Player:
    teamName = 'Liverpool'  # class variables
    def __init__(self, name):
        self.name = name  # creating instance variables

p1 = Player('Mark')
p2 = Player('Steve')

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print("Name:", p2.name)
print("Team Name:", p2.teamName)

# WRONGFUL USE OF CLASS VARIABLES
# ALL OOBJECTS OF A CLASS SHARE THE SAME CLASS VARIABLES
class Player:
    formerTeams = []  # class variables
    teamName = 'Liverpool'
    def __init__(self, name):
        self.name = name  # creating instance variables

p1 = Player('Mark')
p1.formerTeams.append('Barcelona') # wrong use of class variable
p2 = Player('Steve')
p2.formerTeams.append('Chelsea') # wrong use of class variable

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print(p1.formerTeams)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
print(p2.formerTeams)

# CORRECT IMPLEMENTATION BELOW
class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables
        self.formerTeams = []

p1 = Player('Mark')
p1.formerTeams.append('Barcelona')
p2 = Player('Steve')
p2.formerTeams.append('Chelsea')

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print(p1.formerTeams)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
print(p2.formerTeams)


