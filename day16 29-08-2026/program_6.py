# **kwargs - Variable-length Keyword Arguments in Python

# 1. Basic **kwargs example
def print_info(**kwargs):
    """
    Accept multiple keyword arguments
    **kwargs converts all keyword arguments into a dictionary
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 2. Display kwargs details
def show_details(**kwargs):
    print(f"Number of arguments: {len(kwargs)}")
    print(f"Arguments as dictionary: {kwargs}")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")


# 3. Mix positional and **kwargs
def create_user(username, **kwargs):
    print(f"Username: {username}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


# 4. **kwargs with defaults
def build_profile(name, **kwargs):
    profile = {"name": name}
    profile.update(kwargs)
    return profile


# 5. Conditional handling with **kwargs
def filter_data(**kwargs):
    print("Filtered Data:")
    for key, value in kwargs.items():
        if value:  # Only print non-empty values
            print(f"  {key}: {value}")


# 6. **kwargs with default get
def get_user_info(**kwargs):
    name = kwargs.get("name", "Unknown")
    age = kwargs.get("age", "Not specified")
    city = kwargs.get("city", "Not specified")
    email = kwargs.get("email", "Not specified")
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Email: {email}")


# ===== Function Calls =====

print("=== 1. Basic **kwargs ===")
print_info(name="Alice", age=25, city="New York")

print("\n=== 2. Show kwargs details ===")
show_details(color="Red", size="Large", quantity=5)

print("\n=== 3. Mix positional and **kwargs ===")
create_user("john_doe", email="john@example.com", age=28, country="USA")

print("\n=== 4. Build profile dictionary ===")
profile1 = build_profile("Emma", age=30, city="London", profession="Engineer")
print("Profile 1:", profile1)

profile2 = build_profile("Sam", age=25, city="Tokyo")
print("Profile 2:", profile2)

print("\n=== 5. Filter non-empty values ===")
filter_data(name="Bob", age=0, city="", country="India")

print("\n=== 6. Get with default values ===")
print("User 1:")
get_user_info(name="Diana", age=22, city="Paris")

print("\nUser 2:")
get_user_info(name="Charlie", email="charlie@example.com")

print("\nUser 3 (no info):")
get_user_info()

print("\n=== 7. Unpacking dictionary into **kwargs ===")
user_data = {"username": "Eve", "age": 29, "city": "Berlin", "job": "Developer"}
print("Unpacking user_data:")
create_user(**user_data)

print("\n=== 8. Practical example - Settings ===")
def apply_settings(**kwargs):
    defaults = {"theme": "light", "language": "English", "notifications": True}
    defaults.update(kwargs)
    return defaults

settings1 = apply_settings(theme="dark")
print("Settings 1:", settings1)

settings2 = apply_settings(language="Spanish", notifications=False)
print("Settings 2:", settings2)

print("\n### Quick Summary:")
print("- **kwargs allows variable number of keyword arguments")
print("- **kwargs is converted into a dictionary inside the function")
print("- Access values: kwargs['key'] or kwargs.get('key', default)")
print("- Loop through: for key, value in kwargs.items()")
print("- Use **dict to unpack a dictionary when calling function")
print("- Naming: **kwargs is convention, but **options also works")
print("- Order: positional → *args → keyword → **kwargs")
