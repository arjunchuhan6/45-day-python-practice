#create a employee class with attributes name, age, and salary
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

print("Employee class created successfully.")
employee1 = Employee("Alice", 30, 50000)
employee2 = Employee("Bob", 35, 60000)
employee3 = Employee("Charlie", 28, 55000)
print(f"Employee 1: {employee1.name}, Age: {employee1.age}, Salary: {employee1.salary}")
print(f"Employee 2: {employee2.name}, Age: {employee2.age}, Salary: {employee2.salary}")
print(f"Employee 3: {employee3.name}, Age: {employee3.age}, Salary: {employee3.salary}")
