# read json file and print the contents
import json
with open('people.json', mode='r') as file:
    data = json.load(file)
    for person in data:
        print(person)
