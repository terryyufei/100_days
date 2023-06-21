print("Welcome to the tip calculator")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("how many people will split the bill? "))
30
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
amount = "{:.2f}" .format(bill_per_person)

print(f"Each person should pay: ${amount}")