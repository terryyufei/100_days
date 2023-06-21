from clear import clear
from art import logo
print(logo)

print("Welcome to the silent auction")

silent_auction = {}
auction_end = False

def find_highest_bidder(bid_list):
    highest_bid = 0
    winner = ""

    for bidder in bid_list:
        amount = bid_list[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print("The winner is {} with a bid of ${}".format(winner, highest_bid))

while not auction_end:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    silent_auction[name] = bid
    others = input('Are there others who would like to bid? "yes" or "no".\n')

    if others == "no":
        auction_end = True
        find_highest_bidder(silent_auction)
    elif others == "yes":
        clear()




