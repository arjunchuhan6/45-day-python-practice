#update data sqlite database using python only update data
import sqlite3
connection: sqlite3.Connection = sqlite3.connect("students.db")
cursor: sqlite3.Cursor = connection.cursor()
# Update data in the students table
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("A+", "Bob"))
connection.commit()
print("Data updated successfully.")
connection.close()