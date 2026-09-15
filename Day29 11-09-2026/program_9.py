"""Add a new column to the students table."""

import re
import sqlite3


column_name: str = input("Enter the new column name: ").strip()
column_type: str = input("Enter the column type (TEXT, INTEGER, REAL): ").strip().upper()
valid_types = {"TEXT", "INTEGER", "REAL"}

if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", column_name):
	print("Invalid column name.")
elif column_type not in valid_types:
	print("Invalid column type. Choose TEXT, INTEGER, or REAL.")
else:
	connection: sqlite3.Connection = sqlite3.connect("school1.db")
	cursor: sqlite3.Cursor = connection.cursor()
	cursor.execute("PRAGMA table_info(students)")
	existing_columns = {column[1] for column in cursor.fetchall()}

	if column_name in existing_columns:
		print("That column already exists.")
	else:
		# The name is validated above because SQLite cannot parameterize identifiers.
		cursor.execute(f"ALTER TABLE students ADD COLUMN {column_name} {column_type}")
		connection.commit()
		print(f"Column '{column_name}' added successfully.")

	connection.close()
