from transaction import Transaction


class Account:
    account_counter = 5000

    def __init__(self, customer, account_type, initial_balance):
        Account.account_counter += 1
        
        self.account_number = f"Acc{Account.account_counter}"
        self.customer = customer
        self.account_type = account_type
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Enter Amount greater than 0")
            return
        self.balance += amount
        transaction = Transaction("Deposit", amount)
        self.transactions.append(transaction)
        print(f"Rs.{amount} deposited successfully")
        print(f"New Balance: Rs.{self.balance}")
        
    def withdrawal(self, amount):
        if amount <= 0:
            print("Enter Amount greater than 0")
            return
        if amount > self.balance:
            print("Insufficient Balance! ")
            return
        self.balance -= amount
        transaction = Transaction("Withdrawal", amount)
        self.transactions.append(transaction)
        print(f"Rs.{amount} withdrawn successfully! ")
        print(f"New Balance is Rs.{self.balance}")
    
    def show_transactions(self):
        if len(self.transactions) == 0:
            print("No transactions found!")
            return
        
        print("\nTransaction History: ")
        
        for transaction in self.transactions:
            print(transaction)
            
    def check_balance(self):
        print(f"Current Balance: Rs.{self.balance}")