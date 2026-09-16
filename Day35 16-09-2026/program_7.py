# Python Program 7

import sqlite3

DATABASE_NAME = "students.db"


def calculate_average_marks() -> None:
	connection: sqlite3.Connection = sqlite3.connect(DATABASE_NAME)
	cursor: sqlite3.Cursor = connection.cursor()
	cursor.execute("SELECT AVG(marks) FROM students")
	average_marks: float | None = cursor.fetchone()[0]
	connection.close()

	if average_marks is None:
		print("No marks available.")
	else:
		print(f"Average marks: {average_marks:.2f}")


if __name__ == "__main__":
	calculate_average_marks()
