from clear import clear_string
from art import logo
print(logo)

print("Welcome to the silent auction")

silent_auction = {}

name = input("What is your name? ")
bid = input("What is your bid? $")

silent_auction[name] = bid
print(silent_auction)

others = input("Are there others who would like to bid? Yes or No ").lower()





