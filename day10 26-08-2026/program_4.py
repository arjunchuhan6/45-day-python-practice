# wap to use unpack

student = ("Ravi", 20, "Python")

# Each tuple element is assigned to one variable.
name, age, course = student
print("Name:", name)
print("Age:", age)
print("Course:", course)

# A starred variable collects the remaining elements in a list.
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print("First:", first)
print("Middle:", middle)
print("Last:", last)