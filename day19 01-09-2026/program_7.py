# delete json data with age equal to 50
import json
with open('people.json', mode='r') as file:
    data = json.load(file)
    data = [person for person in data if person['age'] != 50]

with open('people.json', mode='w') as file:
    json.dump(data, file, indent=4)
