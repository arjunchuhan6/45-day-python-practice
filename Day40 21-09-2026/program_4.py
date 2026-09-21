# Simple Login API Example
# An API is a way for apps to send and receive data over HTTP.
# In this example, the client sends username and password to the server.
# The server checks whether the login details are valid.

from typing import Any, Literal


from flask.wrappers import Response
from werkzeug.datastructures.structures import ImmutableMultiDict


try:
    from flask import Flask, jsonify, request, render_template_string
except ModuleNotFoundError:
    Flask = None
    jsonify = None
    request = None
    render_template_string = None

# This dictionary stores valid users.
# In real projects, this data is normally saved in a database.
users: dict[str, str] = {
    "admin": "admin123",
    "student": "student123"
}


# This function checks whether the username and password are valid.
def check_login(username: str, password: str) -> bool:
    # Authentication means verifying the identity of the user.
    if username in users and users[username] == password:
        return True
    return False


# Create the API app only if Flask is installed.
if Flask is not None:
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def home() -> str:
        return render_template_string("""
            <html>
            <body>
                <h2>Login Form</h2>
                <form method="POST" action="/login">
                    <label>Username:</label><br>
                    <input type="text" name="username"><br><br>
                    <label>Password:</label><br>
                    <input type="password" name="password"><br><br>
                    <button type="submit">Login</button>
                </form>
            </body>
            </html>
        """)

    @app.route("/login", methods=["GET", "POST"])
    def login_api() -> str | tuple[Response, Literal[400]] | tuple[Response, Literal[200]] | tuple[Response, Literal[401]]:
        if request.method == "GET":
            return render_template_string("""
                <html>
                <body>
                    <h2>Login API</h2>
                    <p>Use POST to send username and password.</p>
                </body>
                </html>
            """)

        # Accept JSON request from API clients
        data: Any | None = request.get_json(silent=True)

        # If no JSON, try form data from browser
        if not data:
            data: ImmutableMultiDict[str, str] = request.form

        if not data:
            return jsonify({"message": "No data sent"}), 400

        username: str | None | Any = data.get("username")
        password: str | None | Any = data.get("password")

        if not username or not password:
            return jsonify({"message": "Username and password are required"}), 400

        if check_login(username, password):
            return jsonify({
                "message": "Login successful",
                "status": "success",
                "username": username
            }), 200
        else:
            return jsonify({
                "message": "Invalid username or password",
                "status": "failed"
            }), 401


    if __name__ == "__main__":
        app.run(debug=True)
else:
    print("Flask is not installed. To run the API, install it with:")
    print("pip install flask")
    print()
    print("Example API request JSON:")
    print('{"username": "admin", "password": "admin123"}')

# Explanation:
# 1. The browser can open the home page with GET /.
# 2. The login form submits data with POST /login.
# 3. API clients can send JSON data to POST /login.
# 4. If valid, it returns success; else, it returns error.
#
# In a real API, passwords should be hashed and stored securely.
