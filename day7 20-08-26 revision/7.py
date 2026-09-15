# wap check a number is prime or composite
n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            print(f"{n} is a composite number.")
            break
    else:
        print(f"{n} is a prime number.")