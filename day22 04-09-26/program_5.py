#add attribute to class
class MyClass:
    def __init__(self, name):
        self.name = name  # Adding an attribute 'name' to the class

    def greet(self):
        return f"Hello, {self.name}!"  # Method that uses the 'name' attribute
print("MyClass created successfully.")
obj1 = MyClass("Alice")
obj2 = MyClass("Bob")
print(obj1.greet())  # Output: Hello, Alice!
print(obj2.greet())  # Output: Hello, Bob!