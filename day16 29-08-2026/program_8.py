# Student Information Management Program

# 1. Function to create student info - returns multiple values
def create_student(student_id, name, age, courses):
    """Create student information and return as tuple"""
    return student_id, name, age, courses


# 2. Function to display student info
def display_student(student_id, name, age, courses):
    print(f"Student ID: {student_id}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Courses: {', '.join(courses)}")
    print()


# 3. Function to calculate GPA with *args
def calculate_gpa(*grades):
    """Calculate average GPA from multiple grades"""
    if not grades:
        return 0
    return sum(grades) / len(grades)


# 4. Function to update student info with **kwargs
def update_student_info(student_id, name, **kwargs):
    """Update student info with dynamic attributes"""
    student = {
        "id": student_id,
        "name": name
    }
    student.update(kwargs)
    return student


# 5. Function to generate report
def generate_report(name, *grades, **info):
    """Generate student report with grades and additional info"""
    gpa = calculate_gpa(*grades)
    print(f"Report for {name}")
    print(f"Grades: {grades}")
    print(f"GPA: {gpa:.2f}")
    for key, value in info.items():
        print(f"{key}: {value}")
    print()


# ===== Create Student Data =====

print("=== 1. Create Multiple Students ===")
student1 = create_student(101, "Alice Johnson", 20, ["Math", "Physics", "Chemistry"])
student2 = create_student(102, "Bob Smith", 21, ["English", "History", "Art"])
student3 = create_student(103, "Charlie Brown", 20, ["Computer Science", "Mathematics", "Data Science"])

print("Students created successfully!\n")

# 2. Display students
print("=== 2. Display Student Information ===")
display_student(*student1)
display_student(*student2)
display_student(*student3)

# 3. Calculate GPA
print("=== 3. Calculate Student GPA ===")
alice_grades = [95, 88, 92, 90]
bob_grades = [85, 90, 87, 89]
charlie_grades = [98, 95, 99, 97]

alice_gpa = calculate_gpa(*alice_grades)
bob_gpa = calculate_gpa(*bob_grades)
charlie_gpa = calculate_gpa(*charlie_grades)

print(f"Alice's GPA: {alice_gpa:.2f}")
print(f"Bob's GPA: {bob_gpa:.2f}")
print(f"Charlie's GPA: {charlie_gpa:.2f}")
print()

# 4. Update student info with **kwargs
print("=== 4. Update Student Information ===")
updated_alice = update_student_info(101, "Alice Johnson", 
                                   age=20, 
                                   gpa=92.5, 
                                   department="Science",
                                   phone="555-0101")
print("Updated Alice Info:", updated_alice)
print()

# 5. Generate detailed reports
print("=== 5. Generate Student Reports ===")
generate_report("Alice", 95, 88, 92, 90, gpa=92.5, year="2nd", status="Active")
generate_report("Bob", 85, 90, 87, 89, gpa=87.75, year="2nd", status="Active")
generate_report("Charlie", 98, 95, 99, 97, gpa=97.25, year="3rd", status="Dean's List")

# 6. Store all students in a dictionary
print("=== 6. Student Database ===")
students_db = {
    101: {"name": "Alice Johnson", "age": 20, "gpa": 92.5, "courses": 3},
    102: {"name": "Bob Smith", "age": 21, "gpa": 87.75, "courses": 3},
    103: {"name": "Charlie Brown", "age": 20, "gpa": 97.25, "courses": 3}
}

print("Complete Student Database:")
for student_id, info in students_db.items():
    print(f"ID {student_id}: {info['name']} - GPA: {info['gpa']}, Courses: {info['courses']}")
print()

# 7. Filter students by criteria
print("=== 7. Filter Students (GPA > 90) ===")
high_performers = {sid: info for sid, info in students_db.items() if info['gpa'] > 90}
for student_id, info in high_performers.items():
    print(f"ID {student_id}: {info['name']} - GPA: {info['gpa']}")
print()

# 8. Sort students by GPA
print("=== 8. Students Sorted by GPA ===")
sorted_students = sorted(students_db.items(), key=lambda x: x[1]['gpa'], reverse=True)
for student_id, info in sorted_students:
    print(f"{info['name']}: {info['gpa']}")

print("\n### Quick Summary:")
print("- Student ID: 101, 102, 103")
print("- Store in dictionary for easy access")
print("- Functions accept multiple values (*args, **kwargs)")
print("- Can filter and sort students")
print("- GPA calculated from grades")
