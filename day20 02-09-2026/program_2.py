#wap to handle invalid integer input exception without try and except block
num = input("Enter an integer: ")
if num.isdigit():
    print("You entered:", int(num))
else:
    print("Error: Invalid input. Please enter a valid integer.")