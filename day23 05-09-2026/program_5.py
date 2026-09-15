#use multiple attributes in __init__ method and explain the use of self parameter in python class

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")

# Create an instance of the Person class
person1 = Person("Alice", 30, "New York")
person1.display_info()

person2 = Person("Bob", 25, "Los Angeles")
person2.display_info()

person3 = Person("Charlie", 28, "Chicago")
person3.display_info()