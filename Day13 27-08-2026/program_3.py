# Create even and odd number lists using comprehensions
numbers = range(1, 21)
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
