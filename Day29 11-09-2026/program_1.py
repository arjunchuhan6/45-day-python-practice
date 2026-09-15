"""
SQL WITH PYTHON - PROGRAM 1
Create a database using Python.
"""
# Import sqlite3 so Python can work with SQLite databases.
import sqlite3
# This is the name of the database file that will be created.
database_name = "school1.db"

# connect() creates school.db if it does not already exist.
# It also opens the database so we can run SQL commands on it.
connection: sqlite3.Connection = sqlite3.connect(database_name)

# close() closes the connection after we finish working with the database.
connection.close()

# Display a message so we know that the program worked.
print(f"Database '{database_name}' created successfully")
