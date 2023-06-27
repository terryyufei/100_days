print("Is he/she your soulmate?")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

both_names = name1 + name2  #concatenate
lowercase_string = both_names.lower() #changg to lowercase
t = lowercase_string.count("t")  #start counting
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")
true = t + r + u + e

l = lowercase_string.count("l")
o= lowercase_string.count("o")
v = lowercase_string.count("v")
e = lowercase_string.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"your score is {love_score}, you go together like coke and mentos.")
elif(love_score >= 40) and (love_score <= 80):
    print(f"your score is {love_score}, you are alright!")
else:
    print(f"your score is {love_score}")
