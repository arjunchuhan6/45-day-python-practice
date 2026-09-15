import sqlite3
from pathlib import Path

# Use the existing Day 31 database containing the students table.
database: Path = Path(__file__).with_name("day31_students.db")

with sqlite3.connect(database) as connection:
	# Create the second table.
	connection.execute("""
		CREATE TABLE IF NOT EXISTS departments (
			department TEXT PRIMARY KEY,
			manager TEXT NOT NULL
		)
	""")

	# Add department information without duplicating existing rows.
	connection.executemany(
		"INSERT OR IGNORE INTO departments VALUES (?, ?)",
		[
			("IT", "Raj"),
			("HR", "Maya"),
			("Sales", "Asha"),
			("Finance", "Vijay"),
		],
	)

	# The database now contains two tables.
	tables: sqlite3.Cursor = connection.execute("""
		SELECT name
		FROM sqlite_master
		WHERE type = 'table'
		ORDER BY name
	""")

	for table in tables:
		print(table[0])
