# Only Registration Example
# Registration means creating a new account for a user.
# The user gives a username and password, and we save it.

# This dictionary stores registered users.
# In real projects, this data is saved in a database.
users = {}

# This function registers a new user.
def register() -> None:
    username: str = input("Create username: ")
    password: str = input("Create password: ")

    # Check if the username already exists.
    if username in users:
        print("Username already exists. Please choose another one.")
    else:
        # Save the username and password in the dictionary.
        users[username] = password
        print("Registration successful!")

# Call the register function.
register()

# Explanation:
# - Registration is the first step in authentication.
# - We create an account with a username and password.
# - In real apps, we do not store passwords in plain text.
# - We usually hash the password for security.
