
# import random

# def generate_number():
#     return random.randint(1, 100)


# def get_guess():
#     return int(input("Enter your guess (1-100): "))


# def check_guess(guess, number):
#     if guess > number:
#         print("Too High!")
#         return False
#     elif guess < number:
#         print("Too Low!")
#         return False
#     else:
#         print("Correct!")
#         return True


# def play_game():
#     number = generate_number()
#     attempts = 0

#     while True:
#         try:
#             guess = get_guess()
#             attempts += 1

#             if check_guess(guess, number):
#                 break

#         except ValueError:
#             print("Please enter a valid number!")

#     print("Attempts =", attempts)


# def main():
#     print("Welcome to the Number Guessing Game!")
#     print("Guess a number between 1 and 100.")
#     play_game()


# if __name__ == "__main__":
#     main()




import random

def generate_number():
    return random.randint(1, 100)


def get_guess():
    return int(input("Enter your guess (1-100): "))


def check_guess(guess, number):
    if guess > number:
        print("Too High!")
        return False
    elif guess < number:
        print("Too Low!")
        return False
    else:
        print("Correct!")
        return True


def play_game():
    number = generate_number()
    attempts = 0

    while True:
        try:
            guess = get_guess()

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue

            attempts += 1

            if check_guess(guess, number):
                break

        except ValueError:
            print("Invalid input! Please enter a number.")

    print("Attempts =", attempts)


def main():
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")
    play_game()


if __name__ == "__main__":
    main()
