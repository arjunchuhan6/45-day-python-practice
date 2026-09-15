#calculate total cost of items purchased/expenses
def calculate_total_cost(expenses):
    return sum(expense['amount'] for expense in expenses)
def view_expenses(expenses):
    return expenses
def search_expense(expenses, description):
    return [expense for expense in expenses if description.lower() in expense['description'].lower()]
def add_expense(expenses, amount, description):
    default_expense = {'amount': amount, 'description': description}
    expenses.append(default_expense)
def delete_expense(expenses, index):
    if 0 <= index < len(expenses):
        return expenses.pop(index)
    else:
        return None
expenses = []
while True:
    print("Welcome to the Expense Tracker!")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. View Total Expenses")
    print("4. View All Expenses")
    print("5. Search Expense")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
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
        total = calculate_total_cost(expenses)
        print(f"Total Expenses: ${total:.2f}")
        
    elif choice == '4':
        if not expenses:
            print("No expenses recorded.")
        else:
            for i, expense in enumerate(expenses):
                print(f"Index: {i}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}")
                
    elif choice == '5':
        search_desc = input("Enter description to search for: ")
        found_expenses = search_expense(expenses, search_desc)
        if not found_expenses:
            print("No expenses found with that description.")
        else:
            for expense in found_expenses:
                print(f"Amount: ${expense['amount']:.2f}, Description: {expense['description']}")
                
    elif choice == '6':
        print("Exiting Expense Tracker. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")