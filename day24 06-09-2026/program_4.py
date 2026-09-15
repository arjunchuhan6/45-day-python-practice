#overrise a method
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name} from the Parent class."


class Child(Parent):
    def greet(self):
        parent_greeting = super().greet()
        return f"{parent_greeting} I am from the Child class."


parent_instance = Parent("Alice")
child_instance = Child("Bob")

print(parent_instance.greet())
print(child_instance.greet())

