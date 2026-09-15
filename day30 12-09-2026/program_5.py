import sqlite3

with sqlite3.connect("students.db") as connection: 
    connection: sqlite3.Connection = connection
    for student in connection.execute(
		"SELECT * FROM students WHERE marks BETWEEN 70 AND 90"
	):
		    print(student)
