from greetings import greet_user, farewell_user
from math_utils import add, multiply, average


def main():
    name = input("Enter your name: ")
    print(greet_user(name))

    x = 12
    y = 8
    print(f"Addition: {add(x, y)}")
    print(f"Multiplication: {multiply(x, y)}")

    numbers = [10, 20, 30, 40]
    print(f"Average: {average(numbers)}")

    print(farewell_user(name))


if __name__ == "__main__":
    main()
