"""Test invalid requests with FastAPI.

Run this example from the repository root with:

    py -m pytest "Day41 03-10-2026/program_6.py"

FastAPI returns HTTP 422 when request data does not match the endpoint's
validation rules.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel


class UserCreate(BaseModel):
    """Request body used to create a user."""

    name: str
    age: int


app = FastAPI()


@app.post("/users")
def create_user(user: UserCreate) -> dict[str, str | int]:
    """Return the validated user data."""

    return {"name": user.name, "age": user.age}


@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict[str, int]:
    """Return a user ID after path validation."""

    return {"id": user_id}


client = TestClient(app)


# Testing step 1: omit a required field from the request body.
def test_invalid_request_body() -> None:
    """A missing age should fail request-body validation."""

    response = client.post("/users", json={"name": "Arjun"})

    # Expected result: HTTP 422 because age is required.
    assert response.status_code == 422


# Testing step 2: send text where the endpoint expects an integer.
def test_invalid_request_field_type() -> None:
    """A text age should fail request-body type validation."""

    response = client.post("/users", json={"name": "Arjun", "age": "twenty"})

    # Expected result: HTTP 422 because age must be an integer.
    assert response.status_code == 422


# Testing step 3: send text where the path expects an integer.
def test_invalid_path_parameter() -> None:
    """A non-integer user ID should fail path validation."""

    response = client.get("/users/invalid")

    # Expected result: HTTP 422 because user_id must be an integer.
    assert response.status_code == 422


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)