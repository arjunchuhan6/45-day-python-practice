"""Fifty sample contacts for the Contact Management System."""


first_names = (
	"Rahul", "Priya", "Arjun", "Neha", "Amit",
	"Sneha", "Vikram", "Ananya", "Rohan", "Kavya",
)
last_names = ("Sharma", "Patel", "Reddy", "Mehta", "Iyer")
cities = (
	("Pune", "Maharashtra"),
	("Mumbai", "Maharashtra"),
	("Hyderabad", "Telangana"),
	("Bengaluru", "Karnataka"),
	("Chennai", "Tamil Nadu"),
)
tags = ("friend", "family", "work", "college", "business")


contacts = {}
for index, (first_name, last_name) in enumerate(
	((first_name, last_name)
	for first_name in first_names
	for last_name in last_names),
	start=1,
):
	name = f"{first_name} {last_name}"
	city, state = cities[(index - 1) % len(cities)]
	contacts[name.casefold()] = {
		"name": name,
		"phone_numbers": [
			f"9{index:09d}",
			f"8{index:09d}",
		],
		"email": f"{first_name.lower()}.{last_name.lower()}{index}@example.com",
		"address": (city, state),
		"tags": {tags[(index - 1) % len(tags)], tags[index % len(tags)]},
	}
