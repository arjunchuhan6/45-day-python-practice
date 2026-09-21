# Authorization Example in Python
# Authorization means checking what a user is allowed to do after login.
# Authentication checks "who you are".
# Authorization checks "what you are allowed to do".

# Example user roles
# admin -> full permission
# user -> limited permission
users: dict[str, str] = {
    "admin": "admin123",
    "user": "user123"
}

roles: dict[str, str] = {
    "admin": "admin",
    "user": "user"
}

# Ask for login details
username: str = input("Enter username: ")
password: str = input("Enter password: ")

# Step 1: Authentication
if username in users and users[username] == password:
    print("Authentication successful!")

    # Step 2: Authorization
    role: str = roles[username]

    if role == "admin":
        print("You are an admin. You can view all data and delete records.")
    elif role == "user":
        print("You are a normal user. You can only view your own data.")
else:
    print("Authentication failed. Please check your username and password.")

# Explanation:
# - First, verify the identity (authentication)
# - Then, decide what the user can do (authorization)
#
# Example:
# - Admin can access everything
# - User can access only limited features
#
# In real applications, authorization is controlled by roles, permissions, and access rules.
