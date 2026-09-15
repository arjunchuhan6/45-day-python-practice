#create a Bank account class with attributes account_number, account_holder, and balance
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
print("BankAccount class created successfully.")
account1 = BankAccount("123456", "Alice", 1000.0)
account2 = BankAccount("789012", "Bob", 2000.0)
print(f"Account 1: {account1.account_number}, Holder: {account1.account_holder}, Balance: ${account1.balance}")
print(f"Account 2: {account2.account_number}, Holder: {account2.account_holder}, Balance: ${account2.balance}")
