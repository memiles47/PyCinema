class Account:
    def __init__(self, name, balance, minBalance):
        self.name = name
        self.balance = balance
        self.minBalance = minBalance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.minBalance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: {} Pounds".format(self.balance))

class Checking(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, minBalance = -1000)

    def __str__(self):
        return "{}'s Checking Accunt : Balance {} Pounds".format(self.name, self.balance)

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, minBalance = 0)

    def __str__(self):
        return "{}'s Savings Accunt : Balance {} Pounds".format(self.name, self.balance)
