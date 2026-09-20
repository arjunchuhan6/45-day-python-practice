import sqlite3
from pathlib import Path


DATABASE_FILE: Path = Path(__file__).with_name("registrations.db")


class DatabaseError(Exception):
	"""Raised when registration data cannot be saved."""


def save_registration(registration) -> None:
	try:
		with sqlite3.connect(DATABASE_FILE) as connection:
			connection.execute(
				"""
				CREATE TABLE IF NOT EXISTS registrations (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					name TEXT NOT NULL,
					email TEXT NOT NULL UNIQUE
				)
				"""
			)
			connection.execute(
				"INSERT INTO registrations (name, email) VALUES (?, ?)",
				(registration["name"], registration["email"]),
			)
	except (sqlite3.Error, KeyError) as error: 
		raise DatabaseError("Could not save registration data.") from error


def create_registration(registration):
	try:
		save_registration(registration)
		return {"valid": True, "message": "Registration saved."}, 201
	except DatabaseError as error:
		return {"valid": False, "error": str(error)}, 500


if __name__ == "__main__":
	registration: dict[str, str] = {
		"name": input("Enter your name: "),
		"email": input("Enter your email: "),
	}
	response, status_code = create_registration(registration)
	print({"status_code": status_code, "response": response})
