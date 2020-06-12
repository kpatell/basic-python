"""Number guessing game using a GUI
From Hello World! Computer Programming for Kids and Beginners by Carter and Warren Sande.
"""

import random
import easygui

secret = random.randint(1, 99)
GUESS = 0
TRIES = 0

easygui.msgbox("""AHOY! I'm the Dread Pirate Roberts, and I have a secret!
It is a number from 1 to 99. I'll give you 6 tries.""")

while GUESS != secret and TRIES < 6:
    GUESS = easygui.integerbox("What's yer guess, matey?")

    if not GUESS:
        break

    if GUESS < secret:
        easygui.msgbox(str(GUESS) + " is too low, ye scurvy dog!")
    elif GUESS > secret:
        easygui.msgbox(str(GUESS) + " is too high, landlubber!")

    TRIES += 1

if GUESS == secret:
    easygui.msgbox("Avast! Ye got it! Found my secret, ye did!")
else:
    easygui.msgbox("No more guesses! Better luck next time, matey!")
    easygui.msgbox("The secret was " + str(secret))
