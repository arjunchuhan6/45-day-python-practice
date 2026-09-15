# Today we learn how to use APIs with Python.
#
# An API (Application Programming Interface) allows one program to
# communicate with another program and exchange data.
# Web APIs usually send and receive data over the internet.

# Understand HTTP (HyperText Transfer Protocol).
# HTTP is the set of rules used for communication between a client and a server.
# In Python, our program is usually the client and sends a request to a server.

# Common HTTP methods:
# GET    - retrieve data from a server.
# POST   - send new data to a server.
# PUT    - update existing data on a server.
# DELETE - remove data from a server.

# An HTTP response contains a status code and usually some data.
# 200 means the request was successful.
# 404 means the requested resource was not found.
# 500 means the server encountered an error.

# APIs commonly exchange data in JSON format because it is easy to read
# and can be converted into Python dictionaries and lists.


# Simple HTTP GET request
from urllib.request import Request, urlopen
import json


url = "https://jsonplaceholder.typicode.com/todos/1"
request = Request(url, method="GET")

with urlopen(request) as response:
	print("Status code:", response.status)
	print("Content type:", response.headers.get("Content-Type"))

	response_text = response.read().decode("utf-8")
	todo = json.loads(response_text)
	print("Response data:", todo)

