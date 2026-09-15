employee = {
    "name": "Riya",
    "age": 28,
    "department": "IT",
    "salary": 60000,
    "employee_id": "EMP101",
    "email": "riya@example.com",
    "experience": 5,
    "city": "Pune"
}

# Access a value
print("Employee name:", employee["name"])

# Display all keys, values, and key-value pairs
print("Keys:", employee.keys())
print("Values:", employee.values())
print("Items:", employee.items())

# Safely access a value using get()
print("Department:", employee.get("department"))

# Display each employee detail
print("\nEmployee details:")
for key, value in employee.items():
    print(f"{key.capitalize()}: {value}")
