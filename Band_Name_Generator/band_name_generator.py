import os


def clear_terminal_screen():
    return os.system("clear || cls")


def band_name_generator():
    clear_terminal_screen()
    print("Welcome to Band Name Generator!")

    while True:
        city_name_input = input("Enter town/city name: ")
        pet_name_input = input("Enter a pet's name: ")
        print(f"\nYour band name is: {city_name_input} {pet_name_input}\n")

        repeat_generator = input("Want to go again - 'yes' or 'no'? ").lower()

        if repeat_generator == 'yes':
            clear_terminal_screen()
        elif repeat_generator == 'no':
            clear_terminal_screen()
            print("Thank you for using Band Name Generator. Have a good day!\n")
            break
        else:
            clear_terminal_screen()
            print("Not a valid option. Try again.")


band_name_generator()