#practice polymorphism
class Animal:
    def sound(self):
        return "The animal makes a sound."

class Dog(Animal):
    def sound(self):
        return "The dog barks."

class Cat(Animal):
    def sound(self):
        return "The cat meows."
    
# Example usage
animal_instance = Animal()
dog_instance = Dog()
cat_instance = Cat()

print(animal_instance.sound())
print(dog_instance.sound())
print(cat_instance.sound())