#!/usr/bin/env python3
"""
mailroom.py: use classes where applicable
Author: JohnR
Version: 1.2
Last updated: 2/19/19
Notes: Replaced dict switch with if/elif to get it to work
"""

from donors import DonorDataBase
from donors import Donor


def menu(prompt):
    """
    Get user input
    :return: call the appropriate menu item
    """
    while True:
        response = input(prompt)
        if response == '1':
            exit_menu()
        elif response == '2':
            donor_actions(donor_db)
        elif response == '3':
            donor_db.print_summary()
        elif response == '4':
            donor_db.thank_all()
        elif response == '5':
            donor_db.save_report()
        else:
            print('Please enter a valid number between 1 - 5.')


def exit_menu():

    print()
    save = input('Enter Y to save all data to disk before exiting. ')
    save = save.lower()
    if save == 'y':
        donor_db.save_report()

    raise SystemExit


def donor_actions(data):

    while True:
        print()
        print('Please choose from the following donor options:')
        print('1 = Return to main menu')
        print('2 = See a list of current donors')
        print('3 = Become a new donor')
        cmd = input('>>> ')

        if cmd == '1':
            break
        elif cmd == '2':
            print()
            print('We currently have the following donors on file: ')
            for i in data.donor_names():
                print(i)
        elif cmd == '3':
            first = input('Please enter your first name: ')
            last = input('Please enter your last name: ')
            amount = float(input('Amount to donate today: '))

            new_donor = Donor(first.capitalize(), last.capitalize(), amount)
            data.add_donor(new_donor)
            print()
            print(f'{new_donor.full_name} has been added as a donor.')
        else:
            print('-' * 40)
            print('Sorry, need a number between 1 and 3')
            print('-' * 40)


if __name__ == '__main__':
    """
    Create a database with a few donors and execute main user prompt
    """
    donor_db = DonorDataBase()

    d1 = Donor('John', 'Randal', [12.32, 34.53, 532.32])
    d2 = Donor('Sarah', 'Samson', [1.32, 324.53, 2345.33, 6602.12])
    d3 = Donor('Alex', 'Rez', [122.32, 2334.53])
    d4 = Donor('Billy', 'Durst', [15.32, 34.00])

    donor_db.add_donor(d1)
    donor_db.add_donor(d2)
    donor_db.add_donor(d3)
    donor_db.add_donor(d4)

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

    menu(main_prompt)
