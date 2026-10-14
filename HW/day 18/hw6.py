try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Please enter a valid number!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

else:
    print("Result:", result)
    print("No errors! Everything went fine.")