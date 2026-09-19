"""Program 2: read employees with GET endpoints."""

import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException


DATABASE: Path = Path(__file__).with_name("employees.db")
app = FastAPI(title="Employee GET API")


@app.get("/employees")
def get_employees() -> list[dict]:
	"""Return all employees from the SQLite database."""
	connection: sqlite3.Connection = sqlite3.connect(DATABASE)
	with closing(connection):
		connection.row_factory = sqlite3.Row
		rows: list[Any] = connection.execute(
			"SELECT id, name, email, department, salary "
			"FROM employees ORDER BY id"
		).fetchall()
	return [dict(row) for row in rows]


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int) -> dict:
	"""Return one employee by ID."""
	connection: sqlite3.Connection = sqlite3.connect(DATABASE)
	with closing(connection):
		connection.row_factory = sqlite3.Row
		row = connection.execute(
			"SELECT id, name, email, department, salary "
			"FROM employees WHERE id = ?",
			(employee_id,),
		).fetchone()

	if row is None:
		raise HTTPException(status_code=404, detail="Employee not found")
	return dict(row)


if __name__ == "__main__":
	import uvicorn

	uvicorn.run(app, host="127.0.0.1", port=8001)