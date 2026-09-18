"""FastAPI example for returning multiple students."""

import fastapi
import uvicorn

app = fastapi.FastAPI()

students = [
	{"student_id": 1, "name": "Aarav", "course": "Python"},
	{"student_id": 2, "name": "Diya", "course": "FastAPI"},
	{"student_id": 3, "name": "Kabir", "course": "Python"},
	{"student_id": 4, "name": "Anaya", "course": "Django"},
]


@app.get("/students")
def get_students(course: str | None = None, limit: int | None = None):
	"""Return multiple students with optional course filtering and result limit."""
	selected_students = students

	if course is not None:
		selected_students = [
			student
			for student in students
			if student["course"].lower() == course.lower()
		]

	if limit is not None:
		if limit < 1:
			raise fastapi.HTTPException(
				status_code=400,
				detail="limit must be greater than 0",
			)
		selected_students = selected_students[:limit]

	return {"count": len(selected_students), "students": selected_students}


if __name__ == "__main__":
	uvicorn.run(app, host="127.0.0.1", port=8000)
