import sqlite3
from pathlib import Path

 # Use the existing Day 31 database.
database: Path = Path(__file__).with_name("day31_students.db")

# SUM(marks) calculates the total of all marks.
with sqlite3.connect(database) as connection: 
    connection: sqlite3.Connection = connection
    total_marks = connection.execute(
		"SELECT SUM(marks) FROM students"
	).fetchone()[0]
	# Display the total marks.
    print("Total marks:", total_marks)
