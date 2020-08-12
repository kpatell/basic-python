# Krishan Patel
# Ball Class

"""Chaper 14: Objects
From Hello World! Computer Programming for Kids and Beginners
Copyright Warren and Carter Sande, 2009-2013
"""

# 14.1: Creating a simple Ball class
# 14.2: Using the Ball class
# 14.3: Adding an __init__() method
# 14.4: Using __str__() to change how the object prints
class Ball:
    """Creates a ball"""
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def __str__(self):
        msg = "Hi, I'm a " + self.size + " " + self.color + \
            " ball! I am going " + self.direction + "wards."
        return msg

    def bounce(self):
        """Ball bounces"""
        if self.direction == "down":
            self.direction = "up"

MY_BALL = Ball("red", "small", "down")
print(MY_BALL)
MY_BALL.bounce()
print(MY_BALL)
