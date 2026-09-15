# Build a student class completely
import json


class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")

    def update_age(self, new_age):
        self.age = new_age
        print(f"Age updated to: {self.age}")

    def update_student_id(self, new_student_id):
        self.student_id = new_student_id
        print(f"Student ID updated to: {self.student_id}")

    def save_to_json(self, filename="student_data.json"):
        student_data = {
            "name": self.name,
            "age": self.age,
            "student_id": self.student_id
        }
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(student_data, file, indent=4)
        print(f"Student data saved to {filename}")

# Create an instance of the Student class using user input
name = input("Enter student name: ")
age = int(input("Enter student age: "))
student_id = input("Enter student ID: ")
student1 = Student(name, age, student_id)

# Display the student's information
student1.display_info()

# Update the student's age
new_age = int(input("Enter new age: "))
student1.update_age(new_age)

# Update the student's ID
new_student_id = input("Enter new student ID: ")
student1.update_student_id(new_student_id)

# Save the updated student's information to a JSON file
student1.save_to_json()
