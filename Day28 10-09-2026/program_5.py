"""
BANK MANAGEMENT SYSTEM - STEP 5
================================
Program 5: Check Balance

WHAT WE ARE DOING:
- Add balance checking functionality to Account class
- Display current account balance
- Show balance in a formatted way
- Methods to check balance different ways
- Simple balance inquiry

NOTES FOR NEXT PROGRAM:
- Program 6 will add transaction validation
"""

class Account:
    """Simple Account class with deposit, withdraw and balance checking"""
    
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
    
    def get_account_number(self):
        return self.account_number
    
    def get_holder_name(self):
        return self.holder_name
    
    def get_balance(self):
        """Return the current balance"""
        return self.balance
    
    def check_balance(self):
        """
        Display current balance in formatted way
        
        Returns:
        - balance amount
        """
        print(f"\n--- Balance Inquiry ---")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Current Balance: ${self.balance:.2f}")
        return self.balance
    
    def has_sufficient_balance(self, amount):
        """
        Check if account has sufficient balance
        
        Parameters:
        - amount: amount to check
        
        Returns:
        - True if balance >= amount, False otherwise
        """
        if self.balance >= amount:
            print(f"✓ Sufficient balance available")
            return True
        else:
            print(f"✗ Insufficient balance")
            print(f"  Required: ${amount:.2f}")
            print(f"  Available: ${self.balance:.2f}")
            return False
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            print(f"Error: Deposit amount must be positive!")
            return False
        
        self.balance = self.balance + amount
        print(f"✓ Deposit successful: ${amount:.2f}")
        print(f"  New balance: ${self.balance:.2f}")
        return True
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            print(f"Error: Withdraw amount must be positive!")
            return False
        
        if amount > self.balance:
            print(f"Error: Insufficient balance!")
            print(f"  Your balance: ${self.balance:.2f}")
            return False
        
        self.balance = self.balance - amount
        print(f"✓ Withdrawal successful: ${amount:.2f}")
        print(f"  New balance: ${self.balance:.2f}")
        return True
    
    def display_info(self):
        """Print full account information"""
        print(f"\n--- Account Information ---")
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ${self.balance:.2f}")


# ============================================================================
# TEST BALANCE CHECKING FUNCTIONALITY
# ============================================================================

if __name__ == "__main__":
    print("="*50)
    print("BANK MANAGEMENT SYSTEM")
    print("Program 5: Check Balance")
    print("="*50)
    
    # Test 1: Create account
    print("\n--- Test 1: Create Account ---")
    account = Account("ACC001", "John Doe", 5000)
    account.display_info()
    
    # Test 2: Check balance using method
    print("\n--- Test 2: Check Balance ---")
    balance = account.check_balance()
    
    # Test 3: Check if has sufficient balance (yes)
    print("\n--- Test 3: Check if Can Withdraw $1000 ---")
    account.has_sufficient_balance(1000)
    
    # Test 4: Check if has sufficient balance (no)
    print("\n--- Test 4: Check if Can Withdraw $6000 ---")
    account.has_sufficient_balance(6000)
    
    # Test 5: After deposit, check balance
    print("\n--- Test 5: After Deposit, Check Balance ---")
    account.deposit(2000)
    account.check_balance()
    
    # Test 6: After withdrawal, check balance
    print("\n--- Test 6: After Withdrawal, Check Balance ---")
    account.withdraw(1500)
    account.check_balance()
    
    # Test 7: Multiple transactions then check
    print("\n--- Test 7: Multiple Transactions ---")
    account.deposit(500)
    account.withdraw(300)
    account.deposit(1000)
    account.check_balance()
    
    # Test 8: Get balance using getter method
    print("\n--- Test 8: Get Balance using Getter ---")
    current_balance = account.get_balance()
    print(f"Current balance from getter: ${current_balance:.2f}")
    
    # Test 9: Check balance is zero
    print("\n--- Test 9: Withdraw All Balance ---")
    current = account.get_balance()
    account.withdraw(current)
    account.check_balance()
    
    # Test 10: Check insufficient balance is empty
    print("\n--- Test 10: Check Insufficient Balance ---")
    account.has_sufficient_balance(100)
    
    print("\n" + "="*50)
    print("Program 5 Complete!")
    print("="*50)