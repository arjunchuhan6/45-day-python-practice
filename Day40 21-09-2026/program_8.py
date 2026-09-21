# Python Program 8: Protect an Endpoint with a Token

from typing import Literal

from flask import Flask, Response, jsonify, request
from flask.wrappers import Response

app = Flask(__name__)

# This is a sample token for learning.
# In a real application, tokens are created after a successful login.
valid_token = "abc123xyz"


@app.route("/public", methods=["GET"])
def public_endpoint() -> Response:
	return jsonify({"message": "Anyone can access this endpoint"})


@app.route("/profile", methods=["GET"])
def protected_endpoint() -> tuple[Response, Literal[401]] | tuple[Response, Literal[200]]:
	# Read the token from the Authorization header.
	authorization_header: str | None = request.headers.get("Authorization")

	# A correct header looks like this:
	# Authorization: Bearer abc123xyz
	if not authorization_header:
		return jsonify({"message": "Token is required"}), 401

	# Split the header into two parts: Bearer and the token value.
	header_parts: list[str] = authorization_header.split(" ", 1)

	if len(header_parts) != 2 or header_parts[0] != "Bearer":
		return jsonify({"message": "Invalid Authorization header"}), 401

	token: str = header_parts[1]

	# Allow access only when the token is valid.
	if token != valid_token:
		return jsonify({"message": "Invalid or expired token"}), 401

	return jsonify({
		"message": "You can access this protected endpoint",
		"profile": {
			"username": "admin",
			"role": "user"
		}
	}), 200


if __name__ == "__main__":
	app.run(debug=True)

# How to test in Postman:
# 1. Start the program.
# 2. Send GET http://127.0.0.1:5000/public without a token.
# 3. Send GET http://127.0.0.1:5000/profile.
# 4. Open the Headers tab and add:
#       Key: Authorization
#       Value: Bearer abc123xyz
# 5. The protected endpoint will return the profile only with a valid token.
#
# Without a token, the API returns 401 Unauthorized.
# A protected endpoint allows access only after the token is checked.