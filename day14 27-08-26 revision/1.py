"""A mini Contact Management System using Python collection data types."""


from dummy_data import contacts


def get_phone_numbers():
	"""Read one or more phone numbers and return them as a list."""
	phone_numbers = []
	while True:
		phone_number = input("Enter phone number: ").strip()
		if phone_number and phone_number not in phone_numbers:
			phone_numbers.append(phone_number)
			if input("Add another phone number? (y/n): ").strip().lower() != "y":
				return phone_numbers
		elif phone_number:
			print("That phone number is already stored.")
		else:
			print("At least one phone number is required.")


def get_tags():
	"""Read comma-separated tags and return them as a set."""
	tag_text = input("Enter tags separated by commas (optional): ").strip()
	return {tag.strip().lower() for tag in tag_text.split(",") if tag.strip()}


def add_contact():
	name = input("Enter contact name: ").strip()
	if not name:
		print("Name cannot be empty.")
		return

	contact_key = name.casefold()
	if contact_key in contacts:
		print("A contact with that name already exists.")
		return

	email = input("Enter email (optional): ").strip()
	city = input("Enter city: ").strip()
	state = input("Enter state (optional): ").strip()
	contacts[contact_key] = {
		"name": name,
		"phone_numbers": get_phone_numbers(),
		"email": email,
		"address": (city, state),
		"tags": get_tags(),
	}
	print("Contact added successfully.")


def display_contact(contact):
	city, state = contact["address"]
	location = f"{city}, {state}" if state else city
	tags = ", ".join(sorted(contact["tags"])) or "None"
	print(f"\nName: {contact['name']}")
	print(f"Phone numbers: {', '.join(contact['phone_numbers'])}")
	print(f"Email: {contact['email'] or 'None'}")
	print(f"City: {location or 'None'}")
	print(f"Tags: {tags}")


def display_contacts(contact_list=None):
	selected_contacts = contact_list if contact_list is not None else list(contacts.values())
	if not selected_contacts:
		print("No contacts found. Choose option 1 to add a contact first.")
		return

	print(f"\nTotal contacts displayed: {len(selected_contacts)}")
	for contact in sorted(selected_contacts, key=lambda item: item["name"].casefold()):
		display_contact(contact)


def search_contact():
	search_text = input("Search by name, phone, email, city, or tag: ").strip().casefold()
	matches = []
	for contact in contacts.values():
		city, state = contact["address"]
		searchable_values = [
			contact["name"],
			contact["email"],
			city,
			state,
			*contact["phone_numbers"],
			*contact["tags"],
		]
		if any(search_text in value.casefold() for value in searchable_values):
			matches.append(contact)
	display_contacts(matches)


def update_contact():
	contact_key = input("Enter the name of the contact to update: ").strip().casefold()
	contact = contacts.get(contact_key)
	if contact is None:
		print("Contact not found.")
		return

	print("Press Enter to keep the current value.")
	new_email = input(f"Email [{contact['email']}]: ").strip()
	new_city = input(f"City [{contact['address'][0]}]: ").strip()
	new_state = input(f"State [{contact['address'][1]}]: ").strip()
	if new_email:
		contact["email"] = new_email
	if new_city or new_state:
		old_city, old_state = contact["address"]
		contact["address"] = (new_city or old_city, new_state or old_state)
	if input("Replace phone numbers? (y/n): ").strip().lower() == "y":
		contact["phone_numbers"] = get_phone_numbers()
	if input("Replace tags? (y/n): ").strip().lower() == "y":
		contact["tags"] = get_tags()
	print("Contact updated successfully.")


def delete_contact():
	contact_key = input("Enter the name of the contact to delete: ").strip().casefold()
	if contact_key not in contacts:
		print("Contact not found.")
		return
	deleted_contact = contacts.pop(contact_key)
	print(f"Deleted {deleted_contact['name']} successfully.")


def find_contacts_by_city():
	city = input("Enter city: ").strip().casefold()
	matches = [
		contact
		for contact in contacts.values()
		if contact["address"][0].casefold() == city
	]
	display_contacts(matches)


def show_menu():
	print("""
========== Contact Management System ==========
1. Add contact
2. Display contacts
3. Search contact
4. Update contact
5. Delete contact
6. Count contacts
7. Find contacts by city
8. Exit
===============================================
""")


def main():
	actions = {
		"1": add_contact,
		"2": display_contacts,
		"3": search_contact,
		"4": update_contact,
		"5": delete_contact,
		"7": find_contacts_by_city,
	}
	while True:
		show_menu()
		choice = input("Enter your choice: ").strip()
		if choice in actions:
			actions[choice]()
		elif choice == "6":
			print(f"Total contacts: {len(contacts)}")
		elif choice == "8":
			print("Thank you for using Contact Management System.")
			break
		else:
			print("Invalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
	main()
