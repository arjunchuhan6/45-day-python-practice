"""Program 3: update an employee with a PUT endpoint."""

import sqlite3
from contextlib import closing
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


DATABASE: Path = Path(__file__).with_name("employees.db")
app = FastAPI(title="Employee PUT API")


class EmployeeUpdate(BaseModel):
	name: str = Field(min_length=1, max_length=100)
	email: str = Field(min_length=3, max_length=200)
	department: str = Field(min_length=1, max_length=100)
	salary: float = Field(ge=0)


@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeUpdate) -> dict:
	"""Update one employee in the SQLite database."""
	try:
		connection: sqlite3.Connection = sqlite3.connect(DATABASE)
		with closing(connection):
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
		raise HTTPException(status_code=409, detail="Email already exists")

	if cursor.rowcount == 0:
		raise HTTPException(status_code=404, detail="Employee not found")
	return {"id": employee_id, **employee.model_dump()}


if __name__ == "__main__":
	import uvicorn

	uvicorn.run(app, host="127.0.0.1", port=8002)
