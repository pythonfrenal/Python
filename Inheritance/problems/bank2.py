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


# Ask user for account details
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

# Create account
account = BankAccount(name, balance)

# Ask user for deposit amount
deposit_amount = float(input("Enter deposit amount: "))
account.deposit(deposit_amount)

# Ask user for withdrawal amount
withdraw_amount = float(input("Enter withdrawal amount: "))
account.withdraw(withdraw_amount)

# Display final balance
account.display_balance()