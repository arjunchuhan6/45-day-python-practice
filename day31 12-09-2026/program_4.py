import sqlite3
from pathlib import Path

# Use the existing Day 31 database.
database: Path = Path(__file__).with_name("day31_students.db")

with sqlite3.connect(database) as connection:
	# AVG(marks) calculates the average marks.
	average_marks = connection.execute(
		"SELECT AVG(marks) FROM students"
	).fetchone()[0]
	print("Average marks:", average_marks)
