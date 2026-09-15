# Understand the HTTP PUT method.
# PUT is used to update an existing resource on a server.
# The request usually contains the complete new version of that resource.
# A successful PUT request commonly returns status code 200 or 204.

from urllib.request import Request, urlopen
import json


url = "https://jsonplaceholder.typicode.com/posts/1"
updated_post = {
	"id": 1,
	"title": "Updated title",
	"body": "This post was updated using an HTTP PUT request.",
	"userId": 1,
}

request = Request(
	url,
	data=json.dumps(updated_post).encode("utf-8"),
	headers={"Content-Type": "application/json"},
	method="PUT",
)

with urlopen(request) as response:
	result = json.load(response)
	print("Status code:", response.status)
	print("Updated post:", result)

