# 265. Use yield
# yield statement in a function makes it a generator function

print("=== Yield Example 1 ===")
def my_generator():
    print("Start")
    yield "First"
    print("Middle")
    yield "Second"
    print("End")
    yield "Third"

print("Creating generator...")
gen = my_generator()
print("\nGetting first value...")
print(next(gen))  # Prints "Start" and returns "First"
print("\nGetting second value...")
print(next(gen))  # Prints "Middle" and returns "Second"
print("\nGetting third value...")
print(next(gen))  # Prints "End" and returns "Third"

print("\n=== Yield in a loop ===")
def yield_range(start, end):
    """Generator that yields numbers in range"""
    current = start
    while current < end:
        yield current
        current += 1

for num in yield_range(10, 15):
    print(num, end=" ")
print()

print("\n=== Yield multiple values ===")
def pairs():
    """Generator that yields pairs"""
    yield (1, 'a')
    yield (2, 'b')
    yield (3, 'c')

for number, letter in pairs():
    print(f"{number}: {letter}")

print("\n=== Yield with computation ===")
def fibonacci(limit):
    """Fibonacci generator"""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("Fibonacci sequence up to 50:")
for fib_num in fibonacci(50):
    print(fib_num, end=" ")
print()
