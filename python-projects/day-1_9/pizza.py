print("Welcome to Sophia's Pizza palace!")
size = input("What size of pizza do you want? S, M, or L? ")
pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do yo want extra cheese? Y or N? ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is : ${bill}")
print("Enjoy your meal!")   
