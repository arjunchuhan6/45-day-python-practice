# Search expenses, create a file, and add, delete, and view total expenses.
import json


EXPENSES_FILE = "expenses.json"


def load_expenses():
    try:
        with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    with open(EXPENSES_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def search_expense(expenses, description):
    return [expense for expense in expenses if description.lower() in expense['description'].lower()]
def add_expense(expenses, amount, description):
    expenses.append({'amount': amount, 'description': description})
def delete_expense(expenses, index):
    if 0 <= index < len(expenses):
        return expenses.pop(index)
    else:
        return None
def view_total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)
def view_expenses(expenses):
    return expenses

expenses = load_expenses()

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
        save_expenses(expenses)
        print("Expense added successfully!")
        
    elif choice == '2':
        index = int(input("Enter the index of the expense to delete: "))
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
        print("Exiting Expense Tracker. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")
