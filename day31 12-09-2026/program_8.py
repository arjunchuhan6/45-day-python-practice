import sqlite3
from pathlib import Path

# Use the existing Day 31 database.
database: Path = Path(__file__).with_name("day31_students.db")

with sqlite3.connect(database) as connection:
	# INNER JOIN returns students with a matching department manager.
	rows: sqlite3.Cursor = connection.execute("""
		SELECT students.name, students.department, departments.manager
		FROM students
		INNER JOIN departments
			ON students.department = departments.department
		ORDER BY students.name
	""")

	for row in rows:
		print(row)
