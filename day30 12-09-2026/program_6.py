import sqlite3

with sqlite3.connect("students.db") as connection: 
    connection: sqlite3.Connection = connection
    for student in connection.execute(
		"SELECT * FROM students WHERE name LIKE 'A%'"):
		    print(student)
