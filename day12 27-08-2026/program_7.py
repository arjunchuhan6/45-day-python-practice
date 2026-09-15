from student_data import students

student_name = input("Enter student name: ").strip().casefold()
new_marks = int(input("Enter new marks (0-100): "))

if not 0 <= new_marks <= 100:
    print("Marks must be between 0 and 100.")
else:
    for student in students:
        if student["name"].casefold() == student_name:
            student["marks"] = new_marks
            print(f"{student['name']}'s marks updated to {new_marks}.")
            break
    else:
        print("Student not found.")
