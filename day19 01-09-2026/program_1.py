# create a csv file with the following columns: name, age, city
import csv

with open('people.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])
    writer.writerow(['Charlie', 35, 'Chicago'])
    writer.writerow(['David', 40, 'Houston'])
    writer.writerow(['Eve', 38, 'Phoenix'])