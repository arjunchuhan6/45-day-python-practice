"""Test a DELETE endpoint with FastAPI.

Run this example from the repository root with:

    py -m pytest "Day41 03-10-2026/program_5.py"

The endpoint deletes a user by ID and returns a confirmation response.
"""

from fastapi import FastAPI, status
from fastapi.testclient import TestClient


app = FastAPI()


@app.delete("/users/{user_id}")
def delete_user(user_id: int) -> dict[str, int | str]:
    """Return a confirmation that the user was deleted."""

    return {"id": user_id, "message": "User deleted successfully"}


client = TestClient(app)


# Testing step 1: send a valid DELETE request with a numeric user ID.
def test_delete_user() -> None:
    """A valid DELETE request should return a confirmation response."""

    response = client.delete("/users/1")

    # Expected result: HTTP 200 with the deleted user's ID and message.
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": 1,
        "message": "User deleted successfully",
    }


# Testing step 2: send an invalid user ID and verify path validation.
def test_delete_user_requires_integer_id() -> None:
    """A non-integer user ID should fail path validation."""

    response = client.delete("/users/invalid")

    # Expected result: HTTP 422 because user_id must be an integer.
    assert response.status_code == 422


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)