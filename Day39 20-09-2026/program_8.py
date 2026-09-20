import unittest

from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx2 import Response
from httpx2._models import Response
from pydantic import BaseModel, ConfigDict, Field, field_validator


app = FastAPI(title="Registration API", version="1.0.0")


class Registration(BaseModel):
	model_config = ConfigDict(str_strip_whitespace=True)

	name: str = Field(min_length=1, max_length=100)
	email: str = Field(pattern=r"^[A-Za-z0-9._%+-]+@gmail\.com$")
	age: int = Field(ge=18, le=60)
	salary: float = Field(gt=15000)

	@field_validator("name")
	@classmethod
	def name_must_contain_letters(cls, value: str) -> str:
		if not any(character.isalpha() for character in value):
			raise ValueError("Name must contain at least one letter.")
		return value


@app.get("/health")
def health_check() -> dict[str, str]:
	return {"status": "ok"}


@app.post("/registrations", status_code=201)
def create_registration(registration: Registration):
	return {
		"valid": True,
		"message": "Registration successful.",
		"data": registration.model_dump(),
	}


class TestRegistrationAPI(unittest.TestCase):
	client = TestClient(app)

	def test_invalid_request_returns_422(self) -> None:
		response: Response = self.client.post(
			"/registrations",
			json={
				"name": "",
				"email": "user@yahoo.com",
				"age": 15,
				"salary": 10000,
			},
		)

		self.assertEqual(response.status_code, 422)

	def test_valid_request_returns_201(self) -> None:
		response: Response = self.client.post(
			"/registrations",
			json={
				"name": "Asha",
				"email": "asha@gmail.com",
				"age": 25,
				"salary": 50000,
			},
		)

		self.assertEqual(response.status_code, 201)
		self.assertTrue(response.json()["valid"])


if __name__ == "__main__":
	unittest.main()
