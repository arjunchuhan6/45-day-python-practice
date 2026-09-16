# Python Program 1

import sqlite3

DATABASE_NAME = "students.db"

def create_student_table() -> None:
	connection: sqlite3.Connection = sqlite3.connect(DATABASE_NAME)
	cursor: sqlite3.Cursor = connection.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS students (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL,
			age INTEGER NOT NULL,
			course TEXT NOT NULL,
			marks REAL NOT NULL
		)
		"""
	)

	connection.commit()
	connection.close()
	print("Student table created successfully.")


if __name__ == "__main__":
	create_student_table()
# 