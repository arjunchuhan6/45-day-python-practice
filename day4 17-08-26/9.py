#create a grade calculator program using if-elif-else statements
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("You have received an A grade.")
elif marks >= 80:
    print("You have received a B grade.")
elif marks >= 70:
    print("You have received a C grade.")

elif marks >= 33 and marks < 69:
    print("You have received a D grade.")
else:
    print("You are failed.")