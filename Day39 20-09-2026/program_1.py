import re


def validate_name(name) -> None | str:
	"""Return an error message when an API name is invalid."""
	if not isinstance(name, str):
		return "Name must be a string."

	name: str = name.strip()
	if not name:
		return "Name is required."
	if len(name) < 2 or len(name) > 50:
		return "Name must be between 2 and 50 characters."
	if not re.fullmatch(r"[A-Za-z]+(?:[ '\-][A-Za-z]+)*", name):
		return "Name can contain only letters, spaces, apostrophes, and hyphens."

	return None


def validate_api_request(request_data):
	"""Validate the name field in an API request body."""
	if not isinstance(request_data, dict):
		return {"valid": False, "error": "Request body must be an object."}

	error: None | str = validate_name(request_data.get("name"))
	if error:
		return {"valid": False, "error": error}

	return {"valid": True, "message": "Name is valid."}


if __name__ == "__main__":
	name: str = input("Enter your name: ")
	result = validate_api_request({"name": name})
	print(result)
