#python to pratice of inheritance
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name} from the Parent class."
    
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        parent_greeting = super().greet()
        return f"{parent_greeting} I am {self.age} years old from the Child class."

# Example usage
parent_instance = Parent("Alice")
child_instance = Child("Bob", 10)
print(parent_instance.greet())  # Output: Hello, I am Alice from the Parent class
print(child_instance.greet())   # Output: Hello, I am Bob from the Parent class. I am 10 years old from the Child class.