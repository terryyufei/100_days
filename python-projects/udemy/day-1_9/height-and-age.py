print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height >= 120:
    print("yay! you can ride!!")
    age = int(input("what is your age? "))
    if age < 12:
        print("please pay $12")
    elif age <= 18:
        print("please pay $15")
    else:
        print("please pay $18")
else:
    print("sorry, you are too short to ride")