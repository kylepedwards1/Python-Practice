import os


def clear_terminal_screen():
    return os.system("clear || cls")


def tip_calculator():
    clear_terminal_screen()
    print("Tip calculator activated.")

    bill = float(input("Enter total bill: $"))
    tip = int(input("Enter tip amount - 10, 12, or 15: "))
    people = int(input("Enter amount of people in your party: "))

    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)

    print(f"\nEach person should pay: ${final_amount}\n")
    return final_amount


tip_calculator()