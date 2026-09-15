# 264. Create a generator
# A generator is a simple way to create iterators using a function with yield

print("=== Simple Generator ===")
def simple_generator():
    """A simple generator that yields numbers"""
    yield 1
    yield 2
    yield 3

# Create generator object
gen = simple_generator()
print(type(gen))  # <class 'generator'>
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

print("\n=== Generator in a loop ===")
def count_up(n):
    """Generator that counts from 1 to n"""
    i = 1
    while i <= n:
        yield i
        i += 1

for number in count_up(5):
    print(number, end=" ")
print()

print("\n=== Generator Expression ===")
# Generator expression (similar to list comprehension but with parentheses)
squares_gen = (x**2 for x in range(5))
print("Generator expression:", squares_gen)

for square in squares_gen:
    print(square, end=" ")
print()

print("\n=== Infinite Generator ===")
def infinite_counter():
    """An infinite generator"""
    n = 0
    while True:
        yield n
        n += 1

count = infinite_counter()
for _ in range(6):
    print(next(count), end=" ")
print()
