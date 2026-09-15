import sqlite3
from pathlib import Path

# Use the existing Day 31 database.
database = Path(__file__).with_name("day31_students.db")

with sqlite3.connect(database) as connection:
	# MIN(marks) returns the lowest mark.
	lowest_marks = connection.execute(
		"SELECT MIN(marks) FROM students"
	).fetchone()[0]
	print("Lowest marks:", lowest_marks)
