# Keyword Arguments in Python

# 1. Basic keyword argument example
def introduce(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


# 2. Keyword arguments with default values
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Cannot divide by zero"


# 3. Using **kwargs (variable-length keyword arguments)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 4. Mixed positional and keyword arguments
def create_profile(username, email, age=None, country="Unknown", verified=False):
    print(f"Username: {username}")
    print(f"Email: {email}")
    if age:
        print(f"Age: {age}")
    print(f"Country: {country}")
    print(f"Verified: {verified}")


# ===== Function Calls =====

print("=== 1. Positional order (no keywords) ===")
introduce("Alice", 25, "New York")

print("\n=== 2. Using keyword arguments (any order) ===")
introduce(city="London", name="Bob", age=30)

print("\n=== 3. Mixed positional and keyword ===")
introduce("Charlie", age=28, city="Paris")

print("\n=== 4. Keyword arguments with defaults ===")
print("Add (default):", calculate(10, 5))
print("Subtract:", calculate(10, 5, operation="subtract"))
print("Multiply:", calculate(10, 5, operation="multiply"))
print("Divide:", calculate(10, 5, operation="divide"))

print("\n=== 5. Using **kwargs ===")
print_info(name="Diana", age=27, city="Tokyo", profession="Engineer")

print("\n=== 6. Mixed positional and keyword with defaults ===")
create_profile("john_doe", "john@example.com")
create_profile("jane_smith", "jane@example.com", age=24, country="India", verified=True)

print("\n=== 7. Keyword unpacking (dictionary unpacking) ===")
user_data = {"name": "Eve", "age": 29, "city": "Berlin"}
introduce(**user_data)

print("\n=== 8. Mixed kwargs and **kwargs ===")
profile_data = {"username": "emma_99", "email": "emma@example.com", "country": "Germany", "verified": True}
create_profile(**profile_data, age=26)

print("\n### Quick Summary:")
print("- Keyword arguments: passed by name (key=value)")
print("- Order doesn't matter with keyword arguments")
print("- Can mix positional and keyword arguments")
print("- Positional args must come before keyword args in the call")
print("- **kwargs collects multiple keyword arguments into a dictionary")
print("- Use **dict to unpack a dictionary as keyword arguments")
