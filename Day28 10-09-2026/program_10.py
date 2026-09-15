"""
BANK MANAGEMENT SYSTEM - STEP 10
=================================
Program 10: Complete Interactive System

The client enters account details and chooses bank operations from a menu.
"""

from program_9 import Account


def get_account_from_client() -> Account:
	"""Create an account using information entered by the client."""
	print("\n--- Create Bank Account ---")
	account_number: str = input("Enter account number: ")
	holder_name: str = input("Enter your name: ")

	while True:
		try:
			initial_balance = float(input("Enter initial balance: "))
			if initial_balance < 0:
				print("Error: Balance cannot be negative")
				continue
			return Account(account_number, holder_name, initial_balance)
		except ValueError:
			print("Error: Please enter a valid number")


def show_menu() -> None:
	"""Display available bank operations."""
	print("\n--- Bank Menu ---")
	print("1. Deposit money")
	print("2. Withdraw money")
	print("3. Check balance")
	print("4. Show transaction history")
	print("5. Exit")


def run_bank_system() -> None:
	"""Run the bank system until the client chooses Exit."""
	print("=" * 50)
	print("WELCOME TO THE BANK MANAGEMENT SYSTEM")
	print("=" * 50)

	account: Account = get_account_from_client()
	file_name: str = "account_data.json"
	account.save_safely(file_name)
	print(f"Data will be saved automatically in {file_name}")

	while True:
		show_menu()
		choice: str = input("Enter your choice: ")

		if choice == "1":
			amount: str = input("Enter deposit amount: ")
			if account.deposit_safely(amount):
				account.save_safely(file_name)
		elif choice == "2":
			amount: str = input("Enter withdrawal amount: ")
			if account.withdraw_safely(amount):
				account.save_safely(file_name)
		elif choice == "3":
			print(f"Current balance: ${account.balance:.2f}")
		elif choice == "4":
			account.display_transactions()
		elif choice == "5":
			account.save_safely(file_name)
			print("Thank you for using the Bank Management System")
			break
		else:
			print("Error: Please choose a number from 1 to 5")


if __name__ == "__main__":
	run_bank_system()
