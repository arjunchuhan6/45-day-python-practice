"""Delete a table from the school database."""

import re
import sqlite3


table_name: str = input("Enter the table name to delete: ").strip()

if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", table_name):
	print("Invalid table name.")
else:
	connection: sqlite3.Connection = sqlite3.connect("school1.db")
	cursor: sqlite3.Cursor = connection.cursor()
	cursor.execute(
		"SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = ?",
		(table_name,),
	)

	if cursor.fetchone() is None:
		print("That table does not exist.")
	else:
		confirmation: str = input(
			f"Delete table '{table_name}' and all its records? (yes/no): "
		).strip().lower()

		if confirmation != "yes":
			print("Table deletion cancelled.")
		else:
			# The table name is validated before it is placed in the SQL command.
			cursor.execute(f"DROP TABLE {table_name}")
			connection.commit()
			print(f"Table '{table_name}' deleted successfully.")

	connection.close()
