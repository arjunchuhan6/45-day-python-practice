# 261. Create an iterator
# An iterator is an object that implements __iter__() and __next__() methods

class CountUp:
    """Custom iterator class that counts up to a given number"""
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        """Return the iterator object itself"""
        return self
    
    def __next__(self):
        """Return the next value"""
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Create an instance of our iterator
counter = CountUp(5)

# Iterate through the values
for num in counter:
    print(num)

print("\n--- Fibonacci Iterator ---")

# Creating a custom iterator for fibonacci sequence
class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a < self.limit:
            value = self.a
            self.a, self.b = self.b, self.a + self.b
            return value
        else:
            raise StopIteration

fib = FibonacciIterator(100)
print("Fibonacci numbers up to 100:")
for num in fib:
    print(num, end=" ")
print()
