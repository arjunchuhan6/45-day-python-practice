"""Program 7: update an employee directly in SQLite."""

import sqlite3
from pathlib import Path


DATABASE: Path = Path(__file__).with_name("employees.db")


def update_employee(
	employee_id: int,
	name: str,
	email: str,
	department: str,
	salary: float,
) -> None:
	"""Update one employee by ID without using an API endpoint."""
	if not name.strip() or not email.strip() or not department.strip():
		raise ValueError("Name, email, and department are required")
	if salary < 0:
		raise ValueError("Salary cannot be negative")

	with sqlite3.connect(DATABASE) as connection:
		try:
			cursor: sqlite3.Cursor = connection.execute(
				"UPDATE employees SET name = ?, email = ?, department = ?, salary = ? "
				"WHERE id = ?",
				(name.strip(), email.strip(), department.strip(), salary, employee_id),
			)
		except sqlite3.IntegrityError as error:
			raise ValueError("Email already exists") from error

		if cursor.rowcount == 0:
			raise ValueError("Employee not found")


if __name__ == "__main__":
	try:
		employee_id = int(input("Enter employee ID: "))
		name: str = input("Enter new employee name: ")
		email: str = input("Enter new employee email: ")
		department: str = input("Enter new department: ")
		salary = float(input("Enter new salary: "))
		update_employee(employee_id, name, email, department, salary)
		print("Employee updated successfully")
	except ValueError as error:
         print(f"Could not update employee: {error}")
