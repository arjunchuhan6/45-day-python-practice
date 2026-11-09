"""Test a basic GET endpoint with FastAPI."""

from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI()


@app.get("/welcome")
def welcome() -> dict[str, str]:
    """Return a welcome message."""

    return {"message": "Arjun"}


client = TestClient(app)


def test_get_welcome() -> None:
    """Test that GET /welcome returns the expected response."""

    response = client.get("/welcome")

    assert response.status_code == 200
    assert response.json() == {"message": "Arjun"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)