#insert data into database using sqlite database using python only insert data
import sqlite3
connection: sqlite3.Connection = sqlite3.connect("students.db")
cursor: sqlite3.Cursor = connection.cursor()

# Insert data into the students table
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Alice", 20, "A"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Bob", 22, "B"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Charlie", 21, "A"))

connection.commit()
print("Data inserted successfully.")
connection.close()