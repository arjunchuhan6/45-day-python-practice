#search data in sqlite database using python only search data
import sqlite3
connection: sqlite3.Connection = sqlite3.connect("students.db")
cursor: sqlite3.Cursor = connection.cursor()

# Search data in the students table
cursor.execute("SELECT * FROM students WHERE name = ?", ("Arjun Mehta",))
result = cursor.fetchall()
print("Search results:", result)

connection.close()