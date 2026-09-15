"""Insert student records into the school database."""

import sqlite3

connection = sqlite3.connect("school1.db")
cursor = connection.cursor()

students = [
    ("Alice", 20, "Python"),
    ("Bob", 22, "SQL"),
    ("Charlie", 21, "Java"),
]

cursor.executemany(
    """
    INSERT INTO students (name, age, course)
    VALUES (?, ?, ?)
    """,
    students,
)

connection.commit()
connection.close()

print("Students inserted successfully")