import os
import random


def clear_terminal_screen():
    return os.system("clear || cls")


def rps_game():
    clear_terminal_screen()

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    game_images = [rock, paper, scissors]

    user_choice = int(input("\nWhat do you choose?\nEnter 0 for Rock,\n1 for Paper,\n2 for Scissors: "))
    print(f"You chose:\n{game_images[user_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{game_images[computer_choice]}")
    
    if user_choice >= 3 or user_choice < 0:
        clear_terminal_screen()
        print("\nYou entered an invalid option. YOU LOSE!\n")
    elif user_choice == 0 and computer_choice == 2:
        print("YOU WIN!\n")
    elif computer_choice == 0 and user_choice == 2:
        print("YOUS LOSE!\n")
    elif computer_choice > user_choice:
        print("YOU LOSE!\n")
    elif user_choice > computer_choice:
        print("YOU WIN!\n")
    elif computer_choice == user_choice:
        print("DRAW!\n")


rps_game()