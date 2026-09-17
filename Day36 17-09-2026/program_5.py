# Program 5: Test a FastAPI endpoint
# Install once: python -m pip install fastapi uvicorn httpx2

from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI(title="Endpoint Testing API")


@app.get("/students")
def get_students() -> list[dict[str, int | str]]:
	return [
		{"id": 1, "name": "Asha"},
		{"id": 2, "name": "Rahul"},
	]


# TestClient calls the API without starting a server.
client = TestClient(app)


def test_get_students() -> None:
	response = client.get("/students")

	assert response.status_code == 200
	assert response.json() == [
		{"id": 1, "name": "Asha"},
		{"id": 2, "name": "Rahul"},
	]


if __name__ == "__main__":
	test_get_students()
	print("Endpoint test passed")


# Run the API server from this folder with:
# python -m uvicorn program_5:app --reload
# Run this endpoint test with:
# python program_5.py
# Or use pytest after installing it:
# python -m pip install pytest
# pytest program_5.py
