'''
Handling a Bank Account
'''

class Account:
    def __init__(self, title = None, balance = 0, amount):
        self.title = title
        self.balance = balance
    def getBalance(self):
        return (self.balance)

    def deposit(self, amount):
        a = self.amount + self.balance
        return

    def withdrawal(self, amount):
        a = self.balance - self.amount
        return

class SavingsAccount(Account):
    def __init__(self, title = None, balance = 0, interestRate = 0):
        self.interestRate = interestRate
        super().__init__(title, balance)

    def interestAmount(self):
        a = self.interestRate * self.balance
        return (a / 100)

demo = SavingsAccount("Mark", 2000, 5)
print(demo.withdrawal(50))

