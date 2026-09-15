#find lowest and highest expense
def find_lowest_expense(expenses):
    if not expenses:
        return None
    return min(expenses, key=lambda x: x['amount'])
def find_highest_expense(expenses):
    if not expenses:
        return None
    return max(expenses, key=lambda x: x['amount'])
def calculate_category_total(expenses, category):
    return sum(expense['amount'] for expense in expenses if expense.get('category') == category)
def add_expense(expenses, amount, description):
    default_expense = {'amount': amount, 'description': description}
    expenses.append(default_expense)
def delete_expense(expenses, index):
    if 0 <= index < len(expenses):
        return expenses.pop(index)
    else:
        return None
def view_total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)
def view_expenses(expenses):
    return expenses
def search_expense(expenses, description):
    return [expense for expense in expenses if description.lower() in expense['description'].lower()]
expenses = []
def save_expenses(expenses):
    import json
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    import json
    try:
        with open('expenses.json', 'r') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

expenses = load_expenses()

while True:
    print("Welcome to the Expense Tracker!")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. View Total Expenses")
    print("4. View All Expenses")
    print("5. Search Expense")
    print("6. Find Lowest Expense")
    print("7. Find Highest Expense")
    print("8. Exit (or type 'exit')")
    
    choice = input("Enter your choice (1-8): ").strip()
    
    if choice == '1':
        try:
            amount = float(input("Enter expense amount: "))
            if amount < 0:
                raise ValueError
        except ValueError:
            print("Please enter a valid non-negative amount.")
            continue
        description = input("Enter expense description: ")
        add_expense(expenses, amount, description)
        save_expenses(expenses)
        print("Expense added successfully!")
        
    elif choice == '2':
        try:
            index = int(input("Enter the index of the expense to delete: "))
        except ValueError:
            print("Please enter a valid integer index.")
            continue
        deleted_expense = delete_expense(expenses, index)
        if deleted_expense:
            save_expenses(expenses)
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
        search_desc = input("Enter description to search for: ")
        found_expenses = search_expense(expenses, search_desc)
        if not found_expenses:
            print("No expenses found with that description.")
        else:
            for expense in found_expenses:
                print(f"Amount: ${expense['amount']:.2f}, Description: {expense['description']}")
                
    elif choice == '6':
        lowest_expense = find_lowest_expense(expenses)
        if lowest_expense:
            print(f"Lowest Expense: Amount: ${lowest_expense['amount']:.2f}, Description: {lowest_expense['description']}")
        else:
            print("No expenses recorded.")
            
    elif choice == '7':
        highest_expense = find_highest_expense(expenses)
        if highest_expense:
            print(f"Highest Expense: Amount: ${highest_expense['amount']:.2f}, Description: {highest_expense['description']}")
        else:
            print("No expenses recorded.")

    elif choice in ('8', 'exit'):
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 8.")