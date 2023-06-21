student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
total_height = 0
for i in student_heights:
  total_height += i
print(f"total height = {total_height}")

number_of_students = 0
for i in student_heights:
  number_of_students += 1
print("number of students = {}".format(number_of_students)) 

average_height = total_height // number_of_students
print(average_height)

