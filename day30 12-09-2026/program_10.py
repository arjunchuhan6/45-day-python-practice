import sqlite3

with sqlite3.connect("students.db") as connection: 
    connection: sqlite3.Connection = connection
    average = connection.execute("SELECT AVG(marks) FROM students").fetchone()[0]
    print("Average marks:", average)
