#!/usr/bin/env python3

import sys

donor_db = {"Wassily Kandinsky": [43928.13, 131.34, 1928.0],
            "Jasper Johns": [3134.43, 153.34],
            "Mark Rothko": [135353.33],
            "Richard Serra": [153757.87, 28457.12, 1293451.0],
            "Yves Tanguy": [1534.23, 2542.19]}

PROMPT = "\n".join(("Type a number from the options below",
        "1 - Send a Thank You to a single donor",
        "2 - Create a Report",
        "3 - Send letters to all donors",
        "4 - Quit\n"))


def thank_you():
    thanks = True
    while thanks:
        user_in = input("Type List to view all donor names, type a current donor name, or type the name of a new donor: ")
        if user_in.lower() == "list": 
            for key in donor_db:
                print(key)
        else:
            for key, value in donor_db.items():
                if user_in.title() == key:
                    user_in = user_in.title()
                    donation = float(input(f"Add a donation amount for {key}: $"))
                    donor_db[key].append(donation)
                    print(f"\nDear {key},\n\nThank you so much for your donation of ${value[-1]}.\n\nSincerely,\n\nThe Mailroom\n")
                    thanks = False
                    break 
            else:
                user_in = user_in.title()
                donation = float(input(f"Add a donation amount for {user_in}: $"))
                donor_db[user_in] = [donation]
                print(f"\nDear {user_in},\n\nThank you so much for your donation of ${donation}.\n\nSincerely,\n\nThe Mailroom\n")
                thanks = False


def report():
    print("{:<26}{}{}{}".format("Donor Name", "| Total Given ", "| Num Gifts ", "| Average Gift"))
    print("------------------------------------------------------------------")
    for key, value in sorted(donor_db.items(), key=lambda t: sum(t[1]), reverse=True):
        print("{:<27}${:12.2f}{:11}  ${:12.2f}".format(key, sum(value), len(value), sum(value)/len(value)))


def letter_to_all():
    for key, value in donor_db.items():
        with open(f'{key}.txt', 'w') as f:
            f.write(f'Dear {key},\n\n\tThank you for your donation of ${value[-1]}.\n\n\t\tSincerely,\n\t\t-The Mailroom')
    print("Emails have been saved as .txt files in your working directory.")

def quit_program():
    print("Thank you for visiting The Mailroom")
    sys.exit()


SWITCH_FUNC_DICT = {"1": thank_you, "2": report, "3": letter_to_all, "4": quit_program}


def main():
    print("Welcome to The Mailroom")
    while True:
        response = input(PROMPT)
        if response not in SWITCH_FUNC_DICT:
            print("Not a valid option")
            continue
        SWITCH_FUNC_DICT.get(response)()


if __name__ == '__main__':
    main()

