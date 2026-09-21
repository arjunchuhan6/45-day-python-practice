# Simple API for validating login credentials
# Authentication means checking if a user is really who they say they are.
# In this API, we check the username and password entered by the user.

from typing import Any, Literal

from flask import Flask, Response, jsonify, request
from flask.wrappers import Response

app = Flask(__name__)

# Stored valid users
# In real projects, these values should come from a database.
valid_users: dict[str, str] = {
    "admin": "admin123",
    "student": "student123"
}


@app.route("/", methods=["GET"])
def home() -> Response:
    return jsonify({"message": "Login API is running. Use POST /login"})


@app.route("/login", methods=["POST"])
def login() -> tuple[Response, Literal[400]] | tuple[Response, Literal[200]] | tuple[Response, Literal[401]]:
    data: Any | None = request.get_json(silent=True)

    if not data:
        return jsonify({"message": "No JSON data sent"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    # Validate credentials
    if username in valid_users and valid_users[username] == password:
        return jsonify({
            "message": "Login successful",
            "username": username
        }), 200

    return jsonify({"message": "Invalid username or password"}), 401


if __name__ == "__main__":
    app.run(debug=True)

# Explanation:
# 1. Client sends JSON data to /login
# 2. API reads username and password
# 3. It checks if username exists in valid_users
# 4. It compares the entered password with the saved password
# 5. If both match, login is successful
# 6. If not, it returns 401 Unauthorized

# Example JSON request in Postman:
# {
#   "username": "admin",
#   "password": "admin123"
# }
