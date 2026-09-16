# Python Program 2

import sqlite3

DATABASE_NAME = "students.db"


def add_student() -> None:
	name: str = input("Enter student name: ")
	age: int = int(input("Enter student age: "))
	course: str = input("Enter student course: ")
	marks: float = float(input("Enter student marks: "))

	connection: sqlite3.Connection = sqlite3.connect(DATABASE_NAME)
	cursor: sqlite3.Cursor = connection.cursor()
	cursor.execute(
		"INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
		(name, age, course, marks),
	)
	connection.commit()
	connection.close()
	print("Student added successfully.")


if __name__ == "__main__":
	add_student()
