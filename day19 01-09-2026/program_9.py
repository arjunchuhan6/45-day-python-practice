# store contacts information in a json file and print it
import json

contacts = [
    {"name": "Alice", "phone": "123-456-7890", "email": "alice@example.com"},
    {"name": "Bob", "phone": "234-567-8901", "email": "bob@example.com"},
    {"name": "Charlie", "phone": "345-678-9012", "email": "charlie@example.com"},
    {"name": "David", "phone": "456-789-0123", "email": "david@example.com"},
    {"name": "Eve", "phone": "567-890-1234", "email": "eve@example.com"}
]

with open('contacts.json', 'w') as f:
    json.dump(contacts, f)

with open('contacts.json', 'r') as f:
    data = json.load(f)
    for contact in data:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")