#calculate  category total cost
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
while True:
    print("Welcome to the Expense Tracker!")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. View Total Expenses")
    print("4. View All Expenses")
    print("5. Search Expense")
    print("6. Calculate Category Total")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == '1':
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        category = input("Enter expense category: ")
        add_expense(expenses, amount, description)
        expenses[-1]['category'] = category  # Assign category to the last added expense
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
                category = expense.get('category', 'N/A')
                print(f"Index: {i}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}, Category: {category}")
                
    elif choice == '5':
        search_desc = input("Enter description to search for: ")
        found_expenses = search_expense(expenses, search_desc)
        if not found_expenses:
            print("No expenses found with that description.")
        else:
            for expense in found_expenses:
                category = expense.get('category', 'N/A')
                print(f"Amount: ${expense['amount']:.2f}, Description: {expense['description']}, Category: {category}")
                
    elif choice == '6':
        category = input("Enter category to calculate total for: ")
        category_total = calculate_category_total(expenses, category)
        print(f"Total for category '{category}': ${category_total:.2f}")