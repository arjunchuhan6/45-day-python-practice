import sqlite3
from pathlib import Path

# Use the existing Day 31 database.
database: Path = Path(__file__).with_name("day31_students.db")

with sqlite3.connect(database) as connection: 
	# MAX(marks) returns the highest mark.
	highest_marks = connection.execute(
		"SELECT MAX(marks) FROM students"
	).fetchone()[0]
	print("Highest marks:", highest_marks)
