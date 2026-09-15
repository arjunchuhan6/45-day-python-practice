# Read a JSON response from an API.
# JSON object data becomes a Python dictionary after json.loads().

from urllib.request import urlopen
import json


url = "https://jsonplaceholder.typicode.com/posts/1"

with urlopen(url) as response:
	response_text = response.read().decode("utf-8")
	post = json.loads(response_text)

print("Title:", post["title"])
print("Body:", post["body"])
print("User ID:", post["userId"])

