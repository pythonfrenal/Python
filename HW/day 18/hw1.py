try:
    num = float(input("Enter a number: "))
    square = num ** 2
    print("Square:", square)

except ValueError:
    print("Please enter a valid number.")