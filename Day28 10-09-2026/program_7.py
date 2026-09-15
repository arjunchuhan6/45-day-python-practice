"""
BANK MANAGEMENT SYSTEM - STEP 7
================================
Program 7: Store Transaction History

This program stores every successful deposit and withdrawal in a list.
Each transaction stores its type, amount, time, and new balance.
"""

from datetime import datetime
from typing import Any


class Account:
	"""Bank account with simple transaction history."""

	def __init__(self, account_number, holder_name, initial_balance=0) -> None:
		self.account_number: Any = account_number
		self.holder_name: Any = holder_name
		self.balance: int = initial_balance
		self.transaction_history = []

	def add_transaction(self, transaction_type, amount) -> None:
		"""Store one completed transaction."""
		transaction = {
			"type": transaction_type,
			"amount": amount,
			"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
			"balance": self.balance,
		}
		self.transaction_history.append(transaction)

	def deposit(self, amount) -> bool:
		"""Deposit money and save the transaction if the amount is valid."""
		if amount <= 0:
			print("Error: Deposit amount must be positive")
			return False

		self.balance = self.balance + amount
		self.add_transaction("Deposit", amount)
		print(f"Deposit successful: ${amount:.2f}")
		return True

	def withdraw(self, amount) -> bool:
		"""Withdraw money and save the transaction if it is valid."""
		if amount <= 0:
			print("Error: Withdrawal amount must be positive")
			return False

		if amount > self.balance:
			print("Error: Insufficient balance")
			return False

		self.balance = self.balance - amount
		self.add_transaction("Withdrawal", amount)
		print(f"Withdrawal successful: ${amount:.2f}")
		return True

	def get_transaction_history(self):
		"""Return all stored transactions."""
		return self.transaction_history

	def display_transactions(self) -> None:
		"""Display all stored transactions."""
		print("\n--- Transaction History ---")

		if len(self.transaction_history) == 0:
			print("No transactions found")
			return

		for number, transaction in enumerate(self.transaction_history, start=1):
			print(f"{number}. {transaction['type']}")
			print(f"   Amount: ${transaction['amount']:.2f}")
			print(f"   Time: {transaction['time']}")
			print(f"   Balance after transaction: ${transaction['balance']:.2f}")


if __name__ == "__main__":
	print("=" * 50)
	print("BANK MANAGEMENT SYSTEM")
	print("Program 7: Store Transaction History")
	print("=" * 50)

	print("\n--- Test 1: Create Account ---")
	account: Account[str, str] = Account("ACC001", "John Doe", 5000)
	print(f"Starting balance: ${account.balance:.2f}")

	print("\n--- Test 2: Successful Transactions ---")
	account.deposit(1000)
	account.withdraw(500)
	account.deposit(250)

	print("\n--- Test 3: Failed Transaction ---")
	account.withdraw(10000)

	print("\n--- Test 4: Display History ---")
	account.display_transactions()

	print("\nTotal stored transactions:", len(account.get_transaction_history()))
	print("Final balance: ${:.2f}".format(account.balance))
	print("\nProgram 7 Complete!")
