"""
BANK MANAGEMENT SYSTEM - STEP 4
================================
Program 4: Withdraw Money

WHAT WE ARE DOING:
- Add withdraw functionality to Account class
- Customers can withdraw money from their accounts
- Check if withdraw amount is valid (positive)
- Check if customer has enough balance
- Update account balance after withdrawal
- Show withdrawal confirmation

NOTES FOR NEXT PROGRAM:
- Program 5 will add check balance functionality
"""

class Account:
    """Simple Account class with deposit and withdraw functionality"""
    
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
    
    def get_account_number(self):
        return self.account_number
    
    def get_holder_name(self):
        return self.holder_name
    
    def get_balance(self):
        return self.balance
    
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
        """
        Withdraw money from the account
        
        Parameters:
        - amount: amount to withdraw (must be positive)
        
        Returns:
        - True if successful, False if failed
        """
        
        # Check if amount is positive
        if amount <= 0:
            print(f"Error: Withdraw amount must be positive!")
            return False
        
        # Check if enough balance
        if amount > self.balance:
            print(f"Error: Insufficient balance!")
            print(f"  Your balance: ${self.balance:.2f}")
            print(f"  Requested: ${amount:.2f}")
            return False
        
        # Subtract from balance
        self.balance = self.balance - amount
        print(f"✓ Withdrawal successful: ${amount:.2f}")
        print(f"  New balance: ${self.balance:.2f}")
        return True
    
    def display_info(self):
        """Print account information"""
        print(f"\n--- Account Information ---")
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ${self.balance:.2f}")


# ============================================================================
# TEST WITHDRAW FUNCTIONALITY
# ============================================================================

if __name__ == "__main__":
    print("="*50)
    print("BANK MANAGEMENT SYSTEM")
    print("Program 4: Withdraw Money")
    print("="*50)
    
    # Test 1: Create account
    print("\n--- Test 1: Create Account with $5000 ---")
    account = Account("ACC001", "John Doe", 5000)
    account.display_info()
    
    # Test 2: Withdraw valid amount
    print("\n--- Test 2: Withdraw $1000 ---")
    account.withdraw(1000)
    account.display_info()
    
    # Test 3: Withdraw another amount
    print("\n--- Test 3: Withdraw $500 ---")
    account.withdraw(500)
    account.display_info()
    
    # Test 4: Try to withdraw more than balance
    print("\n--- Test 4: Try to Withdraw $5000 (more than balance) ---")
    account.withdraw(5000)
    account.display_info()
    
    # Test 5: Try to withdraw negative amount
    print("\n--- Test 5: Try to Withdraw -$200 ---")
    account.withdraw(-200)
    account.display_info()
    
    # Test 6: Try to withdraw zero
    print("\n--- Test 6: Try to Withdraw $0 ---")
    account.withdraw(0)
    account.display_info()
    
    # Test 7: Withdraw all remaining balance
    print("\n--- Test 7: Withdraw Remaining Balance ---")
    current_balance = account.get_balance()
    print(f"Current balance: ${current_balance:.2f}")
    account.withdraw(current_balance)
    account.display_info()
    
    # Test 8: Try to withdraw from empty account
    print("\n--- Test 8: Try to Withdraw from Empty Account ---")
    account.withdraw(100)
    account.display_info()
    
    print("\n" + "="*50)
    print("Program 4 Complete!")
    print("="*50)