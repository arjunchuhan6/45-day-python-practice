# Program 4: Return JSON responses
# Install once: python -m pip install fastapi uvicorn

from fastapi import FastAPI


app = FastAPI(title="JSON Response API")


@app.get("/")
def home() -> dict[str, str]:
	return {"message": "This response is automatically returned as JSON"}


@app.get("/student")
def get_student() -> dict[str, int | str]:
	return {"id": 1, "name": "Asha", "course": "Python"}


@app.get("/students")
def get_students() -> list[dict[str, int | str]]:
	return [
		{"id": 1, "name": "Asha"},
		{"id": 2, "name": "Rahul"},
	]


# Run from this folder with:
# python -m uvicorn program_4:app --reload
# Test these JSON endpoints:
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/student
# http://127.0.0.1:8000/students
# Swagger documentation: http://127.0.0.1:8000/docs

