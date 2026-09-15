"""Select specific student columns based on client input."""

import sqlite3
from typing import Any


available_columns: set[str] = {"id", "name", "age", "course"}
requested_columns: str = input(
	"Enter columns to display, separated by commas "
	"(id, name, age, course): "
)
selected_columns: list[str] = [column.strip() for column in requested_columns.split(",")]

if not selected_columns or any(column not in available_columns for column in selected_columns):
	print("Invalid column. Choose only: id, name, age, course")
else:
	connection: sqlite3.Connection = sqlite3.connect("school1.db")
	cursor: sqlite3.Cursor = connection.cursor()

	# Column names cannot be SQL parameters, so validate them before building the query.
	query: str = f"SELECT {', '.join(selected_columns)} FROM students"
	cursor.execute(query)
	student_records: list[Any] = cursor.fetchall()

	for student in student_records:
		print(student)

	connection.close()
