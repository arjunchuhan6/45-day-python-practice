# store student  information in a json file and print it
import json
students = [
    {"name": "Alice", "age": 20, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 30, "city": "Chicago"}, 
    {"name": "David", "age": 35, "city": "Houston"},
    {"name": "Eve", "age": 38, "city": "Phoenix"},
    {"name": "Frank", "age": 45, "city": "San Antonio"},
    {"name": "Grace", "age": 50, "city": "San Diego"},
    {"name": "Henry", "age": 55, "city": "Dallas"},
    {"name": "Ivy", "age": 60, "city": "San Jose"},
    {"name": "Jack", "age": 65, "city": "Austin"}
]

with open('students.json', 'w') as f:
    json.dump(students, f)

with open('students.json', 'r') as f:
    data = json.load(f)
    for student in data:
        print(f"Name: {student['name']}, Age: {student['age']}, City: {student['city']}")