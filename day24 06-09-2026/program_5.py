#practice encapsulation
class Student:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")


student = Student("Alice", 20)

print(student.get_name())
print(student.get_age())

student.set_name("Bob")
student.set_age(21)

print(student.get_name())
print(student.get_age())

student.set_age(-1)

