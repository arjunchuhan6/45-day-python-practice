#wap to create a simple login program

users = {
    "admin": "admin123",
    "student": "student123",
    "user": "user123"
}

attempts = 3

print("Welcome to the Login System")

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("\nLogin successful! Welcome", username)
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Invalid username or password. {attempts} attempts left.")
        else:
            print("\nInvalid username or password. No attempts left. Account locked.")
