#Today we learn about exception handling in Python
# in first programming we will write a program to handle exceptions in Python
# The above line will throw an exception if the file does not exist
# wap to handle the exception using try and except block
try:
    with open("test.txt", "r") as file:
            content = file.read()
    print(content)
except FileNotFoundError:
    print("The file does not exist. Please check the file name and try again.")
    
#wap to handle divison by zero exception
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")