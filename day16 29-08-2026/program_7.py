# Function Returning Multiple Values in Python

# 1. Return multiple values using tuple (most common)
def get_student_info():
    name = "Alice"
    age = 22
    gpa = 3.8
    return name, age, gpa  # Returns as tuple


# 2. Unpack returned tuple into individual variables
def get_coordinates():
    x = 10
    y = 20
    z = 30
    return x, y, z


# 3. Return multiple values with different data types
def calculate_results(a, b):
    sum_val = a + b
    product = a * b
    quotient = a / b if b != 0 else 0
    return sum_val, product, quotient


# 4. Return multiple values as list
def get_numbers():
    return [5, 10, 15, 20, 25]


# 5. Return dictionary with multiple values
def get_user_profile():
    return {
        "name": "Bob",
        "age": 28,
        "city": "New York",
        "email": "bob@example.com"
    }


# 6. Return multiple values with default unpacking
def get_colors():
    return "Red", "Green", "Blue"


# 7. Partial unpacking with asterisk
def get_data():
    return 1, 2, 3, 4, 5


# 8. Return values from calculations
def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    max_val = max(numbers)
    min_val = min(numbers)
    return total, average, max_val, min_val


# ===== Function Calls and Usage =====

print("=== 1. Return multiple values as tuple ===")
name, age, gpa = get_student_info()
print(f"Name: {name}, Age: {age}, GPA: {gpa}")

print("\n=== 2. Unpack coordinates ===")
x, y, z = get_coordinates()
print(f"X: {x}, Y: {y}, Z: {z}")

print("\n=== 3. Calculate and unpack results ===")
sum_result, prod_result, quot_result = calculate_results(10, 5)
print(f"Sum: {sum_result}")
print(f"Product: {prod_result}")
print(f"Quotient: {quot_result}")

print("\n=== 4. Return as list ===")
numbers = get_numbers()
print(f"Numbers: {numbers}")
print(f"First: {numbers[0]}, Last: {numbers[-1]}")

print("\n=== 5. Return as dictionary ===")
user = get_user_profile()
print(f"User: {user}")
print(f"Name: {user['name']}, City: {user['city']}")

print("\n=== 6. Unpack colors ===")
color1, color2, color3 = get_colors()
print(f"Colors: {color1}, {color2}, {color3}")

print("\n=== 7. Partial unpacking with * ===")
first, *middle, last = get_data()
print(f"First: {first}, Middle: {middle}, Last: {last}")

print("\n=== 8. Calculate statistics ===")
data = [10, 20, 30, 40, 50]
total, avg, max_v, min_v = calculate_stats(data)
print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Max: {max_v}")
print(f"Min: {min_v}")

print("\n=== 9. Without unpacking (return as tuple) ===")
result = get_student_info()
print(f"Result type: {type(result)}")
print(f"Result: {result}")
print(f"Access by index: {result[0]}, {result[1]}")

print("\n### Quick Summary:")
print("- Return multiple values as tuple: return a, b, c")
print("- Unpack easily: x, y, z = function()")
print("- Can return tuple, list, dict, or any object")
print("- Use * for partial unpacking: first, *rest, last = func()")
print("- Access via index if not unpacking: result[0]")
print("- Most Pythonic: return as tuple and unpack immediately")
