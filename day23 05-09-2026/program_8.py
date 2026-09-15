#add display method to display information of multiple objects of different classes
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")
        
class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}")
        
# Create instances of the Person and Employee classes
person1 = Person("Alice", 30, "New York")
person2 = Person("Bob", 25, "Los Angeles")
employee1 = Employee("Charlie", 28, "Software Engineer")
employee2 = Employee("David", 32, "Data Scientist")

# Display information of all objects
def display_all_info(objects):
    for obj in objects:
        obj.display_info()

# Create a list of objects
objects = [person1, person2, employee1, employee2]

# Display information of all objects
display_all_info(objects)