students = ["Hermione", "Harry", "Ron"]
"""
gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor" })

print(gryffindors)
"""

# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# Dictionary comphrension
gryffindors = {student: "Gryffindor" for student in students}
#print(gryffindors)


# using enumerate: synatx is enumerate(iterable, start=0)
for i, student in enumerate(students):
    print(i + 1, student)
