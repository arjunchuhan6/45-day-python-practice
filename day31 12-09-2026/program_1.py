import sqlite3
from pathlib import Path

# Store the database beside this Python file.
database: Path = Path(__file__).with_name("day31_students.db")

# Sample data: id, name, department, marks, and city.
students: list[tuple[int, str, str, int, str]] = [
	(1, "Amit", "IT", 85, "Delhi"),
	(2, "Sara", "HR", 72, "Mumbai"),
	(3, "John", "IT", 91, "Delhi"),
	(4, "Priya", "Sales", 68, "Pune"),
	(5, "Rahul", "HR", 78, "Delhi"),
	(6, "Neha", "IT", 88, "Mumbai"),
	(7, "Vikram", "Sales", 74, "Pune"),
	(8, "Anita", "Finance", 95, "Delhi"),
	(9, "Ravi", "IT", 81, "Chennai"),
	(10, "Kiran", "Finance", 89, "Mumbai"),
	(11, "Meena", "HR", 76, "Delhi"),
	(12, "Arjun", "Sales", 83, "Chennai"),
	(13, "Pooja", "Finance", 92, "Pune"),
	(14, "Sanjay", "IT", 70, "Mumbai"),
	(15, "Ritu", "HR", 86, "Chennai"),
	(16, "Manoj", "Sales", 79, "Delhi"),
	(17, "Kavita", "Finance", 90, "Mumbai"),
	(18, "Deepak", "IT", 65, "Pune"),
	(19, "Shreya", "HR", 94, "Delhi"),
	(20, "Nitin", "Sales", 71, "Chennai"),
]

with sqlite3.connect(database) as connection: 
    connection: sqlite3.Connection = connection
	# Create the five-column table if it does not exist.
    connection.execute("""
		CREATE TABLE IF NOT EXISTS students (
			id INTEGER PRIMARY KEY,
			name TEXT NOT NULL,
			department TEXT NOT NULL,
			marks INTEGER NOT NULL,
			city TEXT NOT NULL
		)
	""")

	# Insert the 20 students without duplicating existing IDs.
    connection.executemany(
		"INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?, ?)",
		students,
	)

	# GROUP BY creates one group for each department.
    rows: sqlite3.Cursor = connection.execute("""
		SELECT department, COUNT(*) AS student_count
		FROM students
		GROUP BY department
		ORDER BY department
	""")

	# Display each department and its number of students.
    for row in rows:
        print(row)