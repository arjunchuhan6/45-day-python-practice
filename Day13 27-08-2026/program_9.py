numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
unique_set = set(numbers)
unique_numbers = [number for number in sorted(unique_set)]

print("Original numbers:", numbers)
print("Numbers without duplicates using a set:", unique_set)
print("Numbers without duplicates using comprehension:", unique_numbers)
