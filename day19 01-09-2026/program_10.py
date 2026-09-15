# convert python dictonary to json file
import json

data = {
    "name": "Alice",
    "age": 20,
    "city": "New York"
}

with open('data.json', 'w') as f:
    json.dump(data, f)