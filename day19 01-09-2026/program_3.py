# add csv records to a csv file
import csv

with open('people.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Frank', 45, 'San Antonio'])
    writer.writerow(['Grace', 50, 'San Diego'])
    writer.writerow(['Henry', 55, 'Dallas'])
    writer.writerow(['Ivy', 60, 'San Jose'])
    writer.writerow(['Jack', 65, 'Austin'])
    
with open('people.csv', mode='r') as file:    
    reader = csv.reader(file)
    for row in reader:
        print(row)