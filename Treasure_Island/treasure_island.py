import os 


def clear_terminal_screen():
    return os.system("clear || cls")


def treasure_island():
    clear_terminal_screen()
    user_name_input = input("\nWhat's your name traveler? ")
    opening_exposition_text = f"""
    Welcome {user_name_input}. While dining in a noisy tavern, you couldn't help overhearing rumors of a 
    secret treasure hidden on a mysterious island.
    The next morning, you left the inn and town that you were staying at and
    walked upon a dusty dirt road.
    """

    print(opening_exposition_text)
    
    fork_in_the_road_input = input("Later on, you came to a fork in the road.\nDid you go 'left' or 'right'? ").lower()

    if fork_in_the_road_input == 'right':
        second_exposition_text = """
        You went right. Later on, you came to a huge lake with an island in the center of it.
        Wait a minute...THAT'S IT! That's the mysterious island that you heard about in the tavern.
        """
        print(second_exposition_text)

        swim_or_wait_input = input("The question is, do you 'wait' or do you try to 'swim' across? ").lower()
        if swim_or_wait_input == 'wait':
            third_exposition_text = """
            You waited. Some time later, a small boat arrived. 
            Hopping on board, you find that this small boat has no captain. 
            Must be a magical boat...
            Anyway, the boat takes you to the mysterious island in the middle of the lake.
            """
            print(third_exposition_text)

            doors_input = input("On this island you find three doors - one 'red', one 'blue', one 'yellow'.\nWhich one do you go through? ").lower()
            if doors_input == 'red':
                print("\nYou opened the red door and was consumed by a Hellish conflagration.\nGAME OVER!\n")
            elif doors_input == 'blue':
                print("\nYou opened the blue door and was devoured by foul beasts.\nGAME OVER!\n")
            elif doors_input == 'yellow':
                print("\nYou opened the yellow door and FOUND THE TREASURE! FINALLY! YOU WIN!\n")
            else:
                clear_terminal_screen()
                print(f"\nThat wasn't a valid option {user_name_input}.\nYou died from Sudden Death Syndrome.\nGAME OVER!\n")
        elif swim_or_wait_input == 'swim':
            print("\nYou tried to swim across.\nYou grew tired halfway there and drowned in the huge lake.\nGAME OVER!")
        else:
            clear_terminal_screen()
            print(f"\nThat wasn't a valid option {user_name_input}.\nYou died from Sudden Death Syndrome.\nGAME OVER!\n")
    elif fork_in_the_road_input == 'left':
        print("\nYou went left.\nLater on, you were ambushed and murdered by bandits.\nGAME OVER!\n")
    else:
        clear_terminal_screen()
        print(f"\nThat wasn't a valid option {user_name_input}.\nYou died from Sudden Death Syndrome.\nGAME OVER!\n")


treasure_island()