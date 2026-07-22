class Customer:
    customer_counter = 1000
    
    def __init__(self, name, age, cnic, phone, address):
        Customer.customer_counter += 1
        self.customer_id = Customer.customer_counter
        self.name = name
        self.cnic = cnic
        self.age = age
        self.phone = phone
        self.address = address
        
    def display_info(self):
        print(f"Customer id: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"CNIC: {self.cnic}")
        print(f"Phone no: {self.phone}")
        print(f"Address: {self.address}")
        
    def __str__(self):
        return (
            f"\nCustomer ID: {self.customer_id}"
            f"\nName: {self.name}"
            f"\nAge: {self.age}"
            f"\nCNIC: {self.cnic}"
            f"\nPhone: {self.phone}"
            f"\nAddress: {self.address}")