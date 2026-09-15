# wap to expense  tracker to add expenses and view total expenses
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})

    def view_total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        return total

    def view_expenses(self):
        return self.expenses

print("Welcome to the Expense Tracker!")
tracker = ExpenseTracker()
print("1. Add Expense")
print("2. View Total Expenses")
print("3. View All Expenses")
while True:
    choice = input("Enter your choice (1-3) or 'q' to quit: ")
    if choice == '1':
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        tracker.add_expense(amount, description)
        print("Expense added successfully!")
    elif choice == '2':
        total = tracker.view_total_expenses()
        print(f"Total Expenses: ${total:.2f}")
    elif choice == '3':
        expenses = tracker.view_expenses()
        if not expenses:
            print("No expenses recorded.")
        else:
            for expense in expenses:
                print(f"Amount: ${expense['amount']:.2f}, Description: {expense['description']}")
    elif choice.lower() == 'q':
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
