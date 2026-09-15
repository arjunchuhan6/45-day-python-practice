#wap to create a number guesing game but in last it will tell the user how many attempts he/she took to guess the number and also tell the user if he/she guessed the number in first attempt or not
    
import random

secret_number = random.randint(1, 100)
attempts = 0
first_attempt = True

while True:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        if first_attempt:
            print("Wow! You guessed the number in your first attempt.")
        break
    elif guess < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")

    first_attempt = False
