#construction use __init__ method to initialize the object and explain the use of self parameter in python class
# In Python, the `__init__` method is a special method that is automatically called when a new instance of a class is created. It is used to initialize the attributes of the object. The `self` parameter in the `__init__` method refers to the instance of the class that is being created. It allows you to access the attributes and methods of the class within the method.
#use __init__ method to initialize the object and explain the use of self parameter in python class
# The `self` parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#complete code with example of class using __init__ method and self parameter
class Person:
    def __init__(self, name, age):
        self.name = name  # Assigning the name parameter to the instance attribute 'name'
        self.age = age    # Assigning the age parameter to the instance attribute 'age'
        print(f"Object initialized with name: {self.name} and age: {self.age}")

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class
person1 = Person("Alice", 30)
person1.greet()