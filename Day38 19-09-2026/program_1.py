"""Program 1: create an employee with a POST endpoint."""

import sqlite3
from contextlib import closing
from pathlib import Path

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


DATABASE: Path = Path(__file__).with_name("employees.db")
app = FastAPI(title="Employee POST API")


class EmployeeCreate(BaseModel):
	name: str = Field(min_length=1, max_length=100)
	email: str = Field(min_length=3, max_length=200)
	department: str = Field(min_length=1, max_length=100)
	salary: float = Field(ge=0)


@app.post("/employees", status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate) -> dict:
	"""Insert one employee into the SQLite database."""
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

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
