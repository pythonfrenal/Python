class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit successful. Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful. Balance:", self.balance)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print()
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)


# Creating object
account = BankAccount("Shahin", 10000)

account.deposit(5000)
account.withdraw(3000)
account.display_balance()