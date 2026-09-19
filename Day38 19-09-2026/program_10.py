"""Complete employee CRUD API backed by SQLite."""

import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


DATABASE: Path = Path(__file__).with_name("employees.db")
app = FastAPI(title="Employee CRUD API", version="1.0.0")


class EmployeeInput(BaseModel):
	name: str = Field(min_length=1, max_length=100)
	email: str = Field(min_length=3, max_length=200)
	department: str = Field(min_length=1, max_length=100)
	salary: float = Field(ge=0)


def initialize_database() -> None:
	"""Create the employee table when the database is new."""
	connection: sqlite3.Connection = sqlite3.connect(DATABASE)
	with connection:
		connection.execute(
			"""
			CREATE TABLE IF NOT EXISTS employees (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT NOT NULL,
				email TEXT NOT NULL UNIQUE,
				department TEXT NOT NULL,
				salary REAL NOT NULL CHECK (salary >= 0)
			)
			"""
		)


def get_employee_row(employee_id: int) -> dict | None:
	connection: sqlite3.Connection = sqlite3.connect(DATABASE)
	with closing(connection):
		connection.row_factory = sqlite3.Row
		row = connection.execute(
			"SELECT id, name, email, department, salary "
			"FROM employees WHERE id = ?",
			(employee_id,),
		).fetchone()
	return dict(row) if row is not None else None


initialize_database()


@app.post("/employees", status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeInput) -> dict:
	try:
		connection: sqlite3.Connection = sqlite3.connect(DATABASE)
		with connection:
			cursor: sqlite3.Cursor = connection.execute(
				"INSERT INTO employees (name, email, department, salary) "
				"VALUES (?, ?, ?, ?)",
				(employee.name, employee.email, employee.department, employee.salary),
			)
	except sqlite3.IntegrityError:
		raise HTTPException(status_code=409, detail="Email already exists")

	return {"id": cursor.lastrowid, **employee.model_dump()}


@app.get("/employees")
def list_employees() -> list[dict]:
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
	employee = get_employee_row(employee_id)
	if employee is None:
		raise HTTPException(status_code=404, detail="Employee not found")
	return employee


@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeInput) -> dict:
	try:
		connection: sqlite3.Connection = sqlite3.connect(DATABASE)
		with connection:
			cursor: sqlite3.Cursor = connection.execute(
				"UPDATE employees SET name = ?, email = ?, department = ?, salary = ? "
				"WHERE id = ?",
				(
					employee.name,
					employee.email,
					employee.department,
					employee.salary,
					employee_id,
				),
			)
	except sqlite3.IntegrityError:
		raise HTTPException(status_code=409, detail="Email already exists")

	if cursor.rowcount == 0:
		raise HTTPException(status_code=404, detail="Employee not found")
	return {"id": employee_id, **employee.model_dump()}


@app.delete("/employees/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int) -> None:
	connection: sqlite3.Connection = sqlite3.connect(DATABASE)
	with connection:
		cursor: sqlite3.Cursor = connection.execute(
			"DELETE FROM employees WHERE id = ?",
			(employee_id,),
		)

	if cursor.rowcount == 0:
		raise HTTPException(status_code=404, detail="Employee not found")


if __name__ == "__main__":
	import uvicorn

	uvicorn.run(app, host="127.0.0.1", port=8006)
