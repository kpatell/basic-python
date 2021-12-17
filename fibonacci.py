"""Basic function to print n terms out of the fibonacci sequence
"""


def fibonacci(n_terms) -> int:
    """Method that prints the fibonacci sequence until the n-th number"""
    if n_terms <= 1:
        return n_terms
    return (fibonacci(n_terms - 1) + fibonacci(n_terms - 2))


print("How many terms of fibonacci sequence to print?: ", end="")
terms = int(input())
while terms <= 0:
    print("Please input a positive integer: ")
    terms = int(input())

print("----------------------------")
for i in range(terms):
    print(fibonacci(i), end=", ")
