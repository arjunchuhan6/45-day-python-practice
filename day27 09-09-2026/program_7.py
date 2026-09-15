# 267. Create a decorator
# A decorator is a function that modifies or enhances another function or class

print("=== Simple Decorator ===")
def my_decorator(func):
    """A simple decorator function"""
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

print("\n=== Decorator with Arguments ===")
def repeat_decorator(times):
    """Decorator that repeats function execution"""
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator

@repeat_decorator(3)
def say_goodbye():
    print("Goodbye!")

say_goodbye()

print("\n=== Decorator with Function Arguments ===")
def add_prefix_decorator(prefix):
    """Decorator that adds a prefix to output"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{prefix}]", end=" ")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@add_prefix_decorator("INFO")
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

print("\n=== Timer Decorator ===")
import time

def timer_decorator(func):
    """Decorator that measures execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(0.1)
    print("Function completed")

slow_function()
