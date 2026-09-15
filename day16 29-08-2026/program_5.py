# Simple Program: Multiple Arguments using *args

# Simple function to add multiple numbers
def add(*args):
    result = sum(args)
    return result


# Simple function to print all items
def print_items(*args):
    for item in args:
        print(item)


# Simple function to find maximum
def find_max(*args):
    if args:
        return max(args)
    return None


# Simple function to concatenate strings
def combine_text(*args):
    return " ".join(args)


# ===== Test the functions =====

print("1. Add multiple numbers:")
print("add(5, 10):", add(5, 10))
print("add(1, 2, 3, 4, 5):", add(1, 2, 3, 4, 5))
print("add(100, 200):", add(100, 200))

print("\n2. Print multiple items:")
print("Items:")
print_items("Apple", "Banana", "Cherry", "Date")

print("\n3. Find maximum value:")
print("Max of (10, 25, 15, 50):", find_max(10, 25, 15, 50))
print("Max of (100, 200, 50):", find_max(100, 200, 50))

print("\n4. Combine text:")
print("combine_text('Hello', 'World'):", combine_text("Hello", "World"))
print("combine_text('Python', 'is', 'awesome'):", combine_text("Python", "is", "awesome"))
