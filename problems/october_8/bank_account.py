
# Decorator
def transaction_decorator(func):
    def wrapper(*args, **kwargs):
        print("Transaction Started")
        result = func(*args, **kwargs)
        print("Transaction Completed")
        return result
    return wrapper


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        self.transactions = []

    # Deposit money
    @transaction_decorator
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero!")

        self.__balance += amount
        self.transactions.append(amount)
        print("Deposited:", amount)

    # Withdraw money
    @transaction_decorator
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero!")

        if amount > self.__balance:
            print("Insufficient balance!")
            return

        self.__balance -= amount
        self.transactions.append(-amount)
        print("Withdrawn:", amount)

    # Display balance
    def display_balance(self):
        print("Current Balance:", self.__balance)

    # Generate report
    def report(self):
        # Nested function
        def transaction_count():
            return len(self.transactions)

        print("Total Transactions:", transaction_count())

        # Lambda function for 5% bonus
        bonus = lambda balance: balance * 0.05
        bonus_amount = bonus(self.__balance)

        print("Final Balance:", self.__balance)
        print("5% Bonus:", bonus_amount)
        print("Balance with Bonus:", self.__balance + bonus_amount)


# Main program
try:
    initial_balance = float(input("Enter initial balance: "))

    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative!")

    account = BankAccount(initial_balance)

    transactions = [1000, 2500, 500, 3000]

    # Process transactions using a for loop
    for i, amount in enumerate(transactions):
        if i == 2:
            account.withdraw(amount)
        else:
            account.deposit(amount)

    # Display balance and report
    account.display_balance()
    account.report()

except ValueError as e:
    print("Invalid amount:", e)
