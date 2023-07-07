# a list of dictionaries

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherine"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# print houses only using a list
"""
houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)
"""
# print houses only using a set
houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
    
