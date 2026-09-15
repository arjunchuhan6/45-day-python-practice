"""Delete one student record from the school database."""

import sqlite3


try:
	student_id: int = int(input("Enter the student id to delete: "))
except ValueError:
	print("Student id must be a number.")
else:
	confirmation: str = input("Delete this record? (yes/no): ").strip().lower()

	if confirmation != "yes":
		print("Delete cancelled.")
	else:
		connection: sqlite3.Connection = sqlite3.connect("school1.db")
		cursor: sqlite3.Cursor = connection.cursor()

		# Use a parameter so the client input is treated as data, not SQL code.
		cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
		connection.commit()

		if cursor.rowcount == 0:
			print("No student found with that id.")
		else:
			print("Student record deleted successfully.")

		connection.close()
