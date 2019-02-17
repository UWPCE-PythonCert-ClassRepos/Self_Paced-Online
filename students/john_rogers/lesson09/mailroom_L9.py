#!/usr/bin/env python3
"""
mailroom_L9.py: refactor to use a donor class
Author: JohnR
Version: .1 (Lesson 09)
Last updated: 2/16/2019
Notes:
    Guidelines:
    * User interaction cleanly separated from data handling
    * No input function in a class that holds the data
    * Encapsulation
    * DRY - Don't Repeat Yourself
"""

from donors import Donor as D
from donors import DonorDB as DDB


def main():
    """
    Create a list of donor and amounts, then get user input for the
    various actions available.
    :return: none
    """

    d1 = D('Sting', 'Jones', 13.45)
    d2 = D('Bono', 'Smith', 1.45)
    d3 = D('Oprah', 'Ricks', 1.00)
    d4 = D('Yoko', 'Ono', 3.02)
    d5 = D('Santa', 'Claus', 233.02)
    DDB.new_donor(d1.)
    DDB.new_donor(d2)
    DDB.new_donor(d3)
    DDB.new_donor(d4)
    DDB.new_donor(d5)

    db = DDB.donors

    main_prompt = (
        "\nWelcome to the main menu!\n"
        "Please pick a number from the following:\n"
        "1: exit the program\n"
        "2: check donor list and become a donor\n"
        "3: display a summary of current donor activity\n"
        "4: print out a thank you for each donor\n"
        "5: save a thank you note to disk for each donor\n"
        ">>> "
    )

    main_dispatch = {
        '1': DDB.exit_menu,
        '2': donor_actions,
        '3': DDB.print_summary,
        '4': DDB.thank_all,
        '5': DDB.save_report,
    }

    menu(main_prompt, main_dispatch, db)


def menu(main_prompt, main_dispatch, db):
    """
    Get user input
    :return: call the appropriate menu item
    """
    while True:
        response = input(main_prompt)
        try:
            main_dispatch[response](db)
        except KeyError:
            print('Please enter a number between 1 and 5.')


def seek_donation(name):
    """
    Prompt user for a donation, use try/except to validate user input.
    :param name: name of donor
    :return: donation amount as a float
    """

    while True:
        donation_amount = input(f'Hi {name.capitalize()}, how much would you '
                                f'like to give today? ')

        try:
            donation_amount = round(float(donation_amount), 2)
            print(form_letter(name, donation_amount))
            return donation_amount
        except ValueError:
            print('Please enter an amount in digits only.')


def donor_actions(names):
    """
    send a thank you, check the donor list or add donation
    :return: None
    """

    while True:
        print('\nEnter q to exit to main menu.')
        cmd = input("Enter 'list' to see a current list of donors or "
                    "a new name to become a new donor today!"
                    "\n>>> ")
        cmd = cmd.lower()

        if cmd.isdigit():
            break
        elif cmd == 'q':
            break
        elif cmd == 'list':
            print()
            for i in names.keys():
                print(i.capitalize())
        elif cmd in names.keys():
            donation = seek_donation(cmd)
            names[cmd].append(donation)
        else:
            names[cmd] = []
            donation = seek_donation(cmd)
            names[cmd].append(donation)


if __name__ == '__main__':
    main()
