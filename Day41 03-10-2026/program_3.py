"""Test a POST endpoint with FastAPI.

Run this example from the repository root with:

    py -m pytest "Day41 03-10-2026/program_3.py"

The endpoint accepts a user's name and returns a created-user response.
FastAPI validates the request body before the route handler runs.
"""

from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from pydantic import BaseModel


class UserCreate(BaseModel):
    """Request body used to create a user."""

    name: str


app = FastAPI()


@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate) -> dict[str, str]:
    """Return the newly created user's name."""

    return {"name": user.name}


client = TestClient(app)


# Testing step 1: send a valid POST request and verify the created response.
def test_create_user() -> None:
    """A valid POST request should create a user."""

    response = client.post("/users", json={"name": "Arjun"})

    # Expected result: HTTP 201 and the submitted user's name.
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"name": "Arjun"}


# Testing step 2: send an incomplete request and verify validation.
def test_create_user_requires_name() -> None:
    """A POST request without a name should fail validation."""

    response = client.post("/users", json={})

    # Expected result: HTTP 422 because the required name is missing.
    assert response.status_code == 422


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)