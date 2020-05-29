# Krishan Patel
# Copyright Warren and Carter Sande, 2009-2013

"""Chaper 11: Nested Loops
From Hello World! Computer Programming for Kids and Beginners"""

# Asks user input for number of blocks, lines, and stars and prints it
# numBlocks = int(input("How many blocks of stars do you want? "))
# numLines = int(input("How many lines in each block? "))
# numStars = int(input("How many stars per line? "))

# for block in range(0, numBlocks):
#     for line in range(0, numLines):
#         for star in range(0, numStars):
#             print('*', end = " ")
#         print()
#     print()

# Staggers star blocks
# numBlocks = int(input("How many blocks of stars do you want? "))
# for block in range(1, numBlocks + 1):
#     for line in range(1, block*2):
#         for star in range(1, (block + line)*2):
#             print("*", end = " ")
#         print()
#     print()

Hotdog combinations - to demonstrate permutations
dog_cal = 140
bun_cal = 120
ket_cal = 80
mus_cal = 20
onion_cal = 40

print("\tDog \tBun \tKetchup\tMustard\tOnions\tCalories")
count = 1

for dog in [0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    total_cal = (bun*bun_cal) + (dog*dog_cal) + \
                        (ketchup*ket_cal) + (mustard*mus_cal) + \
                            (onion*onion_cal)

                    print("#", count, "\t", end = " ")
                    print(dog, "\t", bun, "\t", ketchup, "\t", end = " ")
                    print(mustard, "\t", onion, end = " ")
                    print("\t", total_cal)
                    count += 1

# Countdown timer that asks the user whee to start
# and prints stars beside each number
# import time
# seconds = int(input("Countdown Timer: How many seconds? "))
# for i in range(seconds, 0, -1):
#     print(i, end = " ")
    
#     for star in range(i):
#         print("*", end = " ")
#     print()

#     time.sleep(1)
# print("Blast off!")