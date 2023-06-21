import os

def clear():
    # Clear the console screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

