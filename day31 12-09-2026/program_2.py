import sqlite3
from pathlib import Path

# Use the database created by Program 301.
database: Path = Path(__file__).with_name("day31_students.db")

with sqlite3.connect(database) as connection: 
    connection: sqlite3.Connection = connection
    # COUNT(*) returns the number of records in the table.
    total = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    print("Total students:", total)
