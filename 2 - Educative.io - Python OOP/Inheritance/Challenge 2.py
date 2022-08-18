'''
Handling a Bank Account
'''
class Account:
    def __init__(self, title = None, balance = 0):
        self.title = title
        self.balance = balance
    def getBalance(self):
        return (self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return (self.balance)

    def withdrawal(self, amount):
        self.balance = self.balance - amount
        return (self.balance)

class SavingsAccount(Account):
    def __init__(self, title = None, balance = 0, interestRate = 0):
        self.interestRate = interestRate
        super().__init__(title, balance)

    def interestAmount(self):
        a = self.interestRate * self.balance / 100
        return a

demo = SavingsAccount("Mark", 2000, 5)
print("Initial balance:", demo.getBalance())
print("Balance after withdrawal:", demo.withdrawal(200))
print("Balance after deposit:", demo.deposit(200))
print("Interest on current balance:", demo.interestAmount())

