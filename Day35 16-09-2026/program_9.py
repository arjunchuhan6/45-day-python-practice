# Python Program 9

import sqlite3

DATABASE_NAME = "students.db"


def add_student_with_error_handling() -> None:
	connection: sqlite3.Connection | None = None

	try:
		name: str = input("Enter student name: ").strip()
		age: int = int(input("Enter student age: "))
		course: str = input("Enter student course: ").strip()
		marks: float = float(input("Enter student marks: "))

		connection = sqlite3.connect(DATABASE_NAME)
		cursor: sqlite3.Cursor = connection.cursor()
		cursor.execute(
			"INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
			(name, age, course, marks),
		)
		connection.commit()
		print("Student added successfully.")
	except ValueError:
		print("Age must be an integer and marks must be a number.")
	except sqlite3.Error:
		print("Database error occurred.")
	finally:
		if connection is not None:
			connection.close()


if __name__ == "__main__":
	add_student_with_error_handling()
