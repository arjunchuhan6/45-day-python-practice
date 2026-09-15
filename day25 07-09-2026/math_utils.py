def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
