# create multiple objects of the class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"
    
# dog1 and dog2 are objects of the Dog class.
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print(dog1.bark())
print(dog2.bark())