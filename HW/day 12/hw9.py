# Ask user to guess a number until they get it correct.

secret_number = 7

guess = int(input("Guess the number: "))

while guess != secret_number:
    print("Wrong guess! Try again.")
    guess = int(input("Guess the number: "))

print("Correct! You guessed the number.")
