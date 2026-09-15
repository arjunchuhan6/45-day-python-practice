#use default values in __init__ method and explain the use of self parameter in python class
class Person:
    def __init__(self, name="John Doe", age=30, city    ="New York"):
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")
        

default_person = Person() # Using default values for name, age, and city
default_person.display_info()