#build a basic student management system class with methods to add, remove, and display students
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, age):
        student = {"name": name, "age": age}
        self.students.append(student)
        return f"Student {name} added."

    def remove_student(self, name):
        for student in self.students:
            if student["name"] == name:
                self.students.remove(student)
                return f"Student {name} removed."
        return f"Student {name} not found."

    def display_students(self):
        if not self.students:
            return "No students in the system."
        return "\n".join([f"Name: {student['name']}, Age: {student['age']}" for student in self.students])
    
# Create an object of the StudentManagementSystem class
sms = StudentManagementSystem()

# Add some students
print(sms.add_student("Alice", 20))
print(sms.add_student("Bob", 22))
print(sms.add_student("Charlie", 21))

# Display all students
print(sms.display_students())

# Remove a student
print(sms.remove_student("Bob"))

# Display all students again
print(sms.display_students())