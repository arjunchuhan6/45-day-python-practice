#add and delete expenses and view total expenses
def add_expense(expenses, amount, description):
    expenses.append({'amount': amount, 'description': description})

def delete_expense(expenses, index):
    if 0 <= index < len(expenses):
        return expenses.pop(index)
    else:
        return None

def view_total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)

expenses = []

while True:
    print("Welcome to the Expense Tracker!")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. View Total Expenses")
    print("4. View All Expenses")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        add_expense(expenses, amount, description)
        print("Expense added successfully!")
        
    elif choice == '2':
        index = int(input("Enter the index of the expense to delete: "))
        deleted_expense = delete_expense(expenses, index)
        if deleted_expense:
            print(f"Deleted expense: Amount: ${deleted_expense['amount']:.2f}, Description: {deleted_expense['description']}")
        else:
            print("Invalid index. No expense deleted.")
            
    elif choice == '3':
        total = view_total_expenses(expenses)
        print(f"Total Expenses: ${total:.2f}")
        
    elif choice == '4':
        if not expenses:
            print("No expenses recorded.")
        else:
            for i, expense in enumerate(expenses):
                print(f"Index: {i}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}")
                
    elif choice == '5':
        print("Exiting Expense Tracker. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")