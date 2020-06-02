# Krishan Patel
# Bank Account Class

"""Chaper 14: Objects
From Hello World! Computer Programming for Kids and Beginners
Copyright Warren and Carter Sande, 2009-2013
"""

# Chapter 14 - Try it out
class BankAccount:
    """Creates a bank account"""
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0.0

    def __str__(self):
        bank_account_string = self.name + "\nAccount Number: %s \nBalance: %s" % (self.account_number, round(self.balance, 2))
        return bank_account_string

    def display_balance(self):
        """Displays the balance of the bank account"""
        print("Balance:", self.balance)

    def deposit(self, money_deposit):
        """Makes a deposit into bank account (adds more money to balance)"""
        self.balance += money_deposit

    def withdraw(self, money_withdraw):
        """Withdraws money from bank account (reduces balance)"""
        self.balance -= money_withdraw

class InterestAccount(BankAccount):
    """Type of bank account that earns interest"""
    def add_interest(self, rate):
        """Adds interest to bank account"""
        interest = self.balance*rate
        self.deposit(interest)

# Testing out BankAccount class
print("----------Testing BankAccount----------")
bankAccount = BankAccount("Krishan Patel", 123456)
print(bankAccount)
print()

bankAccount.display_balance()
print()

bankAccount.deposit(34.52)
print(bankAccount)
print()

bankAccount.withdraw(12.25)
print(bankAccount)
print()

bankAccount.withdraw(30.18)
print(bankAccount)
print()

# Testing out InterestAccount class
print("----------Testing InterestAccount----------")
interestAccount = InterestAccount("Krishan Patel", 234567)
print(interestAccount)
print()

interestAccount.display_balance()
print()

interestAccount.deposit(34.52)
print(interestAccount)
print()

interestAccount.add_interest(0.11)
print(interestAccount)
