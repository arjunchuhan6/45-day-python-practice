import sqlite3
from pathlib import Path

# Use the existing Day 31 database.
database: Path = Path(__file__).with_name("day31_students.db")

queries: list[tuple[str, str]] = [
	("1. Students scoring above 85", """
		SELECT name, marks FROM students WHERE marks > 85
	"""),
	("2. Top five students", """
		SELECT name, marks FROM students ORDER BY marks DESC LIMIT 5
	"""),
	("3. Number of students", """
		SELECT COUNT(*) FROM students
	"""),
	("4. Total marks", """
		SELECT SUM(marks) FROM students
	"""),
	("5. Average marks by department", """
		SELECT department, AVG(marks) FROM students GROUP BY department
	"""),
	("6. Lowest and highest marks", """
		SELECT MIN(marks), MAX(marks) FROM students
	"""),
	("7. Students from Delhi", """
		SELECT name FROM students WHERE city = 'Delhi'
	"""),
	("8. Students with above-average marks", """
		SELECT name, marks FROM students
		WHERE marks > (SELECT AVG(marks) FROM students)
	"""),
	("9. Students and managers", """
		SELECT s.name, d.manager
		FROM students AS s
		INNER JOIN departments AS d ON s.department = d.department
	"""),
	("10. Department student counts", """
		SELECT department, COUNT(*) FROM students GROUP BY department
	"""),
]

with sqlite3.connect(database) as connection: 
	for title, query in queries:
		print(f"\n{title}")
		for row in connection.execute(query):
			print(row)
