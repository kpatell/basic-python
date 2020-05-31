# Krishan Patel

"""Chaper 13: Functions
From Hello World! Computer Programming for Kids and Beginners
Copyright Warren and Carter Sande, 2009-2013
"""

# 13.1: Creating and using a function
# 13.2: Passing an argument to a functiom
def print_my_address(my_name, house_number):
    """Prints address"""
    print(my_name)
    print(house_number, end=" ")
    print("Main Street")
    print("Chicago, Illinois, USA")
    print("K2M 2E9")
    print()

print_my_address("Krishan Patel", "123")
print_my_address("Jack Black", "64")
print_my_address("Tom Green", "22")
print_my_address("Todd White", "36")

# 13.4: Creating and using a function that returns a value
# 13.7: Trying to modify a global variable inside a function
def calculate_tax(price, tax_rate):
    """Calculates tax given a price and tax rate"""
    total = price + (price*tax_rate)
    my_price = 10000
    print("my_price (inside function) =", my_price)
    return total

my_price = float(input("Enter a price: "))
total_price = calculate_tax(my_price, 0.06)
print("price =", my_price, " Total price =", total_price)
print("my_price (outside function) =", my_price)

# Try it out
def print_big_initials():
    """Prints initials in big letters"""
    print("""
    K   K  P P P
    K  K   P    P
    K K    P P P
    K  K   P
    K   K  P
    """)

print_big_initials()

def address(name, street, city, state, zip_code, country):
    """7-argument function that prints full address"""
    print(name)
    print(street)
    print(city, end=" ")
    print(state, end=" ")
    print(zip_code)
    print(country)
    print()

address("Krishan Patel", "123 Main Street", "Chicago", "IL", "12345", "USA")

def total_change(num_q, num_d, num_n, num_p):
    """Adds up and returns the amount of change"""
    total = (0.25*num_q) +(0.1*num_d) + (0.05*num_n) + (0.01*num_p)
    return round(total, 2)

quarters = float(input("Quarters: "))
dimes = float(input("Dimes: "))
nickels = float(input("Nickels: "))
pennies = float(input("Pennies: "))
print("Total: $", end="")
print(total_change(quarters, dimes, nickels, pennies))
