from _io import TextIOWrapper
from io import TextIOWrapper
import json
import re
from pathlib import Path


DATA_FILE: Path = Path(__file__).with_name("registrations.json")


def validate_registration(request_data):
	if not isinstance(request_data, dict):
		return {"valid": False, "error": "Request body must be an object."}, 400

	errors = {}
	name = request_data.get("name")
	if not isinstance(name, str) or not name.strip():
		errors["name"] = "Name is required."

	email = request_data.get("email")
	if not isinstance(email, str) or not re.fullmatch(
		r"[A-Za-z0-9._%+-]+@gmail\.com", email.strip()
	):
		errors["email"] = "Email must end with @gmail.com."

	age = request_data.get("age")
	if isinstance(age, bool) or not isinstance(age, int) or not 18 <= age <= 60:
		errors["age"] = "Age must be an integer between 18 and 60."

	salary = request_data.get("salary")
	if isinstance(salary, bool) or not isinstance(salary, (int, float)) or salary <= 15000:
		errors["salary"] = "Salary must be greater than 15000."

	if errors:
		return {"valid": False, "errors": errors}, 422

	return {"valid": True, "message": "Registration successful."}, 201


def save_registration(request_data):
	try:
		registrations = []
		if DATA_FILE.exists():
			with DATA_FILE.open("r", encoding="utf-8") as file: 
				registrations = json.load(file)

		if not isinstance(registrations, list):
			registrations = []
		registrations.append(request_data)

		with DATA_FILE.open("w", encoding="utf-8") as file: 
			json.dump(registrations, file, indent=4)
		return {"valid": True, "message": "Registration saved."}, 201
	except (OSError, json.JSONDecodeError):
		return {"valid": False, "error": "Could not save registration data."}, 500


if __name__ == "__main__":
	age_input: str = input("Enter your age: ")
	salary_input: str = input("Enter your salary: ")

	try:
		age = int(age_input)
	except ValueError:
		age: str = age_input

	try:
		salary = float(salary_input)
	except ValueError:
		salary: str = salary_input

	request: dict[str, str] = {
		"name": input("Enter your name: "),
		"email": input("Enter your Gmail address: "),
		"age": age,
		"salary": salary,
	}
	response, status_code = validate_registration(request)
	if status_code == 201:
		response, status_code = save_registration(request)
	print({"status_code": status_code, "response": response})
