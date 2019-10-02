
import random

VALID_OPTIONS = ["rock", "paper", "scissors"]

def determine_winner(choice1, choice2):
    """
    Determines the winner between two choices from the options: "rock", "paper", and "scissors", according to the following logic:

    Winner Logic:
      + "rock" beats "scissors"
      + "scissors" beats "paper"
      + "paper" beats "rock"
      + same selections (e.g. "rock" vs. "rock") result in a Tie

    Examples:
        determine_winner("rock", "paper")
        determine_winner("rock", "rock")
        etc.

    Returns: either the winning choice (e.g. "paper"), or None if there is a Tie.
    """

    winner = "TODO" # TODO: determine the winner between choice1 and choice2

    return winner

if __name__ == "__main__":

    user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

    print("--------------")
    if user_choice.lower() in VALID_OPTIONS:
        print("You chose:", user_choice)
    else:
        print("Expecting one of: 'rock', 'paper', or 'scissors' (without the quotation marks). Please try again.")
        exit()

    computer_choice = random.choice(VALID_OPTIONS)
    print("The computer chose:", computer_choice)

    winning_choice = None # TODO: determine_winner(user_choice, computer_choice)
    if winning_choice:
        if winning_choice == user_choice:
            print("Congratulations, you won!")
        elif winning_choice == computer_choice:
            print("Oh, the computer won. It's ok.")
    else:
        print("Oh, it's a tie.")

    print("--------------")
    print("Thanks for playing. Please play again!")
