# Understand the HTTP POST method.
#
# POST is used to send new data to a server.
# For example, a website can use POST to create a new user or post.
# The data is usually sent in the request body, often in JSON format.
# A successful POST request commonly returns status code 201 (Created).

from urllib.request import Request, urlopen
import json


url = "https://jsonplaceholder.typicode.com/posts"
new_post = {
	"title": "Learning POST",
	"body": "This data was sent using an HTTP POST request.",
	"userId": 1,
}

request = Request(
	url,
	data=json.dumps(new_post).encode("utf-8"),
	headers={"Content-Type": "application/json"},
	method="POST",
)

with urlopen(request) as response:
	created_post = json.load(response)
	print("Status code:", response.status)
	print("Created post:", created_post)