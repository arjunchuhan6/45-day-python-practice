"""FastAPI example for handling missing student data."""

import fastapi
import uvicorn
from pydantic import BaseModel

app = fastapi.FastAPI()


class Student(BaseModel):
	student_id: int
	name: str
	course: str


@app.post("/add")
def add_student(student: Student):
	"""Accept a student only when all required fields are provided."""
	return {
		"message": "Student data received successfully",
		"student": student.model_dump(),
	}


if __name__ == "__main__":
	uvicorn.run(app, host="127.0.0.1", port=8000)
