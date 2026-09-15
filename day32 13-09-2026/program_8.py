#use parameterized query to prevent sql injection in sqlite database using python only
import sqlite3

connection: sqlite3.Connection = sqlite3.connect("students.db")
cursor: sqlite3.Cursor = connection.cursor()

# Use parameterized query to prevent SQL injection
name = "Arjun Mehta"
cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
result = cursor.fetchall()
print("Search results:", result)

connection.close()