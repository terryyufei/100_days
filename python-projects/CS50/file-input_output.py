#just an intro
"""
names = [] #create an empty list

for _ in range(3):
    names.append(input("What is your name? "))

for name in sorted(names):
    print(f"Hello, {name}")
"""

#using open() function and write() method
"""
name = input("What's your name? ")

file = open('names.txt', 'w') #opened in write (w) mode
file.write(name)
file.close()
print(file)
"""

#using 'a' append mode to add names to a file
"""
name = input("What is your name? ")

file = open('names-append.txt', 'a')
file.write(f"{name}\n")
file.close()
print(file)
"""

#Using with (automatically handles file closing)
"""
name = input("What is your name? ")

with open('names_append.txt', 'a') as file:
    file.write(f"{name}\n")
"""

#Reading from a file
"""
with open('names_append.txt', 'r') as file:
    content = file.read()
    #print(content, end="")

#or
with open("names_append.txt", 'r') as file:
    lines = file.readlines() #reads all the lines from a file and return them as list
    #print(lines)

for line in lines:
    print("Hello", line, end="")
    #or use rstrip() to separate one line from another
    #print("Hello", line.rstrip())

#or
with open("names_append.txt", 'r') as file:
    for line in file:
        #print("hello", line.rstrip)
"""

# To read from a file and print out sorted data

names = [] #create an empty list to store the names.

with open("names_append.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")