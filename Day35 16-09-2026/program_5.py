# Python Program 5

import sqlite3

DATABASE_NAME = "students.db"


def update_student() -> None:
	student_id: int = int(input("Enter student ID to update: "))
	name: str = input("Enter new student name: ")
	age: int = int(input("Enter new student age: "))
	course: str = input("Enter new student course: ")
	marks: float = float(input("Enter new student marks: "))

	connection: sqlite3.Connection = sqlite3.connect(DATABASE_NAME)
	cursor: sqlite3.Cursor = connection.cursor()
	cursor.execute(
		"""
		UPDATE students
		SET name = ?, age = ?, course = ?, marks = ?
		WHERE id = ?
		""",
		(name, age, course, marks, student_id),
	)
	connection.commit()

	if cursor.rowcount == 0:
		print("Student not found.")
	else:
		print("Student updated successfully.")

	connection.close()


if __name__ == "__main__":
	update_student()
