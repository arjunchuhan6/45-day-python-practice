# Python Program 6

import sqlite3

DATABASE_NAME = "students.db"


def delete_student() -> None:
	student_id: int = int(input("Enter student ID to delete: "))

	connection: sqlite3.Connection = sqlite3.connect(DATABASE_NAME)
	cursor: sqlite3.Cursor = connection.cursor()
	cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
	connection.commit()

	if cursor.rowcount == 0:
		print("Student not found.")
	else:
		print("Student deleted successfully.")

	connection.close()


if __name__ == "__main__":
	delete_student()
