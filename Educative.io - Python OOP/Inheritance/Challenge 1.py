'''
Implement a Banking Account
'''

class Account():
    tittle = None
    balance = None
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

    def something(self):
        print("FATHER CLASS")

class SavingsAccount(Account):
    interestRate = None
    def __init__(self, title, balance, interestRate):
        self.interestRate = interestRate
        Account.__init__(self, title,balance)

account = SavingsAccount("Mark", 5000, 5)
print(account.interestRate)
print(account.something())