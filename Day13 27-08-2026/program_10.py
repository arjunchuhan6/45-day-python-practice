# Five mixed comprehension problems

# 1. Create squares of numbers from 1 to 10.
squares = [number ** 2 for number in range(1, 11)]

# 2. Create a list of even numbers from 1 to 20.
even_numbers = [number for number in range(1, 21) if number % 2 == 0]

# 3. Convert names to uppercase.
names = ["aarav", "riya", "kabir", "ananya"]
uppercase_names = [name.upper() for name in names]

# 4. Create a dictionary containing numbers and their cubes.
cubes = {number: number ** 3 for number in range(1, 6)}

# 5. Create a multiplication table using a nested comprehension.
multiplication_table = [
    [row * column for column in range(1, 11)]
    for row in range(1, 11)
]

print("1. Squares:", squares)
print("2. Even numbers:", even_numbers)
print("3. Uppercase names:", uppercase_names)
print("4. Number cubes:", cubes)
print("5. Multiplication table:")
for row in multiplication_table:
    print(row)
