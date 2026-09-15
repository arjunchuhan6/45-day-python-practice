# wap to check someone is eligible for voting or not but add maximum age limit 100
age = int(input("Enter your age: "))
if age >= 18 and age <= 100:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")
    