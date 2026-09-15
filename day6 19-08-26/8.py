#wap to calculate the sum of entered number
sum = 0
while True:
    number = int(input("Enter a number (0 to exit): "))
    if number == 0:
        break
    sum += number
print(f"The sum of the entered numbers is: {sum}")