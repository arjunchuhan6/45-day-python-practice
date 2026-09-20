def validate_age(age) -> None | str:
	if isinstance(age, bool) or not isinstance(age, int):
		return "Age must be an integer."
	if age < 18 or age > 60:
		return "Age must be between 18 and 60."

	return None


def validate_salary(salary) -> None | str:
	if isinstance(salary, bool) or not isinstance(salary, (int, float)):
		return "Salary must be a number."
	if salary <= 15000:
		return "Salary must be greater than 15000."

	return None


def validate_api_request(request_data):
	if not isinstance(request_data, dict):
		return {"valid": False, "error": "Request body must be an object."}

	age_error: None | str = validate_age(request_data.get("age"))
	if age_error:
		return {"valid": False, "field": "age", "error": age_error}

	salary_error: None | str = validate_salary(request_data.get("salary"))
	if salary_error:
		return {"valid": False, "field": "salary", "error": salary_error}

	return {"valid": True, "message": "Age and salary are valid."}


if __name__ == "__main__":
	age = int(input("Enter your age: "))
	salary = float(input("Enter your salary: "))
	print(validate_api_request({"age": age, "salary": salary}))
