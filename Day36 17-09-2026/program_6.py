# Program 6: Understand Swagger documentation
# Install once: python -m pip install fastapi uvicorn

from fastapi import FastAPI


app = FastAPI(
	title="Student Documentation API",
	description="A beginner API for learning Swagger documentation.",
	version="1.0.0",
)


@app.get("/", summary="Home route")
def home() -> dict[str, str]:
	"""Return a welcome message."""
	return {"message": "Open /docs to explore this API"}


@app.get("/students", summary="List students")
def get_students() -> list[dict[str, int | str]]:
	"""Return all students as JSON."""
	return [
		{"id": 1, "name": "Asha", "course": "Python"},
		{"id": 2, "name": "Rahul", "course": "FastAPI"},
	]


# Run from this folder with:
# python -m uvicorn program_6:app --reload
# Open Swagger UI: http://127.0.0.1:8000/docs
# In Swagger, expand an endpoint, click "Try it out", then click "Execute".
# The response body, status code, and request URL appear below the endpoint.
# Alternative documentation: http://127.0.0.1:8000/redoc
# Swagger reads the routes and creates the documentation automatically.

