# Understand the HTTP DELETE method.
#
# DELETE is used to remove an existing resource from a server.
# The resource is identified by its URL, such as /posts/1.
# A successful DELETE request commonly returns status code 200 or 204.

from urllib.request import Request, urlopen


url = "https://jsonplaceholder.typicode.com/posts/1"
request = Request(url, method="DELETE")

with urlopen(request) as response:
	print("Status code:", response.status)
	print("Post was deleted successfully.")

