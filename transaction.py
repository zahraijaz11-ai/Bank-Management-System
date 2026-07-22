from datetime import datetime


class Transaction:
    transaction_counter = 1000
    
    def __init__(self, transaction_type, amount):      
        Transaction.transaction_counter += 1   
        self.transaction_id = f"{self.transaction_counter}"
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = datetime.now().strftime("%d-%m-%Y")
        self.time = datetime.now().strftime("%I:%M:%S %p")
        
    def __str__(self):
        return (
            f"\nTransaction ID : {self.transaction_id}"
            f"\nType : {self.transaction_type}"
            f"\nAmount : {self.amount}"
            f"\nDate: {self.date}"
            f"\nTime: {self.time}"
        )
