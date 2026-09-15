#create a child class called Cat that inherits from Animal
from program_2 import Animal


class Cat(Animal):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color

    def sound(self):
        parent_sound = super().sound()
        return f"{parent_sound} The {self.color} cat meows."
    
# Example usage
cat_instance = Cat("Cat", "black")
print(cat_instance.sound())  # Output: The Cat makes a sound. The black cat meows.