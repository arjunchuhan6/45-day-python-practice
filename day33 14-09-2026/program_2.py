# Understand the HTTP GET method.
#
# GET is used to request or read data from a server.
# It does not normally change or delete data on the server.
# A successful GET request usually returns status code 200.
# APIs often return the requested data in JSON format.

from urllib.request import urlopen
import json


# This public test API returns information about one post.
url = "https://jsonplaceholder.typicode.com/posts/1"

with urlopen(url) as response:
	print("Status code:", response.status)

	data = json.load(response)
	print("Post title:", data["title"])
	print("Post body:", data["body"])
