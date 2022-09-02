class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.get_balance():
            print("cannot withdraw more than %s" % self.get_balance())
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


user1 = BankAccount()
user1.deposit(10000)
user1.withdraw(10000)
print(user1.get_balance())
