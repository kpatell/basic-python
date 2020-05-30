# Krishan Patel

"""Chaper 12: Collecting Things Together - Lists
From Hello World! Computer Programming for Kids and Beginners
Copyright Warren and Carter Sande, 2009-2013
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f']

print(letters[1])
print(letters[1:4])
letters.append('g')
letters.extend(['h', 'i', 'k'])
print(letters)
letters.insert(9, 'j')
print(letters)
letters.remove('k')
print(letters)
del letters[9]
print(letters)

last_letter = letters.pop()
print()
print(letters)
print("Last letter removed:", last_letter, "\n")

# Searching a list
if 'a' in letters:
    print("Found 'a' in letters")
else:
    print("Fidn't find 'a' in letters")

# Sorting lists
print()
scrambled_letters = ['d', 'a', 'e', 'c', 'b']
print(scrambled_letters)
scrambled_letters.sort()
print(scrambled_letters)

scrambled_letters.reverse()
print(scrambled_letters)

scrambled_letters = ['d', 'a', 'e', 'c', 'b']
scrambled_letters.sort(reverse=True)
print(scrambled_letters)

# 2d lists
print()
joe_marks = [55, 63, 77, 81] # math, science, reading, spelling
tom_marks = [65, 61, 67, 72]
beth_marks = [97, 95, 92, 88]
class_marks = [joe_marks, tom_marks, beth_marks]

for student_marks in class_marks:
    print(student_marks)

print("Joe Reading:", class_marks[0][2])

# Trying it out
print()
names = []

print("Enter 5 names: ")
for i in range(5):
    names.append(input())

print("The names are:", end=" ")
for i in range(5):
    print(names[i], end=" ")

print("\n")
print(names) # Printing the original list of names and a sorted list
names.sort()
print(names)
print()
print("The third name you entered is:", names[2])

print()
index_to_replace = int(input("Replace one name. Which one? (1-5): ")) - 1
new_name = input("New name: ")
names[index_to_replace] = new_name
print("The new names are:", end=" ")

for i in range(5):
    print(names[i], end=" ")
