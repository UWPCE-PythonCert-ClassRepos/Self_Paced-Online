#!/usr/bin/env python3
"""
mailroom_fp.py: intro to functional programming concepts
Author: JohnR
Version: 1.4
Last updated: 2/24/19
Notes: introducing map, filter and reduce
 * each donation can be doubled, tripled, etc | challenge(factor)
        give back new donor data base with new data
 * filter donations above or below a specified amount
        Add min_donation and max_donation optional keyword to
         challenge function; filter donations before passing to map
 * Projections: What would it look like to if total contribution if
        they double contributions under $100; what if you triple
        contributions over $50?
 * implement list comprehension where possible
"""

from donors_fp import DonorDataBase
from donors_fp import Donor


def menu(prompt):
    """
    Get user input
    :return: call the appropriate method or function
    """
    while True: # TODO: provide option to save database and restart from
                # TODO: a previously saved database
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
    """
    Exit program after giving user option to save to disk
    :return: None
    """

    print()
    print('Enter Y to save user data to disk before exiting. ')
    save = input('Any other key to exit without saving >>> ')
    save = save.lower()
    if save == 'y':
        donor_db.save_report()

    raise SystemExit


def donor_menu():
    print()
    print('Please choose from the following donor options:')
    print('1 = Return to main menu')
    print('2 = See a list of current donors')
    print('3 = Become a new donor')
    cmd = input('>>> ')
    return cmd


def donor_actions(data):
    """
    Sub-menu of user options
    data: Current user data base
    :return: None
    """

    while True:
        cmd = donor_menu()
        if cmd == '1':
            break
        elif cmd == '2':
            print()
            print('We currently have the following donors on file: ')
            for i in data.donor_names():
                print(i)
        elif cmd == '3': # TODO: check database if name already exists
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