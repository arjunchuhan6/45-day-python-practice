"""Program 8: search employees directly in SQLite."""

import sqlite3
from pathlib import Path
from typing import Any


DATABASE: Path = Path(__file__).with_name("employees.db")


def search_employees(search_text: str) -> list[dict]:
	"""Find employees by name, email, or department."""
	search_text = search_text.strip()
	if not search_text:
		raise ValueError("Search text cannot be empty")

	pattern: str = f"%{search_text}%"
	with sqlite3.connect(DATABASE) as connection:
		connection.row_factory = sqlite3.Row
		rows: list[Any] = connection.execute(
			"SELECT id, name, email, department, salary "
			"FROM employees "
			"WHERE LOWER(name) LIKE LOWER(?) "
			"OR LOWER(email) LIKE LOWER(?) "
			"OR LOWER(department) LIKE LOWER(?) "
			"ORDER BY id",
			(pattern, pattern, pattern),
		).fetchall()
	return [dict(row) for row in rows]


if __name__ == "__main__":
	try:
		search_text: str = input("Search employees: ")
		matches = search_employees(search_text)
		if not matches:
			print("No employees found")
		else:
			for employee in matches:
				print(employee)
	except ValueError as error:
		print(f"Could not search employees: {error}")
