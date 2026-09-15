# Employee Salary Program

def calculate_salary(base, bonus=0):
    """Calculate net salary"""
    return base + bonus


def calculate_tax(salary, tax_rate=0.1):
    """Calculate salary after tax"""
    return salary - (salary * tax_rate)


# ===== Test =====

print("=== Salary Calculations ===")
emp1 = calculate_salary(50000, 5000)
print(f"Employee 1 Salary: ${emp1:,}")

emp2 = calculate_salary(45000)
print(f"Employee 2 Salary: ${emp2:,}")

net = calculate_tax(50000, 0.15)
print(f"Salary After 15% Tax: ${net:,.2f}")
#create a function to calculate the average salary of a list of salaries
def calculate_average_salary(salaries):
    """Calculate average salary from a list of salaries"""
    if not salaries:
        return 0
    return sum(salaries) / len(salaries)

# Test the average salary function
salaries = [50000, 45000, 55000, 48000, 52000]
avg_salary = calculate_average_salary(salaries)
print(f"Average Salary: ${avg_salary:,.2f}")