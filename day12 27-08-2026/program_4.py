#find the lowest marks
from student_data import students

lowest_mark_student = min(students, key=lambda student: student["marks"])

print("Student with the lowest marks:")
print(f"Name: {lowest_mark_student['name']}")
print(f"Marks: {lowest_mark_student['marks']}")
