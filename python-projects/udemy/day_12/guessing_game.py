import random


"""
create a guessing game where the user 
gets to guess what number you are thinking of
The number should be between 1 and 100
should have two difficulty levels; easy and hard
easy level: user gets 10 guesses
hard level: user gets 5 guesses
"""

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == 'easy':
    print("You have 10 attempts remaining to guess the number")
else:
    print("You have 5 attempts remaining to guees the number")

# Generate the random number
def guess_number():
    my_number = random.randint(1, 101)
    guessed = False

    while not guessed:
        # ask user for a number
        user_number = int(input("Make a guess: "))

        #compare random number with user number
        if user_number == my_number:
            print("You got it!")
            guessed = True
        elif user_number < my_number:
            print("Too low.\n Guess again")
        else:
            print("Too high. Try guessing a lower number") 

guess_number()       
