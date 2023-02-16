# The BankAccount class simulates a bank account.

class BankAccount:
    
    # The __init__ method 
    
    def __init__(self):
        self.balance = float(1000.0)

    # The deposit method makes a deposit into the
    # account.

    def deposit(self, amount):
        self.balance += amount

    # The withdraw method withdraws an amount
    # from the account.

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Error: Insufficient funds')

    # The get_balance method returns the
    # account balance.

    def get_balance(self):
        return self.balance

    def set_balance(self, x):
        self.balance=x