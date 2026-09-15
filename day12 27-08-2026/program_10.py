from program_9 import employees

highest_paid_employee = max(employees, key=lambda employee: employee["salary"])

print("Highest-paid employee:")
print(f"Name: {highest_paid_employee['name']}")
print(f"Department: {highest_paid_employee['department']}")
print(f"Salary: {highest_paid_employee['salary']}")
