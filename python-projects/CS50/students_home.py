import csv
"""
students = []

with open("students_home.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
"""
#as a dictionary
"""
students = []

with open("students_home2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
"""

# Writing to a csv file
"""
name = input("What is your name? ")
home = input("Where's your home? ")

with open("students_home3.csv", 'a') as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
"""

#using a dictionary

name = input("What is your name? ")
home = input("Where's your home? ")

with open("students_home3.csv", 'a') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})