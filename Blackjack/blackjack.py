import os
import random
from art import logo


def clear_terminal_screen():
    return os.system("clear || cls")


def deal_card():
    """ Returns a random card from the deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """ Take a list of cards and return the score calculated from the cards. """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "\nYou went over. YOU LOSE!\n"
    
    if user_score == computer_score:
        return "\nDRAW!\n"
    elif computer_score == 0:
        return "\nOpponent has Blackjack! YOU LOSE!\n"
    elif user_score == 0:
        return "\nBLACKJACK! YOU WIN!\n"
    elif user_score > 21:
        return "\nYou went over. YOU LOSE!\n"
    elif computer_score > 21:
        return "\nYour opponent went over. YOU WIN!\n"
    elif user_score > computer_score:
        return "\nYOU WIN!\n"
    else:
        return "\nYOU LOSE!\n"


def play_game():
    clear_terminal_screen()
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(
            f"\nYour cards: {user_cards}, current score: {user_score}",
            f"\nComputer's first card: {computer_cards[0]}"
        )

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Enter 'yes' to get another card or 'no' to pass: ").lower()
            if user_should_deal == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(
        f"\nYour final hand: {user_cards}, final score: {user_score}",
        f"\nComputer's final hand: {computer_cards}, final score: {computer_score}",
        compare(user_score, computer_score)
    )


clear_terminal_screen()

while input("\nWant to play a game of Blackjack? Enter 'yes' or 'no': ") == "yes":
    clear_terminal_screen()
    play_game()                