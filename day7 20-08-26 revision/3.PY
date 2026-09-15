#WAP grade calclulator using also add fail below 40 marks
marks = int(input("Enter your marks: "))
while marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
    marks = int(input("Enter your marks: "))
if marks < 40:
    print("Fail")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")