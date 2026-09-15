# 268. Apply a decorator to a function
# Demonstrate various ways to apply decorators

print("=== Decorator Application Method 1: Using @ symbol ===")
def uppercase_decorator(func):
    """Decorator that converts output to uppercase"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@uppercase_decorator
def get_message():
    return "hello world"

print(get_message())

print("\n=== Decorator Application Method 2: Direct assignment ===")
def bold_decorator(func):
    """Decorator that adds bold formatting"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*** {result} ***"
    return wrapper

def say_name():
    return "Alice"

say_name = bold_decorator(say_name)
print(say_name())

print("\n=== Multiple Decorators ===")
def add_stars(func):
    """Adds stars around output"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{'*' * 5} {result} {'*' * 5}"
    return wrapper

def add_brackets(func):
    """Adds brackets around output"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"[{result}]"
    return wrapper

@add_stars
@add_brackets
def get_text():
    return "DECORATED"

print(get_text())

print("\n=== Decorator on Class Method ===")
class Calculator:
    @staticmethod
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Calling function: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    def add(self, a, b):
        print(f"Adding {a} + {b}")
        return a + b

calc = Calculator()
result = calc.add(5, 3)
print(f"Result: {result}")

print("\n=== Decorator with functools.wraps ===")
import functools

def logging_decorator(func):
    """Decorator that logs function calls"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logging_decorator
def multiply(x, y):
    """Multiply two numbers"""
    return x * y

print(multiply(4, 5))
print(f"Function name: {multiply.__name__}")
print(f"Function docstring: {multiply.__doc__}")
