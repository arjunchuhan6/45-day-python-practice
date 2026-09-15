# An object is an instance of a class. It stores data in attributes and can
# use the class's methods.
class Car:
	def __init__(self, brand, color):
		self.brand = brand
		self.color = color

	def describe(self):
		return f"This {self.color} {self.brand} car is ready to drive."

# car1 and car2 are objects of the Car class.
car1 = Car("Toyota", "red")
car2 = Car("Honda", "blue")

print(car1.describe())
print(car2.describe())
