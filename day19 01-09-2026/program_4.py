# create a json file with the following data: name, age, city
import json
with open('people.json', mode='w') as file:
    data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
        {'name': 'David', 'age': 40, 'city': 'Houston'},
        {'name': 'Eve', 'age': 38, 'city': 'Phoenix'}
    ]
    json.dump(data, file, indent=4)