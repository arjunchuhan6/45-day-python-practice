"""Test authentication for a FastAPI endpoint.

Run this example from the repository root with:

    py -m pytest "Day41 03-10-2026/program_7.py"

The protected endpoint requires a valid API key in the request headers.
"""

from fastapi import Depends, FastAPI, Header, HTTPException, status
from fastapi.testclient import TestClient


EXPECTED_API_KEY = "test-api-key"
app = FastAPI()


def verify_api_key(x_api_key: str | None = Header(default=None)) -> str:
    """Return the API key when it is valid, otherwise reject the request."""

    if x_api_key != EXPECTED_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )

    return x_api_key


@app.get("/protected")
def protected_route(api_key: str = Depends(verify_api_key)) -> dict[str, str]:
    """Return protected data after successful authentication."""

    return {"message": "Authenticated successfully"}


client = TestClient(app)


# Testing step 1: send the correct API key in the request header.
def test_authenticated_request() -> None:
    """A valid API key should allow access to the protected endpoint."""

    response = client.get(
        "/protected",
        headers={"X-API-Key": EXPECTED_API_KEY},
    )

    # Expected result: HTTP 200 and the protected response.
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Authenticated successfully"}


# Testing step 2: omit the API key from the request.
def test_request_without_api_key() -> None:
    """A missing API key should deny access."""

    response = client.get("/protected")

    # Expected result: HTTP 401 because authentication is required.
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Invalid or missing API key"}


# Testing step 3: send an incorrect API key.
def test_request_with_invalid_api_key() -> None:
    """An incorrect API key should deny access."""

    response = client.get(
        "/protected",
        headers={"X-API-Key": "wrong-key"},
    )

    # Expected result: HTTP 401 because the API key is invalid.
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)