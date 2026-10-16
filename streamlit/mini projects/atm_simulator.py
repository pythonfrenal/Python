
balance = 5000


def show_menu():
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def check_balance():
    print("Current Balance: ₹", balance)


def deposit():
    global balance

    amount = float(input("Enter deposit amount: ₹"))

    if amount <= 0:
        print("Please enter a valid amount!")
    else:
        balance += amount
        print("Amount deposited successfully!")
        print("Updated Balance: ₹", balance)


def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Please enter a valid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining Balance: ₹", balance)


# Main program
while True:
    show_menu()

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice! Please select 1-4.")
