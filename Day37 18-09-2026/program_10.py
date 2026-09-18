"""Student search API using FastAPI query parameters."""

import fastapi
import uvicorn

app = fastapi.FastAPI()

students = [
	{"student_id": 1, "name": "Aarav", "course": "Python"},
	{"student_id": 2, "name": "Diya", "course": "FastAPI"},
	{"student_id": 3, "name": "Kabir", "course": "Python"},
	{"student_id": 4, "name": "Anaya", "course": "Django"},
]


@app.get("/students/search")
def search_students(
	name: str | None = None,
	course: str | None = None,
	limit: int = 10,
):
	"""Search students by name or course and optionally limit the results."""
	if limit < 1:
		raise fastapi.HTTPException(
			status_code=400,
			detail="limit must be greater than 0",
		)

	search_name: str | None = name.strip().lower() if name else None
	search_course: str | None = course.strip().lower() if course else None

	results = [
		student
		for student in students
		if (search_name is None or search_name in student["name"].lower())
		and (search_course is None or search_course in student["course"].lower())
	][:limit]

	return {"count": len(results), "students": results}


if __name__ == "__main__":
	uvicorn.run(app, host="127.0.0.1", port=8000)
