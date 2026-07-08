"""
Project : Rock Paper Scissors Game
Author  : Swati Ranjita Swain
Language: Python 3

Description:
A professional command-line Rock-Paper-Scissors game
with score tracking, input validation, and replay option.
"""

import random


class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user, computer):
        if user == computer:
            return "Tie"

        if (
            (user == "rock" and computer == "scissors") or
            (user == "paper" and computer == "rock") or
            (user == "scissors" and computer == "paper")
        ):
            self.user_score += 1
            return "You Win"

        self.computer_score += 1
        return "Computer Wins"

    def display_score(self):
        print("\nCurrent Score")
        print("-" * 25)
        print(f"You      : {self.user_score}")
        print(f"Computer : {self.computer_score}")


def main():
    game = RockPaperScissors()

    print("=" * 45)
    print("      ROCK PAPER SCISSORS GAME")
    print("=" * 45)

    while True:

        user_choice = input(
            "\nChoose (rock/paper/scissors): "
        ).strip().lower()

        if user_choice not in game.choices:
            print("Invalid choice! Try again.")
            continue

        computer_choice = game.get_computer_choice()

        print(f"\nYour Choice     : {user_choice.title()}")
        print(f"Computer Choice : {computer_choice.title()}")

        result = game.determine_winner(
            user_choice,
            computer_choice
        )

        print(f"\nResult: {result}")

        game.display_score()

        play_again = input(
            "\nPlay Again? (Y/N): "
        ).strip().lower()

        if play_again != "y":
            break

    print("\nFinal Score")
    print("-" * 25)
    print(f"You      : {game.user_score}")
    print(f"Computer : {game.computer_score}")

    print("\nThank you for playing!")


if __name__ == "__main__":
    main()
