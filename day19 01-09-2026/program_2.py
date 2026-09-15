# read a csv file and print the contents
import csv

with open('people.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)