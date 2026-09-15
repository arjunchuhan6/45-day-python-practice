"""
BANK MANAGEMENT SYSTEM - STEP 9
================================
Program 9: Handle Errors and Exceptions

This program catches common errors so the bank program can continue running.
"""

from typing import Self

from program_8 import Account as JsonAccount


class Account(JsonAccount):
	"""Account with simple error handling."""

	def deposit_safely(self, amount) -> bool:
		"""Try to deposit money and show a friendly error if it fails."""
		try:
			amount = float(amount)
			return self.deposit(amount)
		except (TypeError, ValueError):
			print("Error: Please enter a valid number for the deposit")
			return False

	def withdraw_safely(self, amount) -> bool:
		"""Try to withdraw money and show a friendly error if it fails."""
		try:
			amount = float(amount)
			return self.withdraw(amount)
		except (TypeError, ValueError):
			print("Error: Please enter a valid number for the withdrawal")
			return False

	def save_safely(self, file_name) -> bool:
		"""Save data and handle file errors."""
		try:
			self.save_to_json(file_name)
			return True
		except OSError:
			print("Error: Could not save the account file")
			return False

	@classmethod
	def load_safely(cls, file_name) -> Self:
		"""Load data and handle common JSON and file errors."""
		try:
			return cls.load_from_json(file_name)
		except FileNotFoundError:
			print("Error: Account file was not found")
		except ValueError:
			print("Error: Account file contains invalid JSON")
		except KeyError:
			print("Error: Account file is missing required data")

		return None


if __name__ == "__main__":
	print("=" * 50)
	print("BANK MANAGEMENT SYSTEM")
	print("Program 9: Handle Errors and Exceptions")
	print("=" * 50)

	print("\n--- Test 1: Valid Deposit ---")
	account = Account("ACC001", "John Doe", 5000)
	account.deposit_safely("1000")

	print("\n--- Test 2: Invalid Deposit ---")
	account.deposit_safely("abc")

	print("\n--- Test 3: Withdrawal With Insufficient Funds ---")
	account.withdraw_safely(10000)

	print("\n--- Test 4: Invalid Withdrawal ---")
	account.withdraw_safely("wrong")

	print("\n--- Test 5: Missing JSON File ---")
	Account.load_safely("file_that_does_not_exist.json")

	print("\nFinal balance: ${:.2f}".format(account.balance))
	print("\nProgram 9 Complete!")
