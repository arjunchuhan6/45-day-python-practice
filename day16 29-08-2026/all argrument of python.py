# Function Arguments in Python

# 1. Positional arguments

def greet(name):
    print(f"Hello, {name}!")


# 2. Keyword arguments

def add(a, b):
    return a + b


# 3. Default arguments

def student_info(name, age=18, city="Delhi"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


# 4. Variable-length positional arguments (*args)

def show_numbers(*numbers):
    print("Numbers:", numbers)


# 5. Variable-length keyword arguments (**kwargs)

def show_details(**details):
    print("Details:", details)


# Calling the functions
print("=== Positional arguments ===")
greet("Aman")

print("\n=== Keyword arguments ===")
print("Sum:", add(a=10, b=20))

print("\n=== Default arguments ===")
student_info("Riya")
student_info("Rahul", 22, "Mumbai")

print("\n=== *args ===")
show_numbers(1, 2, 3, 4, 5)

print("\n=== **kwargs ===")
show_details(name="Sam", age=25, city="Pune")

print("\n### Quick summary:")
print("- Positional arguments: passed by position")
print("- Keyword arguments: passed by name")
print("- Default arguments: used if not provided")
print("- *args: many positional values")
print("- **kwargs: many keyword values")
