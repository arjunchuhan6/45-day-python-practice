# Python Program 8

import sqlite3

DATABASE_NAME = "students.db"


def get_valid_text(prompt: str) -> str:
	while True:
		value: str = input(prompt).strip()
		if value:
			return value
		print("This field cannot be empty.")


def get_valid_age() -> int:
	while True:
		age_text: str = input("Enter student age: ").strip()
		if age_text.isdigit() and 8<= int(age_text) <= 30:
			return int(age_text)
		print("Age must be a whole number between 8 and 30.")


def get_valid_marks() -> float:
	while True:
		marks_text: str = input("Enter student marks: ").strip()
		try:
			marks: float = float(marks_text)
		except ValueError:
			print("Marks must be a number between 0 and 500.")
			continue

		if 0 <= marks <= 500:
			return marks
		print("Marks must be a number between 0 and 500.")


def add_student_with_validation() -> None:
	name: str = get_valid_text("Enter student name: ")
	age: int = get_valid_age()
	course: str = get_valid_text("Enter student course: ")
	marks: float = get_valid_marks()

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
	add_student_with_validation()
