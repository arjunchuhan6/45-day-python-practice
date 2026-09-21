# Python Program 9: Test Unauthorized Access

from flask.testing import FlaskClient
from werkzeug.test import TestResponse

from program_8 import app


# Flask's test client sends a request to the API without opening a browser.
with app.test_client() as client: 
	# Do not send the Authorization header.
	response: TestResponse = client.get("/profile")

	print("Status code:", response.status_code)
	print("Response:", response.get_json())

	# 401 means the user is not authorized to access the endpoint.
	assert response.status_code == 401
	assert response.get_json() == {"message": "Token is required"}

print("Unauthorized access test passed")

# Expected output:
# Status code: 401
# Response: {'message': 'Token is required'}
# Unauthorized access test passed