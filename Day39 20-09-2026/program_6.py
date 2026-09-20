import re
from typing import Any


class APIError(Exception):
	status_code = 500

	def __init__(self, message, details=None) -> None:
		super().__init__(message)
		self.message: Any = message
		self.details = details


class BadRequestError(APIError):
	status_code = 400


class ValidationError(APIError):
	status_code = 422


def validate_registration(request_data):
	try:
		if not isinstance(request_data, dict):
			raise BadRequestError("Request body must be an object.")

		errors = {}
		name = request_data.get("name")
		if not isinstance(name, str) or not name.strip():
			errors["name"] = "Name is required."

		email = request_data.get("email")
		if not isinstance(email, str) or not re.fullmatch(
			r"[A-Za-z0-9._%+-]+@gmail\.com", email.strip()
		):
			errors["email"] = "Email must end with @gmail.com."

		if errors:
			raise ValidationError("Request validation failed.", errors)

		return {"valid": True, "message": "Registration successful."}, 201
	except APIError as error: 
		response = {"valid": False, "error": error.message}
		if error.details:
			response["errors"] = error.details
		return response, error.status_code


if __name__ == "__main__":
	request: dict[str, str] = {
		"name": input("Enter your name: "),
		"email": input("Enter your Gmail address: "),
	}
	response, status_code = validate_registration(request)
	print({"status_code": status_code, "response": response})
