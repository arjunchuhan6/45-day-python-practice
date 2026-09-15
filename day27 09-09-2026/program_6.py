# 266. Create a generator for squares
# Generator function that yields squares of numbers

print("=== Square Generator Function ===")
def square_generator(n):
    """Generator that yields squares of numbers from 0 to n"""
    for i in range(n):
        yield i ** 2

print("Squares from 0 to 10:")
for square in square_generator(10):
    print(square, end=" ")
print()

print("\n=== Square Generator from List ===")
def squares_from_list(numbers):
    """Generator that yields squares of numbers in a list"""
    for num in numbers:
        yield num ** 2

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Squares of", my_numbers)
for sq in squares_from_list(my_numbers):
    print(sq, end=" ")
print()

print("\n=== Square Generator Expression ===")
# Generator expression for squares (more concise)
squares = (x**2 for x in range(1, 11))
print("Generator expression for squares:")
for sq in squares:
    print(sq, end=" ")
print()

print("\n=== Memory Efficient Comparison ===")
# List comprehension - creates entire list in memory
print("List comprehension:")
square_list = [x**2 for x in range(5)]
print(square_list)
print(f"Type: {type(square_list)}")

# Generator expression - creates values on demand
print("\nGenerator expression:")
square_gen = (x**2 for x in range(5))
print(square_gen)
print(f"Type: {type(square_gen)}")
print(f"Values: {list(square_gen)}")

print("\n=== Using next() with square generator ===")
sq_gen = square_generator(5)
print("First square:", next(sq_gen))   # 0
print("Second square:", next(sq_gen))  # 1
print("Third square:", next(sq_gen))   # 4
print("Fourth square:", next(sq_gen))  # 9
print("Fifth square:", next(sq_gen))   # 16
