# Handle errors when calling an API.
# HTTPError means the server returned an error status, such as 404.
# URLError means the computer could not connect to the server.
# TimeoutError means the server took too long to respond.

from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
import json


def fetch_json(url, timeout=10) -> Any | None:
	try:
		with urlopen(url, timeout=timeout) as response:
			return json.load(response)
	except HTTPError as error: 
		print("API error: status code", error.code)
	except URLError as error: 
		print("Connection error:", error.reason)
	except TimeoutError:
		print("The request took too long.")
	except json.JSONDecodeError:
		print("The server did not return valid JSON.")

	return None


# This URL is valid, so the response is returned as a dictionary.
print("\n1. Successful request")
data: Any | None = fetch_json("https://jsonplaceholder.typicode.com/posts/1")

if data is not None:
	print("Title:", data["title"])

# This URL does not exist, so the HTTPError handler runs.
print("\n2. HTTP error")
fetch_json("https://jsonplaceholder.typicode.com/posts/99999")

# This domain does not exist, so the URLError handler runs.
print("\n3. Connection error")
fetch_json("https://this-domain-does-not-exist.example")

# This server returns HTML instead of JSON, so JSONDecodeError runs.
print("\n4. Invalid JSON")
fetch_json("https://example.com")

# A short timeout demonstrates the timeout handler when the server is slow.
print("\n5. Timeout error")
fetch_json("https://httpbin.org/delay/3", timeout=1)

