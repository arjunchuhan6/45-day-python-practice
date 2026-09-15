# 263. Use next()
# next() function retrieves the next item from an iterator

print("=== Basic next() usage ===")
numbers = [10, 20, 30, 40, 50]
num_iter = iter(numbers)

print("First:", next(num_iter))   # 10
print("Second:", next(num_iter))  # 20
print("Third:", next(num_iter))   # 30

print("\n=== next() with default value ===")
# When iterator is exhausted, next() raises StopIteration
# We can provide a default value to avoid the error

string_iter = iter("AB")
print(next(string_iter))           # A
print(next(string_iter))           # B
print(next(string_iter, "END"))    # END (default value)
print(next(string_iter, "DONE"))   # DONE (default value)

print("\n=== next() in a loop ===")
list_data = [100, 200, 300]
iter_obj = iter(list_data)

try:
    while True:
        value = next(iter_obj)
        print(f"Got: {value}")
except StopIteration:
    print("Iterator exhausted!")

print("\n=== Using next() with range ===")
range_iter = iter(range(5, 10))
print("Elements from range(5, 10):")
while True:
    value = next(range_iter, None)
    if value is None:
        break
    print(value)
