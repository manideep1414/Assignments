class UserAccount:
    def __init__(self, username, pin, balance):
        self.username = username
        self.pin = pin
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. Balance: ₹{self.__balance}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Balance: ₹{self.__balance}")
        else:
            print("Insufficient balance.")


class ATM:
    def __init__(self):
        self.user = None

    def login(self, user, pin):
        if user.pin == pin:
            self.user = user
            print(f"Welcome, {user.username}!")
        else:
            print("Invalid PIN!")

    def deposit(self, amount):
        if self.user:
            self.user.deposit(amount)
        else:
            print("Login first.")

    def withdraw(self, amount):
        if self.user:
            self.user.withdraw(amount)
        else:
            print("Login first.")

    def check_balance(self):
        if self.user:
            print(f"Balance: ₹{self.user.get_balance()}")
        else:
            print("Login first.")


alice = UserAccount("Alice", 1234, 5000)
atm = ATM()

atm.login(alice, 1234)
atm.check_balance()
atm.deposit(1000)
atm.withdraw(2000)
atm.check_balance()
