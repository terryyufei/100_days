"""
enemies = 1 #global variable

def increase_enemies():
    enemies = 2 # local variable
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")  
""" 

# Modifying Global scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
    