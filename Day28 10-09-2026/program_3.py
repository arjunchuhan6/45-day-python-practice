"""
BANK MANAGEMENT SYSTEM - STEP 3
================================
Program 3: Deposit Money

WHAT WE ARE DOING:
- Add deposit functionality to Account class
- Customers can deposit money into their accounts
- Check if deposit amount is valid
- Update account balance after deposit
- Show deposit confirmation

NOTES FOR NEXT PROGRAM:
- Program 4 will add withdraw functionality
"""

class Account:
    """Simple Account class with deposit functionality"""
    
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
        """
        Deposit money into the account
        
        Parameters:
        - amount: amount to deposit (must be positive)
        
        Returns:
        - True if successful, False if failed
        """
        
        # Check if amount is positive
        if amount <= 0:
            print(f"Error: Deposit amount must be positive! (entered: {amount})")
            return False
        
        # Add to balance
        self.balance = self.balance + amount
        print(f"✓ Deposit successful: ${amount:.2f}")
        print(f"  New balance: ${self.balance:.2f}")
        return True
    
    def display_info(self):
        """Print account information"""
        print(f"\n--- Account Information ---")
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ${self.balance:.2f}")


# ============================================================================
# TEST DEPOSIT FUNCTIONALITY
# ============================================================================

if __name__ == "__main__":
    print("="*50)
    print("BANK MANAGEMENT SYSTEM")
    print("Program 3: Deposit Money")
    print("="*50)
    
    # Test 1: Create account
    print("\n--- Test 1: Create Account ---")
    account = Account("ACC001", "John Doe", 1000)
    account.display_info()
    
    # Test 2: Deposit positive amount
    print("\n--- Test 2: Deposit $500 ---")
    account.deposit(500)
    account.display_info()
    
    # Test 3: Deposit another amount
    print("\n--- Test 3: Deposit $1500 ---")
    account.deposit(1500)
    account.display_info()
    
    # Test 4: Try to deposit negative amount
    print("\n--- Test 4: Try to Deposit Negative Amount ---")
    account.deposit(-200)
    account.display_info()
    
    # Test 5: Try to deposit zero
    print("\n--- Test 5: Try to Deposit Zero ---")
    account.deposit(0)
    account.display_info()
    
    # Test 6: Deposit decimal amount
    print("\n--- Test 6: Deposit $50.75 ---")
    account.deposit(50.75)
    account.display_info()
    
    # Test 7: Multiple deposits
    print("\n--- Test 7: Multiple Deposits ---")
    print("Depositing $100 + $200 + $300...")
    account.deposit(100)
    account.deposit(200)
    account.deposit(300)
    account.display_info()
    
    print("\n" + "="*50)
    print("Program 3 Complete!")
    print("="*50)