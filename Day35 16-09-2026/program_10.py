import sqlite3

DATABASE_NAME = "student_management.db"
COURSES = ["Python", "Java", "SQL", "Web Development", "Data Science"]


def create_student_table():
	with sqlite3.connect(DATABASE_NAME) as connection:
		connection.execute(
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


def seed_students():
	with sqlite3.connect(DATABASE_NAME) as connection:
		student_count = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
		if student_count != 0:
			return
		students = []
		for student_number in range(500):
			students.append(
				(
					"Aarav Sharma" if student_number == 0 else f"Student {student_number + 1}",
					18 + student_number % 13,
					COURSES[student_number % len(COURSES)],
					250 + (student_number * 17) % 251,
				)
			)
		connection.executemany(
			"INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
			students,
		)
		print("New database created with 500 students.")


def update_first_student_name():
	with sqlite3.connect(DATABASE_NAME) as connection:
		connection.execute(
			"UPDATE students SET name = ? WHERE id = ?",
			("Aarav Sharma", 1),
		)


def get_text(prompt):
	while True:
		value = input(prompt).strip()
		if value:
			return value
		print("This field cannot be empty.")


def get_age():
	while True:
		try:
			age = int(input("Enter age: "))
			if 8 <= age <= 30:
				return age
			print("Age must be between 8 and 30.")
		except ValueError:
			print("Age must be a whole number.")


def get_marks():
	while True:
		try:
			marks = float(input("Enter marks: "))
			if 0 <= marks <= 500:
				return marks
			print("Marks must be between 0 and 500.")
		except ValueError:
			print("Marks must be a number.")


def add_student():
	try:
		with sqlite3.connect(DATABASE_NAME) as connection:
			next_id = connection.execute(
				"SELECT COALESCE(MAX(id), 0) + 1 FROM students"
			).fetchone()[0]
			student = (
				f"Student {next_id}",
				get_age(),
				get_text("Enter course: "),
				get_marks(),
			)
			connection.execute(
				"INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
				student,
			)
		print("Student added successfully.")
	except sqlite3.Error:
		print("Database error occurred.")


def display_students(students):
	for student_id, name, age, course, marks in students:
		print(f"{student_id}: {name} | Age: {age} | {course} | Marks: {marks:.2f}")


def view_students():
	try:
		with sqlite3.connect(DATABASE_NAME) as connection:
			students = connection.execute(
				"SELECT id, name, age, course, marks FROM students ORDER BY id"
			).fetchall()
		if students:
			display_students(students)
	except sqlite3.Error:
		print("Database error occurred.")


def search_student():
	search_name = get_text("Enter name to search: ")
	try:
		with sqlite3.connect(DATABASE_NAME) as connection:
			students = connection.execute(
				"SELECT id, name, age, course, marks FROM students WHERE name LIKE ? ORDER BY name",
				(f"%{search_name}%",),
			).fetchall()
		if students:
			display_students(students)
		else:
			print("No matching students found.")
	except sqlite3.Error:
		print("Database error occurred.")


def update_student():
	try:
		student_id = int(input("Enter student ID to update: "))
		student = (
			get_text("Enter new name: "),
			get_age(),
			get_text("Enter new course: "),
			get_marks(),
			student_id,
		)
		with sqlite3.connect(DATABASE_NAME) as connection:
			cursor = connection.execute(
				"UPDATE students SET name = ?, age = ?, course = ?, marks = ? WHERE id = ?",
				student,
			)
		print("Student updated successfully." if cursor.rowcount else "Student not found.")
	except ValueError:
		print("Student ID must be a whole number.")
	except sqlite3.Error:
		print("Database error occurred.")


def delete_student():
	try:
		student_id = int(input("Enter student ID to delete: "))
		with sqlite3.connect(DATABASE_NAME) as connection:
			cursor = connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
		print("Student deleted successfully." if cursor.rowcount else "Student not found.")
	except ValueError:
		print("Student ID must be a whole number.")
	except sqlite3.Error:
		print("Database error occurred.")


def calculate_average_marks():
	try:
		with sqlite3.connect(DATABASE_NAME) as connection:
			average_marks = connection.execute("SELECT AVG(marks) FROM students").fetchone()[0]
		print("No marks available." if average_marks is None else f"Average marks: {average_marks:.2f}")
	except sqlite3.Error:
		print("Database error occurred.")


def main():
	create_student_table()
	seed_students()
	update_first_student_name()
	while True:
		print(
			"\n1. Add student\n2. View students\n3. Search student\n"
			"4. Update student\n5. Delete student\n6. Calculate average marks\n0. Exit"
		)
		choice = input("Enter your choice: ").strip()
		try:
			if choice == "1":
				add_student()
			elif choice == "2":
				view_students()
			elif choice == "3":
				search_student()
			elif choice == "4":
				update_student()
			elif choice == "5":
				delete_student()
			elif choice == "6":
				calculate_average_marks()
			elif choice == "0":
				print("Goodbye.")
				break
			else:
				print("Invalid choice.")
		except KeyboardInterrupt:
			print("\nOperation cancelled.")


if __name__ == "__main__":
	main()
