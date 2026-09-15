# 262. Use iter()
# iter() function creates an iterator object from an iterable

# Example 1: Using iter() with a list
print("=== Using iter() with a list ===")
numbers = [1, 2, 3, 4, 5]
number_iterator = iter(numbers)

print(next(number_iterator))  # Output: 1
print(next(number_iterator))  # Output: 2
print(next(number_iterator))  # Output: 3

print("\n=== String Iterator ===")
# Example 2: Using iter() with a string
text = "Hello"
text_iterator = iter(text)

for char in text_iterator:
    print(char, end="-")
print()

print("\n=== Dictionary Iterator ===")
# Example 3: Using iter() with a dictionary (iterates over keys)
my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_iterator = iter(my_dict)

for key in dict_iterator:
    print(f"Key: {key}, Value: {my_dict[key]}")

print("\n=== Tuple Iterator ===")
# Example 4: Using iter() with a tuple
tuple_data = (10, 20, 30, 40)
tuple_iterator = iter(tuple_data)

print("Tuple elements:")
for val in tuple_iterator:
    print(val)
