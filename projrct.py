#Create a Customer class that stores name and account_balance. 
#Implement methods to deposit, withdraw, and check balance. 
#Ensure withdrawals cannot exceed the available balance. 

class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: Rs{amount}. New balance: Rs{self.balance}.")
        else:
            print("Enter an amount...")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw: Rs{amount}. New balance: Rs{self.balance}.")
        else:
            print("Invalid amount.")

    def check_balance(self):
        print(f"Balance: Rs{self.balance}.")

customer = Customer("Dark Knight")
customer.check_balance()
customer.deposit(50)
customer.withdraw(20)
customer.withdraw(100)
customer.check_balance()