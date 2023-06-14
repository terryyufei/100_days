#THE GOAL IS TO PRINT MEOW 3 TIMES
'''
#USING WHILE LOOP
i = 3
while i > 0:
    print("meow")
    i -= 1
'''

#USING FOR LOOP
'''
for i in [0, 1, 2]: #using a list, not advisible when you want to iterate over a large data
    print("meow")   # python automatically initiliazes i to zero
'''
'''
#using range function which is advisibale
for _ in range(3): #using _ is good practise when you are only using a varible because the python
    print("meow") #function requires you to
'''

#PRINT MEOW 3 TIMES USING ONLY THE PRINT() FUNCTION
#print("meow\n" * 3, end='')
print("meow", "meow", "meow", sep="\n")

'''
#TAKE INPUT FROM USER
while True:
    n = int(input("What is n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
'''

#LISTS
"""
students = ["sophia", "winnie", "lorna"]
#print(students[0], students[1], students[2])
#print(students[0])
#print(students[1])
#print(students[2])

#for student in students:
    #print(f"-{student}")

#for index, student in enumerate(students, start=1): #adding enumerate() to print numbers
    #print(f"{index}. {student}")

for i in range(len(students)): #using the range function
    print(i + 1, students[i]) #printing out with numbers, +1 because it counts from zero
"""

#DICTIONARY
'''
students = {
    "hermoine": "gryffindor",
    "harry": "gryffindor",
    "ron": "gryffindor",
    "draco": "slytherin",
}
#print(students["hermoine"])

for student in students:
    print(student, students[student], sep=": ") #prints both key and value
'''
