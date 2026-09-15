#create a student constructor
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Major: {self.major}")
        
# Create an instance of the Student class
student1 = Student("David", 20, "Computer Science")
student1.display_info()
student2 = Student("Eva", 22, "Mathematics")
student2.display_info()
