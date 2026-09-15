#use else for exception handling
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("No exceptions occurred.")