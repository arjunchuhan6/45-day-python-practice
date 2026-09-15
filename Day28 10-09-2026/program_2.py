"""
BANK MANAGEMENT SYSTEM - STEP 2
================================
Program 2: Create Customer Class

WHAT WE ARE DOING:
- Create a simple Customer class to store customer information
- Store: Customer ID, Name, Email, Phone
- Methods to manage customer accounts
- Customers can have multiple accounts

NOTES FOR NEXT PROGRAM:
- Program 3 will add deposit functionality
"""

# First, we use the Account class from Program 1
class Account:
    """Simple Account class from Program 1"""
    
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
    
    def get_account_number(self):
        return self.account_number
    
    def get_balance(self):
        return self.balance


class Customer:
    """
    A simple class to represent a bank customer
    Attributes: customer_id, name, email, phone, accounts (list)
    """
    
    def __init__(self, customer_id, name, email, phone):
        """
        Create a new customer
        
        Parameters:
        - customer_id: unique ID (example: "CUST001")
        - name: customer's full name (example: "John Doe")
        - email: customer's email (example: "john@email.com")
        - phone: customer's phone (example: "555-1234")
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.accounts = []  # List to store accounts
        print(f"Customer {customer_id} created: {name}")
    
    def get_customer_id(self):
        """Return customer ID"""
        return self.customer_id
    
    def get_name(self):
        """Return customer name"""
        return self.name
    
    def add_account(self, account):
        """
        Add an account to this customer
        
        Parameters:
        - account: Account object to add
        """
        self.accounts.append(account)
        print(f"Account {account.get_account_number()} added to {self.name}")
    
    def get_accounts(self):
        """Return list of all accounts"""
        return self.accounts
    
    def get_total_balance(self):
        """Calculate total balance across all accounts"""
        total = 0
        for account in self.accounts:
            total = total + account.get_balance()
        return total
    
    def display_info(self):
        """Print customer information"""
        print(f"\n--- Customer Information ---")
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Number of Accounts: {len(self.accounts)}")
        print(f"Total Balance: ${self.get_total_balance():.2f}")
    
    def display_accounts(self):
        """Print all accounts of this customer"""
        print(f"\n--- Accounts for {self.name} ---")
        if len(self.accounts) == 0:
            print("No accounts found")
        else:
            for account in self.accounts:
                print(f"Account: {account.get_account_number()} | Balance: ${account.get_balance():.2f}")


# ============================================================================
# TEST THE CUSTOMER CLASS
# ============================================================================

if __name__ == "__main__":
    print("="*50)
    print("BANK MANAGEMENT SYSTEM")
    print("Program 2: Customer Class")
    print("="*50)
    
    # Test 1: Create first customer
    print("\n--- Test 1: Create Customer 1 ---")
    customer1 = Customer("CUST001", "John Doe", "john@email.com", "555-1234")
    
    # Test 2: Create second customer
    print("\n--- Test 2: Create Customer 2 ---")
    customer2 = Customer("CUST002", "Jane Smith", "jane@email.com", "555-5678")
    
    # Test 3: Create accounts for customer 1
    print("\n--- Test 3: Add Accounts to Customer 1 ---")
    acc1 = Account("ACC001", "John Doe", 5000)
    acc2 = Account("ACC002", "John Doe", 3000)
    customer1.add_account(acc1)
    customer1.add_account(acc2)
    
    # Test 4: Create account for customer 2
    print("\n--- Test 4: Add Account to Customer 2 ---")
    acc3 = Account("ACC003", "Jane Smith", 7500)
    customer2.add_account(acc3)
    
    # Test 5: Display customer 1 information
    print("\n--- Test 5: Display Customer 1 Information ---")
    customer1.display_info()
    customer1.display_accounts()
    
    # Test 6: Display customer 2 information
    print("\n--- Test 6: Display Customer 2 Information ---")
    customer2.display_info()
    customer2.display_accounts()
    
    # Test 7: Test getter methods
    print("\n--- Test 7: Using Getter Methods ---")
    print(f"Customer ID: {customer1.get_customer_id()}")
    print(f"Customer Name: {customer1.get_name()}")
    print(f"Total Balance: ${customer1.get_total_balance():.2f}")
    
    print("\n" + "="*50)
    print("Program 2 Complete!")
    print("="*50)
