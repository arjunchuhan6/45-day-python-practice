employees = [
    {
        "employee_id": "EMP101",
        "name": "Riya",
        "age": 28,
        "department": "IT",
        "salary": 60000
    },
    {
        "employee_id": "EMP102",
        "name": "Arjun",
        "age": 32,
        "department": "Sales",
        "salary": 55000
    },
    {
        "employee_id": "EMP103",
        "name": "Meera",
        "age": 26,
        "department": "HR",
        "salary": 50000
    }
]

print("Employee database:")
for employee in employees:
    print(
        f"{employee['employee_id']} | {employee['name']} | "
        f"{employee['department']} | Salary: {employee['salary']}"
    )
