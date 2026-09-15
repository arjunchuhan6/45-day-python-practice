"""A small, persistent command-line expense tracker."""
import json

FILE_NAME = "expenses project.json"


def add_expense(expenses, amount, description, category):
    expenses.append({"amount": amount, "description": description, "category": category})


def delete_expense(expenses, index):
    if 0 <= index < len(expenses):
        return expenses.pop(index)
    return None


def view_total_expenses(expenses):
    return sum(expense["amount"] for expense in expenses)


def view_expenses(expenses):
    return expenses


def search_expense(expenses, description):
    return [expense for expense in expenses
            if description.lower() in expense["description"].lower()]


def calculate_category_total(expenses, category):
    return sum(expense["amount"] for expense in expenses
               if expense["category"].lower() == category.lower())


def save_expenses(expenses):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def load_expenses():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []


def display_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    for number, expense in enumerate(expenses, 1):
        print(f"{number}. {expense['description']} | "
              f"{expense['category']} | ${expense['amount']:.2f}")


def read_amount():
    while True:
        try:
            amount = float(input("Amount: ").strip())
            if amount < 0:
                raise ValueError
            return amount
        except ValueError:
            print("Invalid amount. Enter a non-negative number.")


def main():
    expenses = load_expenses()
    while True:
        print("\nWelcome to the Expense Tracker!")
        print("1. Add Expense\n2. Delete Expense\n3. View Total Expenses")
        print("4. View Expenses by Category\n5. View All Expenses")
        print("6. Search Expense\n7. Calculate Category Total\n8. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            description = input("Description: ").strip()
            category = input("Category: ").strip()
            if not description or not category:
                print("Description and category cannot be empty.")
                continue
            add_expense(expenses, read_amount(), description, category)
            save_expenses(expenses)
            print("Expense added.")
        elif choice == "2":
            display_expenses(expenses)
            try:
                index = int(input("Expense number to delete: ")) - 1
                deleted = delete_expense(expenses, index)
                if deleted is None:
                    print("Invalid expense number.")
                else:
                    save_expenses(expenses)
                    print("Expense deleted.")
            except ValueError:
                print("Invalid input. Enter a whole number.")
        elif choice == "3":
            print(f"Total expenses: ${view_total_expenses(expenses):.2f}")
        elif choice == "4":
            category = input("Category: ").strip()
            display_expenses([e for e in expenses if e["category"].lower() == category.lower()])
        elif choice == "5":
            display_expenses(view_expenses(expenses))
        elif choice == "6":
            display_expenses(search_expense(expenses, input("Search description: ").strip()))
        elif choice == "7":
            category = input("Category: ").strip()
            print(f"{category} total: ${calculate_category_total(expenses, category):.2f}")
        elif choice == "8":
            save_expenses(expenses)
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid option. Choose 1-8.")


if __name__ == "__main__":
    main()
    
        
