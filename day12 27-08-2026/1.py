from student_data import students

print("Student details:")
for number, student in enumerate(students, start=1):
    print(f"\nStudent {number}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Course: {student['course']}")
    print(f"Marks: {student['marks']}")

print("\nAll student names:")
for student in students:
    print(student["name"])