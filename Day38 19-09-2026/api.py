"""Employee API with SQLite storage."""

import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


DATABASE: Path = Path(__file__).with_name("employees.db")
app = FastAPI(title="Employee API")


class EmployeeCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=3, max_length=200)
    department: str = Field(min_length=1, max_length=100)
    salary: float = Field(ge=0)


def row_to_employee(row: sqlite3.Row) -> dict:
    return dict(row)


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Employee API is running"}


@app.get("/employees")
def get_employees() -> list[dict]:
    connection: sqlite3.Connection = sqlite3.connect(DATABASE)
    with closing(connection):
        connection.row_factory = sqlite3.Row
        rows: list[Any] = connection.execute(
            "SELECT id, name, email, department, salary "
            "FROM employees ORDER BY id"
        ).fetchall()
    return [row_to_employee(row) for row in rows]


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int) -> dict:
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
    return row_to_employee(row)


@app.post("/employees", status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate) -> dict:
    try:
        connection: sqlite3.Connection = sqlite3.connect(DATABASE)
        with closing(connection):
            cursor: sqlite3.Cursor = connection.execute(
                "INSERT INTO employees (name, email, department, salary) "
                "VALUES (?, ?, ?, ?)",
                (employee.name, employee.email, employee.department, employee.salary),
            )
            connection.commit()
            employee_id: int | None = cursor.lastrowid
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Email already exists")

    return {"id": employee_id, **employee.model_dump()}
