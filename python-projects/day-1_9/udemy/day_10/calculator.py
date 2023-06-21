# Calculator(Trial)
"""
# Add
def add(a, b):
    return a + b

# Subtract
def sub(a, b):
    return a - b

# Multiply
def mul(a, b):
    return a * b

# Divide
def div(a, b):
    return a / b

# Create a dictionary
operations = {
    "+": add,
    "-": sub, 
    "*": mul, 
    "/": div,
}

# Ask user for first input
num1 = int(input("What's a?: "))

# Try to loop and print all the operations
for sign in operations:
    print(sign)

proceed = True

# Ask user to pick a sign
operation_sign = input("Pick an operation sign from the line above: ")

# Ask user for second input
num2 = int(input("What's b?: "))

# Try and use the sign picked to do calculations
calculation_function = operations[operation_sign]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_sign} {num2} = {answer}")

# Print vs Return

operation_sign = input("Pick another operation sign: ")
num3 = int(input("What's the next number?: "))
calculation_function = operations[operation_sign]
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_sign} {num3} = {second_answer}")


# Try and use the while loop to allow user to do as many calculations as possible
while proceed:
        operation_sign = input("Pick another operation sign: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operation_sign]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_sign} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
             num1 = answer
        else:
             proceed = False
 """            
    
# Final Calculator with exit option
"""
# Add
def add(a, b):
    return a + b

# Subtract
def sub(a, b):
    return a - b

# Multiply
def mul(a, b):
    return a * b

# Divide
def div(a, b):
    return a / b

# Create a dictionary
operations = {
    "+": add,
    "-": sub, 
    "*": mul, 
    "/": div,
}

# Ask user for first input
num1 = int(input("What's a?: "))

# Try to loop and print all the operations
for sign in operations:
    print(sign)
# Use while loop to allow as many calculations as possible 
proceed = True

while proceed:
        operation_sign = input("Pick an operation sign: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operation_sign]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_sign} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
             num1 = answer
        else:
             proceed = False
"""

# Final calculator with Recursion
from art import logo
print(logo)
# Add
def add(a, b):
    return a + b

# Subtract
def sub(a, b):
    return a - b

# Multiply
def mul(a, b):
    return a * b

# Divide
def div(a, b):
    return a / b

# Create a dictionary
operations = {
    "+": add,
    "-": sub, 
    "*": mul, 
    "/": div,
}
def calclator():
    # Ask user for first input
    num1 = float(input("What's a?: "))

    # Try to loop and print all the operations
    for sign in operations:
        print(sign)
    # Use while loop to allow as many calculations as possible 
    proceed = True

    while proceed:
        operation_sign = input("Pick an operation sign: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_sign]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_sign} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start afresh.: ") == "y":
             num1 = answer
        else:
             proceed = False
             calclator()

calclator()
