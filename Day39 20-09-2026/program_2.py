import re


def validate_email(email) -> None | str:
	"""Return an error message when an API email is invalid."""
	if not isinstance(email, str):
		return "Email must be a string."

	email: str = email.strip()
	if not email:
		return "Email is required."
	if len(email) < 5 or len(email) > 50:
		return "Email must be between 5 and 50 characters."
	if not re.fullmatch(r"[A-Za-z0-9._%+-]+@gmail\.com", email):
		return "Email must be a valid Gmail address ending with @gmail.com."

	return None


def validate_api_request(request_data):
	"""Validate the email field in an API request body."""
	if not isinstance(request_data, dict):
		return {"valid": False, "error": "Request body must be an object."}

	error: None | str = validate_email(request_data.get("email"))
	if error:
		return {"valid": False, "error": error}

	return {"valid": True, "message": "Email is valid."}


if __name__ == "__main__":
	email: str = input("Enter your Gmail address: ")
	result = validate_api_request({"email": email})
	print(result)
