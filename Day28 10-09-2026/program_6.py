"""
BANK MANAGEMENT SYSTEM - STEP 6
================================
Program 6: Validate Transactions

WHAT WE ARE DOING:
- Add transaction validation to Account class
- Validate deposit amounts (positive, within limits)
- Validate withdraw amounts (positive, sufficient balance)
- Validate minimum balance rules
- Validate daily transaction limits
- Return validation status before performing transaction

NOTES FOR NEXT PROGRAM:
- Program 7 will add transaction history tracking
"""

from typing import Any


class Account:
    """Account class with transaction validation"""
    
    # Class constants for validation
    MIN_DEPOSIT = 0.01
    MAX_DEPOSIT = 1000000
    MIN_BALANCE = 0
    MAX_DAILY_TRANSACTIONS = 5
    
    def __init__(self, account_number, holder_name, initial_balance=0) -> None:
        self.account_number: Any = account_number
        self.holder_name: Any = holder_name
        self.balance: int = initial_balance
        self.daily_transactions = 0
    
    def get_account_number(self) -> Any:
        return self.account_number
    
    def get_holder_name(self) -> Any:
        return self.holder_name
    
    def get_balance(self):
        return self.balance
    
    def validate_deposit(self, amount) -> bool:
        """
        Validate deposit amount
        
        Parameters:
        - amount: amount to validate
        
        Returns:
        - True if valid, False otherwise
        """
        
        # Check if amount is positive
        if amount <= 0:
            print(f"✗ Error: Amount must be positive!")
            return False
        
        # Check minimum deposit
        if amount < self.MIN_DEPOSIT:
            print(f"✗ Error: Minimum deposit is ${self.MIN_DEPOSIT:.2f}")
            return False
        
        # Check maximum deposit
        if amount > self.MAX_DEPOSIT:
            print(f"✗ Error: Maximum deposit is ${self.MAX_DEPOSIT:.2f}")
            return False
        
        # Check daily transaction limit
        if self.daily_transactions >= self.MAX_DAILY_TRANSACTIONS:
            print(f"✗ Error: Daily transaction limit reached ({self.MAX_DAILY_TRANSACTIONS})")
            return False
        
        print(f"✓ Deposit validation passed: ${amount:.2f}")
        return True
    
    def validate_withdraw(self, amount) -> bool:
        """
        Validate withdraw amount
        
        Parameters:
        - amount: amount to validate
        
        Returns:
        - True if valid, False otherwise
        """
        
        # Check if amount is positive
        if amount <= 0:
            print(f"✗ Error: Amount must be positive!")
            return False
        
        # Check if sufficient balance
        if amount > self.balance:
            print(f"✗ Error: Insufficient balance!")
            print(f"  Available: ${self.balance:.2f}")
            print(f"  Requested: ${amount:.2f}")
            return False
        
        # Check if withdrawal keeps minimum balance
        remaining = self.balance - amount
        if remaining < self.MIN_BALANCE:
            print(f"✗ Error: Cannot go below minimum balance (${self.MIN_BALANCE:.2f})")
            return False
        
        # Check daily transaction limit
        if self.daily_transactions >= self.MAX_DAILY_TRANSACTIONS:
            print(f"✗ Error: Daily transaction limit reached ({self.MAX_DAILY_TRANSACTIONS})")
            return False
        
        print(f"✓ Withdrawal validation passed: ${amount:.2f}")
        return True
    
    def deposit(self, amount) -> bool:
        """Deposit money with validation"""
        if not self.validate_deposit(amount):
            return False
        
        self.balance = self.balance + amount
        self.daily_transactions: int = self.daily_transactions + 1
        print(f"✓ Deposit successful: ${amount:.2f}")
        print(f"  New balance: ${self.balance:.2f}")
        return True
    
    def withdraw(self, amount) -> bool:
        """Withdraw money with validation"""
        if not self.validate_withdraw(amount):
            return False
        
        self.balance = self.balance - amount
        self.daily_transactions: int = self.daily_transactions + 1
        print(f"✓ Withdrawal successful: ${amount:.2f}")
        print(f"  New balance: ${self.balance:.2f}")
        return True
    
    def display_info(self) -> None:
        """Print account information"""
        print(f"\n--- Account Information ---")
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ${self.balance:.2f}")
        print(f"Daily Transactions: {self.daily_transactions}/{self.MAX_DAILY_TRANSACTIONS}")


# ============================================================================
# TEST TRANSACTION VALIDATION
# ============================================================================

if __name__ == "__main__":
    print("="*50)
    print("BANK MANAGEMENT SYSTEM")
    print("Program 6: Validate Transactions")
    print("="*50)
    
    # Test 1: Create account
    print("\n--- Test 1: Create Account ---")
    account: Account[str, str] = Account("ACC001", "John Doe", 5000)
    account.display_info()
    
    # Test 2: Valid deposit
    print("\n--- Test 2: Valid Deposit $500 ---")
    account.deposit(500)
    
    # Test 3: Deposit negative amount
    print("\n--- Test 3: Try Negative Deposit ---")
    account.deposit(-200)
    
    # Test 4: Deposit zero
    print("\n--- Test 4: Try Zero Deposit ---")
    account.deposit(0)
    
    # Test 5: Deposit too large
    print("\n--- Test 5: Try Deposit Over Limit ($2000000) ---")
    account.deposit(2000000)
    
    # Test 6: Valid withdrawal
    print("\n--- Test 6: Valid Withdrawal $1000 ---")
    account.withdraw(1000)
    
    # Test 7: Withdraw negative amount
    print("\n--- Test 7: Try Negative Withdrawal ---")
    account.withdraw(-500)
    
    # Test 8: Withdraw more than balance
    print("\n--- Test 8: Try Withdrawal Over Balance ($6000) ---")
    account.withdraw(6000)
    
    # Test 9: Multiple valid transactions
    print("\n--- Test 9: Multiple Valid Transactions ---")
    account.deposit(1000)
    account.withdraw(500)
    account.deposit(2000)
    account.withdraw(1000)
    account.display_info()
    
    # Test 10: Hit daily transaction limit
    print("\n--- Test 10: Hit Daily Transaction Limit ---")
    account.deposit(100)  # This is the 5th transaction
    account.display_info()
    print("\nAttempting 6th transaction (should fail):")
    account.deposit(100)
    
    print("\n" + "="*50)
    print("Program 6 Complete!")
    print("="*50)