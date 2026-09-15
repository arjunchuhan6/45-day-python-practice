# updarte json file with new data
import json

with open('people.json', mode='r') as file:
    data = json.load(file)

data.append({'name': 'Frank', 'age': 45, 'city': 'San Antonio'})
data.append({'name': 'Grace', 'age': 50, 'city': 'San Diego'})
data.append({'name': 'Henry', 'age': 55, 'city': 'Dallas'})
data.append({'name': 'Ivy', 'age': 60, 'city': 'San Jose'})
data.append({'name': 'Jack', 'age': 65, 'city': 'Austin'})

with open('people.json', mode='w') as file:
    json.dump(data, file, indent=4)