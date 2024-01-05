import os
from random import randint


def clear_terminal_screen():
    return os.system("clear || cls")


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """ Checks answer against guess. Returns the number of turns remaining. """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! It was {answer}.\n")


def set_difficulty():
    level = input("Choose a difficulty. Enter 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    clear_terminal_screen()
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("\nYou're out of guesses. YOU LOSE!\n")
            return 
        elif guess != answer:
            print("Guess again.")


game()