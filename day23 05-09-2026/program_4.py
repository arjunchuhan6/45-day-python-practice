#create a bank aaccount constructor
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def display_info(self):
        print(f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}")
        
# Create an instance of the BankAccount class
account1 = BankAccount("123456789", "Frank", 1000.50)
account1.display_info()
account2 = BankAccount("987654321", "Grace", 2500.75)
account2.display_info()