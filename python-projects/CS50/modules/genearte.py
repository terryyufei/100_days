# using from
"""
from random import choice

coin = choice(["heads", "tails"])
print(coin)
"""
# using import
import random

coin = random.choice(["heads", "tails"])
#print(coin)

number = random.randint(1, 10)
#print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

