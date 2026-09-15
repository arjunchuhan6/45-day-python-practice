# create employee constructor
class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}")
        
# Create an instance of the Employee class
employee1 = Employee("Bob", 25, "Software Engineer")
employee1.display_info()
employee2 = Employee("Charlie", 28, "Data Scientist")
employee2.display_info()
