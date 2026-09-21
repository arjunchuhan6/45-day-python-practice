# Store hashed passwords in SQLite and expose them through an API
# This version uses a real database instead of a JSON file.
# Passwords are hashed before saving and compared on login.

from doctest import Example
import hashlib
import sqlite3
from typing import Any, Literal
from wsgiref import headers

from flask.wrappers import Response

try:
    from flask import Flask, jsonify, request
except ModuleNotFoundError:
    Flask = None
    jsonify = None
    request = None

DB_NAME = "users.db"

# Function to hash password using SHA-256
# SHA-256 is a simple hashing example for learning.
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Create database connection and table if it does not exist.
def get_db_connection() -> sqlite3.Connection:
    connection: sqlite3.Connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
        """
    )
    connection.commit()
    return connection

# Register a new user
# Save only the hashed password in the SQLite database.
def register_user(username: str, password: str) -> bool:
    connection: sqlite3.Connection = get_db_connection()
    cursor: sqlite3.Cursor = connection.cursor()

    existing = cursor.execute(
        "SELECT 1 FROM users WHERE username = ?",
        (username,)
    ).fetchone()

    if existing:
        connection.close()
        return False

    cursor.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, hash_password(password))
    )
    connection.commit()
    connection.close()
    return True

# Login check
# Hash the entered password and compare with the stored hash in SQLite.
def login_user(username: str, password: str) -> bool:
    connection: sqlite3.Connection = get_db_connection()
    row = connection.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username,)
    ).fetchone()
    connection.close()

    if row is None:
        return False

    stored_hash = row["password_hash"]
    return stored_hash == hash_password(password)


if Flask is not None:
    app = Flask(__name__)

    @app.route("/register", methods=["POST"])
    def register_api() -> tuple[Response, Literal[400]] | tuple[Response, Literal[201]] | tuple[Response, Literal[409]]:
        data: Any | None = request.get_json(silent=True)
        if not data:
            return jsonify({"message": "No data sent"}), 400

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"message": "Username and password are required"}), 400

        if register_user(username, password):
            return jsonify({"message": "Registration successful"}), 201
        return jsonify({"message": "User already exists"}), 409

    @app.route("/login", methods=["POST"])
    def login_api() -> tuple[Response, Literal[400]] | tuple[Response, Literal[200]] | tuple[Response, Literal[401]]:
        data: Any | None = request.get_json(silent=True)
        if not data:
            return jsonify({"message": "No data sent"}), 400

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"message": "Username and password are required"}), 400

        if login_user(username, password):
            return jsonify({"message": "Login successful", "username": username}), 200
        return jsonify({"message": "Invalid username or password"}), 401

    if __name__ == "__main__":
        app.run(debug=True)
else:
    print("Flask is not installed. Install it with: pip install flask")

# Explanation:
# - The real password is never stored directly.
# - The password is hashed before saving in SQLite.
# - On login, the entered password is also hashed.
# - If both hashes match, the user is authenticated.
# - This is a real database example for learning.
