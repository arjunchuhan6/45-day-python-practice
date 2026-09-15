"""
BANK MANAGEMENT SYSTEM - STEP 8
================================
Program 8: Save Account Data to JSON

This program saves account information and transaction history to a JSON file.
It can also load that information back into an Account object.
"""

from _io import TextIOWrapper
from io import TextIOWrapper
import json
from typing import Self

from program_7 import Account as HistoryAccount


class Account(HistoryAccount):
	"""Account from Program 7 with JSON save and load methods."""

	def save_to_json(self, file_name) -> None:
		"""Save account information to a JSON file."""
		account_data = {
			"account_number": self.account_number,
			"holder_name": self.holder_name,
			"balance": self.balance,
			"transaction_history": self.transaction_history,
		}

		output_file: TextIOWrapper = open(file_name, "w")
		json.dump(account_data, output_file, indent=4)
		output_file.close()

		print(f"Account data saved to {file_name}")

	@classmethod
	def load_from_json(cls, file_name) -> Self:
		"""Load account information from a JSON file."""
		input_file: TextIOWrapper = open(file_name, "r")
		account_data = json.load(input_file)
		input_file.close()

		account: Self = cls(
			account_data["account_number"],
			account_data["holder_name"],
			account_data["balance"],
		)
		account.transaction_history = account_data["transaction_history"]
		print(f"Account data loaded from {file_name}")
		return account


if __name__ == "__main__":
	print("=" * 50)
	print("BANK MANAGEMENT SYSTEM")
	print("Program 8: Save Account Data to JSON")
	print("=" * 50)

	file_name = "account_data.json"

	print("\n--- Test 1: Create Account and Add Transactions ---")
	account = Account("ACC001", "John Doe", 5000)
	account.deposit(1000)
	account.withdraw(500)

	print("\n--- Test 2: Save Account ---")
	account.save_to_json(file_name)

	print("\n--- Test 3: Load Account ---")
	loaded_account: Account = Account.load_from_json(file_name)
	print(f"Account number: {loaded_account.account_number}")
	print(f"Holder name: {loaded_account.holder_name}")
	print(f"Balance: ${loaded_account.balance:.2f}")

	print("\n--- Test 4: Display Loaded History ---")
	loaded_account.display_transactions()

	print("\nProgram 8 Complete!")
