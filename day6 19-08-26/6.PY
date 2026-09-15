#wap to keep asking for a password untill the correct one is entered
correct_password = "python123"
while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Password correct!")
        break
    else:
        print("Incorrect password. Please try again.")