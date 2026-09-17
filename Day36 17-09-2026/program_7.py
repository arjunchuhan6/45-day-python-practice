# Program 7: Build a basic Student API
# Install once: python -m pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
	title="Basic Student API",
	description="A small API built with the FastAPI basics.",
	version="1.0.0",
)


class StudentCreate(BaseModel):
	name: str
	course: str


students: list[dict[str, int | str]] = [
	{"id": 1, "name": "Asha", "course": "Python"},
	{"id": 2, "name": "Rahul", "course": "FastAPI"},
]


@app.get("/")
def home() -> dict[str, str]:
	return {"message": "Welcome to the Basic Student API"}


@app.get("/about")
def about() -> dict[str, str]:
	return {"message": "This API manages student records"}


@app.get("/students")
def get_students(course: str | None = None) -> list[dict[str, int | str]]:
	if course is None:
		return students
	return [student for student in students if student["course"].lower() == course.lower()]


@app.get("/students/{student_id}")
def get_student(student_id: int) -> dict[str, int | str]:
	for student in students:
		if student["id"] == student_id:
			return student
	raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students", status_code=201)
def create_student(student: StudentCreate) -> dict[str, int | str]:
	new_student = {
		"id": len(students) + 1,
		"name": student.name,
		"course": student.course,
	}
	students.append(new_student)
	return new_student


# Run from this folder with:
# python -m uvicorn program_7:app --reload
# Open Swagger and test every route:
# http://127.0.0.1:8000/docs
# Try the query parameter: GET /students?course=Python
# Try the path parameter: GET /students/1
# Try POST /students with: {"name": "Neha", "course": "FastAPI"}

