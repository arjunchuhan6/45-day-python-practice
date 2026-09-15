#filter even numbers and odd numbers from a list using filter function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("even numbers:", even_numbers)
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("odd numbers:", odd_numbers)