from student_data import students

highest_mark_student = max(students, key=lambda student: student["marks"])

print("Student with the highest marks:")
print(f"Name: {highest_mark_student['name']}")
print(f"Marks: {highest_mark_student['marks']}")