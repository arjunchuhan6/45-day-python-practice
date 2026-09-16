# Python Program 3

import sqlite3

DATABASE_NAME = "students.db"


def view_students() -> None:
	connection: sqlite3.Connection = sqlite3.connect(DATABASE_NAME)
	cursor: sqlite3.Cursor = connection.cursor()
	cursor.execute("SELECT id, name, age, course, marks FROM students")
	students: list[tuple[int, str, int, str, float]] = cursor.fetchall()
	connection.close()

	if not students:
		print("No students found.")
		return

	for student in students:
		student_id, name, age, course, marks = student
		print(
			f"ID: {student_id}, Name: {name}, Age: {age}, "
			f"Course: {course}, Marks: {marks}"
		)


if __name__ == "__main__":
	view_students()
