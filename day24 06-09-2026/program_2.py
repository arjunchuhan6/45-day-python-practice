#create a parent class called Animal
class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        return f"The {self.species} makes a sound."
    
#create a child class called Dog that inherits from Animal

# Example usage
animal_instance = Animal("Animal")

print(animal_instance.sound())  # Output: The Animal makes a sound.
