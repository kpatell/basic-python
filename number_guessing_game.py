"""Number guessing game"""

import random

secret = random.randint(1, 99)
GUESS = 0
TRIES = 0

print("\n-----------------------------------------------------------------")
print("AHOY! I'm the Dread Pirate Roberts, and I have a secret!")
print("It is a number from 1 to 99. I'll give you 6 tries.\n")

while GUESS != secret and TRIES < 6:
    GUESS = int(input("What's yer guess? "))

    if GUESS < secret:
        print("Too low, ye scurvy dog!\n")
    elif GUESS > secret:
        print("Too high, landlubber!\n")

    TRIES = TRIES + 1

    if GUESS == secret:
        print("Avast! Ye got it! Found my secret, ye did!")

if GUESS != secret and TRIES == 6:
    print("No more guesses! Better luck next time, matey!")
    print("The secret number was", secret)

print("\n-----------------------------------------------------------------")
