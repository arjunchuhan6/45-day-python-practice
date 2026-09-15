import sqlite3

with sqlite3.connect("students.db") as connection: 
    connection: sqlite3.Connection = connection
    print("First two records from the students table:")
    for student in connection.execute("SELECT * FROM students LIMIT 2"):
        print(student)
