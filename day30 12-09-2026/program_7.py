import sqlite3


with sqlite3.connect("students.db") as connection: 
    connection: sqlite3.Connection = connection
    print("Students ordered by marks:")
    for student in connection.execute("SELECT * FROM students ORDER BY marks DESC"):
        print(student)
