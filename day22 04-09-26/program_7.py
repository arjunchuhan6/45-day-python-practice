# Accessing object attributes

class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age


# student is an object of the Student class.
student = Student("Aarav", 20)

# Use dot notation to access the object's attributes.
print(student.name)
print(student.age)



