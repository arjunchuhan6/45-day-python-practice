# Understand HTTP status codes.
#
# A status code tells us what happened after the server received a request.
# 1xx means the request is still being processed.
# 2xx means the request was successful. For example, 200 means OK.
# 3xx means the resource was redirected to another location.
# 4xx means there is a client error. For example, 404 means Not Found.
# 5xx means there is a server error. For example, 500 means Server Error.

from urllib.request import urlopen

from requests import HTTPError


# This function sends a GET request to the given URL.
# It reads the status code when the request succeeds.
# HTTPError catches error responses, such as 404, instead of stopping the program.
def check_url(url) -> None:
	try:
		with urlopen(url) as response:
			status_code = response.status
	except HTTPError as error:
		status_code: int = error.code

	print(url)
	print("Status code:", status_code)

	show_status_message(status_code)


# This function checks the first digit of the status code.
# It prints a simple explanation for the response category.
def show_status_message(status_code) -> None:
	if 100 <= status_code < 200:
		print("Information: the request is being processed.")
	elif 200 <= status_code < 300:
		print("Success: the request worked.")
	elif 300 <= status_code < 400:
		print("Redirect: the resource moved.")
	elif 400 <= status_code < 500:
		print("Client error: check the request.")
	elif 500 <= status_code < 600:
		print("Server error: try again later.")


# This valid post returns 200 because the resource exists.
check_url("https://jsonplaceholder.typicode.com/posts/1")

# This missing post returns 404 because the resource does not exist.
check_url("https://jsonplaceholder.typicode.com/posts/99999")

# These sample codes demonstrate the main status-code groups locally.
# They do not make network requests; they only test our message function.
print("\nSample status codes:")
for sample_code in (200, 301, 404, 500):
	print("Status code:", sample_code)
	show_status_message(sample_code)
