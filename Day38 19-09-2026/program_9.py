"""Program 9: delete an employee directly from SQLite."""

import sqlite3
from pathlib import Path


DATABASE: Path = Path(__file__).with_name("employees.db")


def delete_employee(employee_id: int) -> None:
	"""Delete one employee by ID without using an API endpoint."""
	with sqlite3.connect(DATABASE) as connection:
		cursor: sqlite3.Cursor = connection.execute(
			"DELETE FROM employees WHERE id = ?",
			(employee_id,),
		)
		if cursor.rowcount == 0:
			raise ValueError("Employee not found")


if __name__ == "__main__":
	try:
		employee_id = int(input("Enter employee ID to delete: "))
		delete_employee(employee_id)
		print("Employee deleted successfully")
	except ValueError as error:
		print(f"Could not delete employee: {error}")
