# The BankAccount class simulates a bank account.

class BankAccount:
    """
    The BankAccount class represents a bank account.

    Attributes:
        __balance (float): The current balance of the account.

    Methods:
        deposit(amount): Makes a deposit into the account.
        withdraw(amount): Withdraws an amount from the account.
        get_balance(): Returns the account balance.
        set_balance(x): Sets the account balance to the specified value.
    """

    def __init__(self):
        """
        Initializes a new instance of the BankAccount class.
        The initial balance is set to 0.0.
        """
        self.__balance = float(0.0)

    def deposit(self, amount):
        """
        Makes a deposit into the account.

        Args:
            amount (float): The amount to be deposited.

        Returns:
            None
        """
        self.__balance += amount

    def withdraw(self, amount):
        """
        Withdraws an amount from the account.

        Args:
            amount (float): The amount to be withdrawn.

        Returns:
            None
        """
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')

    def get_balance(self):
        """
        Returns the account balance.

        Returns:
            float: The current balance of the account.
        """
        return self.__balance

    def set_balance(self, x):
        """
        Sets the account balance to the specified value.

        Args:
            x (float): The new balance value.

        Returns:
            None
        """
        self.__balance = x
