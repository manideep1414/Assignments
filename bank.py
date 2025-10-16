class Bank:
    def __init__(self,acc_holder,balance):
        self.acc_holder = acc_holder
        self.balance = balance
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.balance = balance
        
    def display(self):
        print(f"Account Holder={self.acc_holder}",f"Balance={self.balance}")
        
    def deposit(self,amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else: 
            self.balance += amount
            print(f"The deposit amount is {amount}. Balance: ₹{self.balance:.2f}")
        
    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter the amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"The withdrawed amount is {amount}. Balance: ₹{self.balance:.2f}")    
    
            
          
b1=Bank("A",2000)
b2=Bank("B",2000)
b3=Bank("C",2000)
b4=Bank("D",-100)

b1.display()
b2.display()   
b3.display()
b4.display()

b3.deposit(10)
b3.display()

b2.withdraw(10)
b2.display()

b1.withdraw(2010)
b1.display()

               