# wap to keeping for numbers until user enters a zero number
while True:
    number = int(input("Enter a number (0 to exit): "))
    if number == 0:
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {number}")