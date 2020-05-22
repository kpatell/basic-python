import random

secret = random.randint(1, 99)
guess = 0
tries = 0

print("\n-----------------------------------------------------------------")
print("AHOY! I'm the Dread Pirate Roberts, and I have a secret!")
print("It is a number from 1 to 99. I'll give you 6 tries.\n")

while guess != secret and tries < 6:
    guess = int(input("What's yer guess? "))
    
    if guess < secret:
        print("Too low, ye scurvy dog!\n")
    elif guess > secret:
        print("Too high, landlubber!\n")

    tries = tries + 1

    if guess == secret:
        print("Avast! Ye got it! Found my secret, ye did!")

if guess != secret and tries == 6:
    print("No more guesses! Better luck next time, matey!")
    print("The secret number was", secret)
    
print("\n-----------------------------------------------------------------")