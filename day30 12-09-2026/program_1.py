import sqlite3


connection: sqlite3.Connection = sqlite3.connect("students.db")
cursor: sqlite3.Cursor = connection.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS students (
		id INTEGER PRIMARY KEY,
		name TEXT NOT NULL,
		marks INTEGER NOT NULL
	)
""")

students: list[tuple[int, str, int]] = [
	(1, "Amit", 85),
	(2, "Sara", 72),
	(3, "John", 91),
]
cursor.executemany("INSERT OR IGNORE INTO students VALUES (?, ?, ?)", students)
connection.commit()

cursor.execute("SELECT * FROM students WHERE marks > 80")

print("Students with marks greater than 80:")
for student in cursor.fetchall():
	print(student)

connection.close()
