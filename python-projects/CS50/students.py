#Read and interprete a csv file
"""
with open('students.csv') as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
        #or 
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
"""
#Creating a dictionary and sorting the data

students = []

with open('students.csv') as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student ={"name": name, "house": house}
        students.append(student)
"""
def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
"""

# Or use the lambda function instead of defining a function

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")