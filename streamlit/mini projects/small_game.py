
import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def get_player_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()

    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        choice = input("Enter rock, paper, or scissors: ").lower()

    return choice


def check_winner(player, computer):
    if player == computer:
        return "Draw!"

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "scissors" and computer == "paper")
        or (player == "paper" and computer == "rock")
    ):
        return "You win!"

    else:
        return "Computer wins!"


def play_game():
    player = get_player_choice()
    computer = get_computer_choice()

    print("You chose:", player)
    print("Computer chose:", computer)
    print(check_winner(player, computer))


def main():
    print("Welcome to Rock, Paper, Scissors!")
    play_game()


if __name__ == "__main__":
    main()
