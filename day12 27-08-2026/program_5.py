from student_data import students

total_marks = sum(student["marks"] for student in students)
average_marks = total_marks / len(students)

print(f"Average marks: {average_marks:.2f}")