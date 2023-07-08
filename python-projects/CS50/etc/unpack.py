"""
    total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

#coins = [100, 50, 25]

#print(total(coins[0], coins[1], coins[2]), "knuts")
#print(total(*coins), "knuts")

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

#print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "knuts")
print(total(**coins), "knuts")
"""

def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25)
