# Small API-consuming application.
# This program gets meaningful product JSON from an API and lets the user
# view one product.

from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import json


API_URL = "https://dummyjson.com/products?limit=10"


def get_products():
	try:
		request = Request(
			API_URL,
			headers={"User-Agent": "Mozilla/5.0"},
		)
		with urlopen(request, timeout=10) as response:
			data = json.load(response)
			return data["products"]
	except HTTPError as error:
		print(f"API error ({error.code}) while requesting {API_URL}")
		print("Server message:", error.reason)
	except URLError as error: 
		print("Connection error while contacting the API:", error.reason)
	except TimeoutError:
		print("API error: the request took too long.")
	except json.JSONDecodeError:
		print("API error: the server returned invalid JSON.")

	return []


def show_product(product) -> None:
	print("\nProduct ID:", product["id"])
	print("Name:", product["title"])
	print("Category:", product["category"])
	print("Price: $", product["price"], sep="")
	print("Rating:", product["rating"])
	print("Stock:", product["stock"])
	print("Description:", product["description"])


def main() -> None:
	while True:
		products = get_products()

		if not products:
			print("No products were loaded.")
			choice = input("Press Enter to retry or type q to quit: ").lower()
			if choice == "q":
				break
			continue

		print("\nProducts from the API:\n")
		for product in products:
			print(f'{product["id"]}. {product["title"]} - ${product["price"]}')

		choice = input("\nEnter a product ID, or q to quit: ").lower()
		if choice == "q":
			break

		try:
			product_id = int(choice)
		except ValueError:
			print("Please enter a whole number.")
			continue

		selected_product = next(
			(product for product in products if product["id"] == product_id),
			None,
		)

		if selected_product is None:
			print("Product not found. Please try again.")
		else:
			show_product(selected_product)


if __name__ == "__main__":
	main()
