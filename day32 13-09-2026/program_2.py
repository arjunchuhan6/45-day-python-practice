#create table using sqlite database using python only create data
import sqlite3
connection: sqlite3.Connection = sqlite3.connect("students.db")
cursor: sqlite3.Cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL)''')
connection.commit()
print("Table created successfully.")
connection.close()