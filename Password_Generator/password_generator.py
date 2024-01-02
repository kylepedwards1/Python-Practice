import os
import random


def clear_terminal_screen():
    return os.system("clear || cls")


def password_generator():
    clear_terminal_screen()

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_query = int(input("How many letters do you want? "))
    symbols_query = int(input("How many symbols do you want? "))
    numbers_query = int(input("How many numbers do you want? "))

    password_list = []

    for character in range(1, letters_query + 1):
        password_list.append(random.choice(letters))
    
    for symbol in range(1, symbols_query + 1):
        password_list += random.choice(symbols)
    
    for number in range(1, numbers_query + 1):
        password_list += random.choice(numbers)
    
    random.shuffle(password_list)

    password = ""
    for character in password_list:
        password += character
    
    print(f"\nYour password is: {password}\n")
    return password


password_generator()