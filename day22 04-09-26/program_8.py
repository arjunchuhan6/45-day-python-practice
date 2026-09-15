# Adding a method to a class

class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def introduce(self):
		return f"My name is {self.name} and I am {self.age} years old."

	def study(self, subject):
		return f"{self.name} is studying {subject}."

	def have_birthday(self):
		self.age += 1
		return f"{self.name} is now {self.age} years old."


# student is an object of the Student class.
student = Student("Aarav", 20)

# Call the method using the object and dot notation.
print(student.introduce())
print(student.study("Python"))
print(student.have_birthday())
