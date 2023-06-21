# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

list_items = len(names)
random_choice = random.randint(0, list_items - 1)
person = names[random_choice]
print(person + " is going to buy the meal today!")

random_choice = random.randint(0, list_items - 1)
person = names[random_choice]
print(person + " is going to buy drinks today!")