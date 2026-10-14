class Bank:
    def __init__(self,Name,Balance):

        self.Name=Name
        self.balance=Balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def show_balance(self):
        return self.balance
B=Bank("Ajith",10000)
B.deposit(1000)
B.withdraw(200)
print(B.show_balance())




