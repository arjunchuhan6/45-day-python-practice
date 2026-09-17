# Program 2: Build a basic FastAPI application
# Install once: py -m pip install fastapi uvicorn

from fastapi import FastAPI


# Create the FastAPI application.
app = FastAPI(title="Student API")


@app.get("/")
def home() -> dict[str, str]:
	return {"message": "Welcome to the Student API"}


@app.get("/about")
def about() -> dict[str, str]:
	return {"about": "This API is built with FastAPI"}


@app.get("/students")
def get_students() -> list[dict[str, str | int]]:
	return [
		{"id": 1, "name": "Asha", "course": "Python"},
		{"id": 2, "name": "Rahul", "course": "FastAPI"},
	]


# Run from this folder with:
# py -m uvicorn program_2:app --reload
# Test in a browser:
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/about
# http://127.0.0.1:8000/students
# Interactive Swagger documentation:
# http://127.0.0.1:8000/docs

