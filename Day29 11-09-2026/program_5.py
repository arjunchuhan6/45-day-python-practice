"""Select and display all student records from the school database."""

import sqlite3
from typing import Any


connection: sqlite3.Connection = sqlite3.connect("school1.db")
cursor: sqlite3.Cursor = connection.cursor()

cursor.execute("SELECT * FROM students")
student_records: list[Any] = cursor.fetchall()

for student in student_records:
	print(student)

connection.close()
