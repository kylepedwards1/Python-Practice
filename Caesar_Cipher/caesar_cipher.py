import os 


def clear_terminal_screen():
    return os.system("clear || cls")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    
    for character in start_text:
        if character in alphabet:
            position = alphabet.index(character)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += character
    
    print(f"\nHere's the {cipher_direction}d result: {end_text}\n")


should_end = False
while not should_end:
    clear_terminal_screen()
    direction = input("\nEnter 'encode' to encrypt, 'decode' to decrypt: ")
    text = input("Enter your message: ").lower()
    shift = int(input("Enter the shift number: "))

    shift = shift % 26
    
    caesar_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Enter 'yes' to restart the program, 'no' to exit the program: ")
    if restart == "no":
        clear_terminal_screen()
        should_end = True
        print("\nThank you for using Caesar Cipher. Goodbye.\n")