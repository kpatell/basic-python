# Krishan Patel
# Hotdog Class

"""Chaper 14: Objects
From Hello World! Computer Programming for Kids and Beginners
Copyright Warren and Carter Sande, 2009-2013
"""

# 14.6: HotDog class with cook(), add_condiments() and __str__()
class HotDog:
    """Creats a hotdog object"""
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Raw"
        self.condiments = []

    def __str__(self):
        msg = "hot dog"

        if len(self.condiments) > 0:
            msg = msg + " with "

        for i in self.condiments:
            msg = msg + i + ", "

        msg = msg.strip(", ")
        msg = self.cooked_string + " " + msg + "."
        return msg

    def cook(self, time):
        """Cooks the hotdog a certain amount of time and
        then changes the cooked_level to the appropriate
        level it is cooked
        """
        self.cooked_level = self.cooked_level + time

        if self.cooked_level > 8:
            self.cooked_string = "Charcoal"
        elif self.cooked_level > 5:
            self.cooked_string = "Well-done"
        elif self.cooked_level > 3:
            self.cooked_string = "Medium"
        else:
            self.cooked_string = "Raw"

    def add_condiment(self, condiment):
        """Adds a condiment to the hotdog"""
        self.condiments.append(condiment)

myDog = HotDog()
print(myDog)
print()
print("Cooking hot dog for 4 minutes...")
myDog.cook(4)
print(myDog)
print()
print("Cooking hot dog for 3 more minutes...")
myDog.cook(3)
print(myDog)
print()
print("What happens if I cook it for more 10 more minutes?")
myDog.cook(10)
print(myDog)
print()
print("Now, I'm going to add some stuff on my hot dog")
myDog.add_condiment("ketchup")
myDog.add_condiment("mustard")
print(myDog)
