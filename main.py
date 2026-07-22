from customer import Customer
from account import Account

customer1 = Customer(
    "zahra",
    22,
    "35201-0855734-2",
    "03214059574",
    "Lahore\n"
)
customer2 = Customer(
    "Zunaira",
    22,
    "35402-0866538-2",
    "03147658976",
    "Islamabad"
)
customer1.display_info()
customer2.display_info()
print("\nTotal Customers created:")
print(Customer.customer_counter - 1000)

accounts = []
account1 = Account(customer1, "Saving", 10000)
account2 = Account(customer2, "Current", 96700)
accounts.append(account1)
accounts.append(account2)

while True:   
    print("\n----Bank Management System----")
    print("1. Select existing account ")
    print("2. create a new account ")
    print("3. Exit")
    
    try:
        main_choice = int(input("Enter your choice: "))
    except ValueError:
        print("\nPlease enter an integer only!")
        continue
    
    if main_choice == 1:
        pass
    elif main_choice == 2:
        print("\n------ Create New Account ------")
        name = input("Enter name: ")
        try:
            cnic = int(input("Enter CNIC(without characters): "))
            phone = int(input("Enter Number: "))
            while True:
                age = int(input("Enter age:"))
                if age <= 0:
                    print("\nage must be great than 0.")
                    continue
                break
            while True:
                balance = float(input("Enter initial balance: "))
                if balance <= 0:
                    print("Enter a valid amount! ")
                    continue
                break
        except ValueError:
            print("\nPlease enter an integer only!")
            continue
        address = input("Enter Address:")
        try:
            print("1. Savings")
            print("2. Current")
            account_type = int(input("Enter account type:"))
        except ValueError:
            print("\nPlease enter an integer only!")
            continue   
        
        if account_type == 1:
            account_type = "Savings"   
        elif account_type == 2:
            account_type = "Current" 
        else:
            break
    
        new_customer = Customer(
            name,
            age,
            cnic,
            phone,
            address
        )
        new_account = Account(
            new_customer,
            account_type,
            balance
        )
        accounts.append(new_account)
        print("\nAccount created successfully!!")
        print(f"\nCustomer ID: {new_customer.customer_id}")
        print(f"Account Number: {new_account.account_number}")
        new_customer.display_info()
    
    elif main_choice == 3:
        print("\nThank you!")   
        break
    else:
        print("\nInvalid option!")
        continue
    print("\n=====Available Accounts=====")
    
    for i, account in enumerate(accounts, start=1):
        account_description = (
            f"{i}. {account.customer.name} "
            f"({account.account_number}) - {account.account_type}"
        )
        print(account_description)
        
    print(f"{len(accounts)+1}. Exit")
    try:
        customer_choice = int(input("Select an account: "))
    except ValueError:
        print("\nPlease enter an integer only!")
        continue
    
    if 1 <= customer_choice <= len(accounts):
        selected_account = accounts[customer_choice-1]
    elif customer_choice == len(accounts)+1:
        print("\nThank you!!")
        break
    else:
        print("\nInvalid choice! ")
        continue
    while True:
        print("\n--------MENU--------")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. check Balance")
        print("4. Show Transaction")
        print("5. Back")
        print("6. Exit")
    
        try:
            choice = int(input("\nEnter your choice from the Menu: "))
        except ValueError:
            print("\nPlease enter an integer only!")
            continue
        if choice == 1:
            try:
                amount = float(input("\nEnter deposit amount: "))
            except ValueError:
                print("\nIntegers only!")
                continue
            selected_account.deposit(amount)
        elif choice == 2:
            try:
                amount = float(input("\nEnter withdrawal amount: "))
            except ValueError:
                print("\nIntegers only!")
                continue
            selected_account.withdrawal(amount)
        elif choice == 3:
            selected_account.check_balance()
        elif choice == 4:
            selected_account.show_transactions()
        elif choice == 5:
            break
        elif choice == 6:
            print("\nTHANK YOU FOR USING ZAHRA'S BANK MANAGEMENT SYSTEM!")
            exit()
        else:
            print("\nInvalid option! ")
            continue
        