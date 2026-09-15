"""Update one student record in the school database."""

import sqlite3
try:
	student_id: int = int(input("Enter the student id to update: "))
	new_name: str = input("Enter the new name: ")
	new_age: int = int(input("Enter the new age: "))
	new_course: str = input("Enter the new course: ")
except ValueError:
	print("Student id and age must be numbers.")
else:
	connection: sqlite3.Connection = sqlite3.connect("school1.db")
	cursor: sqlite3.Cursor = connection.cursor()

	# Parameters keep user input separate from the SQL command.
	cursor.execute(
		"""
		UPDATE students
		SET name = ?, age = ?, course = ?
		WHERE id = ?
		""",
		(new_name, new_age, new_course, student_id),
	)
	connection.commit()

	if cursor.rowcount == 0:
		print("No student found with that id.")
	else:
		print("Student record updated successfully.")

	connection.close()
