from student_data import students

subject = input("Enter a course: ").strip().casefold()
matching_students = [
    student for student in students
    if student["course"].casefold() == subject
]

if matching_students:
    print("\nStudents enrolled in that course:")
    for student in matching_students:
        print(f"{student['name']} - {student['course']}")
else:
    print("No student found for that course.")