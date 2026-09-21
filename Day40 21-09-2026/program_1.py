# Very simple authentication example
# Authentication = checking whether the user is really who they say they are.
# For example: username + password login.

# We keep a small dictionary of users.
# This is only for learning. In real apps, data is stored in a database.
users: dict[str, str] = {
    "admin": "admin123",
    "student": "student123"
}

# Ask user for username and password.
# Compare them with the stored values.
# If both match, login is successful.
username: str = input("Enter username: ")
password: str = input("Enter password: ")

if username in users and users[username] == password:
    print("Authentication successful! Welcome", username)
else:
    print("Authentication failed! Wrong username or password.")

# Explanation:
# 1. The user gives username and password.
# 2. The program checks if the username exists.
# 3. It compares the password with the saved password.
# 4. If both are correct, the user is authenticated.
#
# Important:
# In real projects, we never store plain text passwords.
# We use hashing like SHA-256 or bcrypt so passwords are protected.
# Also, real authentication may include login attempts, sessions, tokens, and databases.
