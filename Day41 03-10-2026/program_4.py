"""Test a PUT endpoint with FastAPI.

Run this example from the repository root with:

    py -m pytest "Day41 03-10-2026/program_4.py"

The endpoint updates a user's name and returns the updated user.
"""

from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from pydantic import BaseModel


class UserUpdate(BaseModel):
    """Request body used to update a user."""

    name: str


app = FastAPI()


@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate) -> dict[str, int | str]:
    """Return the updated user's ID and name."""

    return {"id": user_id, "name": user.name}


client = TestClient(app)


# Testing step 1: send a valid PUT request with a path ID and new name.
def test_update_user() -> None:
    """A valid PUT request should update the user's name."""

    response = client.put("/users/1", json={"name": "Arjun Updated"})

    # Expected result: HTTP 200 with the user ID and updated name.
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"id": 1, "name": "Arjun Updated"}


# Testing step 2: send an invalid path ID and verify FastAPI validation.
def test_update_user_requires_integer_id() -> None:
    """A non-integer user ID should fail path validation."""

    response = client.put("/users/invalid", json={"name": "Arjun Updated"})

    # Expected result: HTTP 422 because user_id must be an integer.
    assert response.status_code == 422


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)