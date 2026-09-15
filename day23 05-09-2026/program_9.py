#add update method
class MyClass:
    def __init__(self, value):
        self.value = value

    def update(self, new_value):
        self.value = new_value
        
#create an instance of MyClass
my_instance = MyClass(10)

# Update the value of the instance
my_instance.update(20)

# Print the updated value
print(my_instance.value)  # Output: 20