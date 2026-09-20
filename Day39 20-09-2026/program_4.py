def validate_age(age) -> None | str:
	if age is None:
		return "Age is required."
	if isinstance(age, bool) or not isinstance(age, int):
		return "Age must be an integer."
	if age < 18 or age > 60:
		return "Age must be between 18 and 60."

	return None


def validate_salary(salary) -> None | str:
	if salary is None:
		return "Salary is required."
	if isinstance(salary, bool) or not isinstance(salary, (int, float)):
		return "Salary must be a number."
	if salary <= 15000:
		return "Salary must be greater than 15000."

	return None


def validate_api_request(request_data):
	if not isinstance(request_data, dict):
		return {"valid": False, "error": "Request body must be an object."}

	errors = {}
	age_error: None | str = validate_age(request_data.get("age"))
	if age_error:
		errors["age"] = age_error

	salary_error: None | str = validate_salary(request_data.get("salary"))
	if salary_error:
		errors["salary"] = salary_error

	if errors:
		return {"valid": False, "errors": errors}

	return {"valid": True, "message": "Age and salary are valid."}


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

	print(validate_api_request({"age": age, "salary": salary}))
