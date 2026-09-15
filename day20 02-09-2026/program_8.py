# WAP to use raise in exception handling
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    if num2 == 0:
        raise ValueError("Division by zero is not allowed.")

    result = num1 / num2
    print("The result is:", result)
except ValueError as error:
    print("Error:", error)


