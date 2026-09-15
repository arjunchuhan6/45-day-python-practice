from student_data import students

student_name = input("Enter the student name to delete: ").strip().casefold()

for index, student in enumerate(students):
    if student["name"].casefold() == student_name:
        deleted_student = students.pop(index)
        print(f"{deleted_student['name']} was deleted.")
        break
else:
    print("Student not found.")
