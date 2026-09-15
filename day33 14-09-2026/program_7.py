# Send a GET request and receive a response.
# The response contains a status code, headers, and a body.
# The body returned by this API is JSON data.

from urllib.request import urlopen
import json


url = "https://jsonplaceholder.typicode.com/posts/1"

with urlopen(url) as response:
	print("Status code:", response.status)
	print("Content type:", response.headers.get("Content-Type"))

	response_data = json.load(response)
	print("Response body:", response_data)

