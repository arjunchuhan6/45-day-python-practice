# Program 3: Create three basic routes
# Install once: python -m pip install fastapi uvicorn

from fastapi import FastAPI


app = FastAPI(title="First Route API")


# The / route is the home page of this API.
@app.get("/")
def home() -> dict[str, str]:
	return {"message": "Hello from the home route"}


@app.get("/about")
def about() -> dict[str, str]:
	return {"message": "This is the about route"}


@app.get("/students")
def students() -> list[dict[str, int | str]]:
	return [
		{"id": 1, "name": "Asha"},
		{"id": 2, "name": "Rahul"},
	]


# Run from this folder with:
# python -m uvicorn program_3:app --reload
# Test the route in a browser:
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/about
# http://127.0.0.1:8000/students
# Swagger documentation: http://127.0.0.1:8000/docs

