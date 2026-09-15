import sqlite3

with sqlite3.connect("students.db") as connection: 
    connection: sqlite3.Connection = connection
    total = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    print("Total students:", total)
