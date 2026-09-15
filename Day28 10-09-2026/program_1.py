"""
BANK MANAGEMENT SYSTEM - STEP 1
================================
Program 1: Create Account Class

WHAT WE ARE DOING:
- Create a simple Account class to store account information
- Store: Account Number, Account Holder Name, Balance
- Methods to get and display account information

NOTES FOR NEXT PROGRAM:
- Program 2 will add Customer class that manages accounts
"""

class Account:
    """
    A simple class to represent a bank account
    Attributes: account_number, holder_name, balance
    """
    
    def __init__(self, account_number, holder_name, initial_balance=0):
        """
        Create a new account
        
        Parameters:
        - account_number: unique ID (example: "ACC001")
        - holder_name: name of account owner (example: "John Doe")
        - initial_balance: starting amount (default 0)
        """
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
        print(f"Account {account_number} created for {holder_name}")
    
    def get_account_number(self):
        """Return the account number"""
        return self.account_number
    
    def get_holder_name(self):
        """Return the account holder name"""
        return self.holder_name
    
    def get_balance(self):
        """Return the current balance"""
        return self.balance
    
    def display_info(self):
        """Print account information"""
        print(f"\n--- Account Information ---")
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ${self.balance:.2f}")


# ============================================================================
# TEST THE ACCOUNT CLASS
# ============================================================================

if __name__ == "__main__":
    print("="*50)
    print("BANK MANAGEMENT SYSTEM")
    print("Program 1: Account Class")
    print("="*50)
    
    # Test 1: Create first account
    print("\n--- Test 1: Create Account 1 ---")
    account1 = Account("ACC001", "John Doe", 5000)
    account1.display_info()
    
    # Test 2: Create second account
    print("\n--- Test 2: Create Account 2 ---")
    account2 = Account("ACC002", "Jane Smith", 3000)
    account2.display_info()
    
    # Test 3: Create third account
    print("\n--- Test 3: Create Account 3 ---")
    account3 = Account("ACC003", "Bob Johnson", 7500)
    account3.display_info()
    
    # Test 4: Using getter methods
    print("\n--- Test 4: Using Getter Methods ---")
    print(f"Account 1 Number: {account1.get_account_number()}")
    print(f"Account 1 Holder: {account1.get_holder_name()}")
    print(f"Account 1 Balance: ${account1.get_balance():.2f}")
    
    print("\n" + "="*100)
    print("Program 1 Complete!")
    print("="*100)