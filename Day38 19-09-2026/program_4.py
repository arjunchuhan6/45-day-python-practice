"""Program 4: delete an employee with a DELETE endpoint."""

import sqlite3
from contextlib import closing
from pathlib import Path

from fastapi import FastAPI, HTTPException, status


DATABASE: Path = Path(__file__).with_name("employees.db")
app = FastAPI(title="Employee DELETE API")


@app.delete(
	"/employees/{employee_id}",
	status_code=status.HTTP_204_NO_CONTENT,
)
def delete_employee(employee_id: int) -> None:
	"""Delete one employee from the SQLite database."""
	connection: sqlite3.Connection = sqlite3.connect(DATABASE)
	with closing(connection):
		cursor: sqlite3.Cursor = connection.execute(
			"DELETE FROM employees WHERE id = ?",
			(employee_id,),
		)
		connection.commit()

	if cursor.rowcount == 0:
		raise HTTPException(status_code=404, detail="Employee not found")


if __name__ == "__main__":
	import uvicorn

	uvicorn.run(app, host="127.0.0.1", port=8003)
