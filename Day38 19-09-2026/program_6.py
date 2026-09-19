"""Program 6: add an employee directly to SQLite without an API endpoint."""

import sqlite3
from pathlib import Path


DATABASE: Path = Path(__file__).with_name("employees.db")


def add_employee(name: str, email: str, department: str, salary: float) -> int:
	"""Insert an employee and return the new employee ID."""
	if not name.strip() or not email.strip() or not department.strip():
		raise ValueError("Name, email, and department are required")
	if salary < 0:
		raise ValueError("Salary cannot be negative")

	with sqlite3.connect(DATABASE) as connection:
		try:
			cursor: sqlite3.Cursor = connection.execute(
				"INSERT INTO employees (name, email, department, salary) "
				"VALUES (?, ?, ?, ?)",
				(name.strip(), email.strip(), department.strip(), salary),
			)
		except sqlite3.IntegrityError as error:
			raise ValueError("Email already exists") from error
	return cursor.lastrowid


if __name__ == "__main__":
	try:
		name: str = input("Enter employee name: ")
		email: str = input("Enter employee email: ")
		department: str = input("Enter department: ")
		salary = float(input("Enter salary: "))
		employee_id: int = add_employee(name, email, department, salary)
		print(f"Employee added successfully with ID {employee_id}")
	except ValueError as error:
		print(f"Could not add employee: {error}")
