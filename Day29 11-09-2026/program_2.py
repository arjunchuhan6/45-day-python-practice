"""
SQL WITH PYTHON - PROGRAM 2
Create a table in the school database.
"""

# Import sqlite3 so Python can work with the SQLite database.
import sqlite3


# Open the database created in Program 1.
connection: sqlite3.Connection = sqlite3.connect("school1.db")

# cursor() allows us to send SQL commands to the database.
cursor: sqlite3.Cursor = connection.cursor()

# CREATE TABLE makes a new students table.
# IF NOT EXISTS prevents an error if the table already exists.
cursor.execute("""
	CREATE TABLE IF NOT EXISTS students(
		id INTEGER PRIMARY KEY,
		name TEXT NOT NULL,
		age INTEGER,
		course TEXT
	)
""")

# commit() saves the table creation in the database file.
connection.commit()

# close() closes the database connection.
connection.close()

print("students table created successfully")
