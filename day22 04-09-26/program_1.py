# create a student class with attributes name, age, and grade
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

print("Student class created successfully.")
student1 = Student("John", 20, "A")
student2 = Student("Jane", 22, "B")
print(f"Student 1: {student1.name}, Age: {student1.age}, Grade: {student1.grade}")
print(f"Student 2: {student2.name}, Age: {student2.age}, Grade: {student2.grade}")