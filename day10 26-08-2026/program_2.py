# acces tuple elements

fruits = ("apple", "banana", "cherry", "orange")

# Indexing starts at 0.
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Negative indexes count from the end.
print("Last fruit:", fruits[-1])

# Slicing accesses a range of elements.
print("First two fruits:", fruits[0:2])

# Unpacking assigns tuple elements to variables.
first, second, third, fourth = fruits
print("Unpacked values:", first, second, third, fourth)
