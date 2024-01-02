import os
import random
from hangman_words import word_list
from hangman_art import logo


def clear_terminal_screen():
    return os.system("clear || cls")


def hangman_game():
    clear_terminal_screen()
    print(logo)


hangman_game()