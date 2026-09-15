"""Insert multiple students into the school database."""

import sqlite3

connection = sqlite3.connect("school1.db")
cursor = connection.cursor()

students = [
    ("Bob", "Mathematics"),
    ("Charlie", "Physics"),
    ("Diana", "Computer Science"),
]

cursor.executemany(
    """
    INSERT INTO students (name, course)
    VALUES (?, ?)
    """,
    students,
)

connection.commit()

print(f"{cursor.rowcount} student records inserted")

connection.close()