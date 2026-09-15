#wap to reverse a number using while loop
n = int(input("Enter a number: "))
reversed_number = 0
while n > 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n //= 10
print(f"Reversed number: {reversed_number}")