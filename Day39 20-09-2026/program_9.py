"""Improved employee CRUD API backed by SQLite."""

import re
import sqlite3
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field, field_validator


DATABASE: Path = Path(__file__).with_name("employee.db")
app = FastAPI(title="Employee CRUD API", version="2.0.0")


class EmployeeInput(BaseModel):
	model_config = ConfigDict(str_strip_whitespace=True)

	name: str = Field(min_length=1, max_length=100)
	email: str = Field(min_length=3, max_length=200)
	department: str = Field(min_length=1, max_length=100)
	salary: float = Field(ge=0)

	@field_validator("email")
	@classmethod
	def validate_email(cls, value: str) -> str:
		if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", value):
			raise ValueError("Email must be valid.")
		return value.lower()


class Employee(EmployeeInput):
	id: int


def get_connection() -> sqlite3.Connection:
	connection: sqlite3.Connection = sqlite3.connect(DATABASE)
	connection.row_factory = sqlite3.Row
	return connection


def initialize_database() -> None:
	connection: sqlite3.Connection = get_connection()
	try:
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
		connection.commit()
	finally:
		connection.close()


def row_to_employee(row: sqlite3.Row | None) -> dict | None:
	return dict(row) if row is not None else None


def find_employee(employee_id: int) -> dict | None:
	connection: sqlite3.Connection = get_connection()
	try:
		row = connection.execute(
			"SELECT id, name, email, department, salary "
			"FROM employees WHERE id = ?",
			(employee_id,),
		).fetchone()
		return row_to_employee(row)
	finally:
		connection.close()


def database_error() -> HTTPException:
	return HTTPException(
		status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
		detail="Database operation failed.",
	)


initialize_database()


@app.get("/health")
def health_check() -> dict[str, str]:
	return {"status": "ok"}


@app.post("/employees", response_model=Employee, status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeInput) -> dict:
	connection: sqlite3.Connection = get_connection()
	try:
		cursor: sqlite3.Cursor = connection.execute(
			"INSERT INTO employees (name, email, department, salary) "
			"VALUES (?, ?, ?, ?)",
			(employee.name, employee.email, employee.department, employee.salary),
		)
		connection.commit()
	except sqlite3.IntegrityError:
		connection.rollback()
		raise HTTPException(status_code=409, detail="Email already exists")
	except sqlite3.Error:
		connection.rollback()
		raise database_error()
	finally:
		connection.close()
	return {"id": cursor.lastrowid, **employee.model_dump()}


@app.get("/employees", response_model=list[Employee])
def list_employees() -> list[dict]:
	connection: sqlite3.Connection = get_connection()
	try:
		rows: list[Any] = connection.execute(
			"SELECT id, name, email, department, salary "
			"FROM employees ORDER BY id"
		).fetchall()
	except sqlite3.Error:
		raise database_error()
	finally:
		connection.close()
	return [dict(row) for row in rows]


@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int) -> dict:
	try:
		employee = find_employee(employee_id)
	except sqlite3.Error:
		raise database_error()
	if employee is None:
		raise HTTPException(status_code=404, detail="Employee not found")
	return employee


@app.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: EmployeeInput) -> dict:
	connection: sqlite3.Connection = get_connection()
	try:
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
		connection.commit()
	except sqlite3.IntegrityError:
		connection.rollback()
		raise HTTPException(status_code=409, detail="Email already exists")
	except sqlite3.Error:
		connection.rollback()
		raise database_error()
	finally:
		connection.close()

	if cursor.rowcount == 0:
		raise HTTPException(status_code=404, detail="Employee not found")
	return {"id": employee_id, **employee.model_dump()}


@app.delete("/employees/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int) -> None:
	connection: sqlite3.Connection = get_connection()
	try:
		cursor: sqlite3.Cursor = connection.execute(
			"DELETE FROM employees WHERE id = ?", (employee_id,)
		)
		connection.commit()
	except sqlite3.Error:
		connection.rollback()
		raise database_error()
	finally:
		connection.close()

	if cursor.rowcount == 0:
		raise HTTPException(status_code=404, detail="Employee not found")


if __name__ == "__main__":
	import uvicorn

	uvicorn.run(app, host="127.0.0.1", port=8007)
