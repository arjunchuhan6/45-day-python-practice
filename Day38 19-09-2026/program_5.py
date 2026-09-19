"""Program 5: connect FastAPI to the employee SQLite database."""

import sqlite3
from contextlib import closing
from pathlib import Path

from fastapi import FastAPI


DATABASE: Path = Path(__file__).with_name("employees.db")
app = FastAPI(title="Employee SQLite Connection API")


def get_database_status() -> dict[str, int | str | bool]:
	"""Open SQLite, read the employee count, and close the connection."""
	connection: sqlite3.Connection = sqlite3.connect(DATABASE)
	with closing(connection):
		employee_count: int = connection.execute(
			"SELECT COUNT(*) FROM employees"
		).fetchone()[0]
	return {
		"connected": True,
		"database": DATABASE.name,
		"employee_count": employee_count,
	}


@app.get("/database-status")
def database_status() -> dict[str, int | str | bool]:
	return get_database_status()


if __name__ == "__main__":
	import uvicorn

	uvicorn.run(app, host="127.0.0.1", port=8004)
