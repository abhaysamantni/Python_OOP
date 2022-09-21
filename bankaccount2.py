# The BankAccount class simulates a bank account.

class BankAccount:
    
    # The __init__ method accepts an argument for
    # the account's balance. It is assigned to
    # the __balance attribute.
    
    def __init__(self, bal):
        self.balance = bal

    # The deposit method makes a deposit into the
    # account.


    # The get_balance method returns the
    # account balance.

    def get_balance(self):
        return self.balance

    # The __str__ method returns a string
    # indicating the object's state.

#    def __str__(self):
#        return 'The balance is $' + format(self.__balance, ',.2f')
