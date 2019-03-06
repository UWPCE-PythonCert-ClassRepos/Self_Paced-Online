#!/usr/bin/env python3
"""
mailroom_fp.py: intro to functional programming concepts
Author: JohnR
Version: 2.0
Last updated: 3/3/19
Notes: introducing map, filter and reduce
"""

from donors_fp import DonorDataBase
from donors_fp import Donor


def menu(prompt):
    """
    Get user input
    :return: call the appropriate method or function
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
        elif response == '6':
            challenge(donor_db)
        elif response == '7':
            challenge_filtered(donor_db)
        else:
            print('Please enter a valid number between 1 - 6.')


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
    """
    Sub-menu for becoming a new donor
    :return: return a number as a string
    """
    print()
    print('Please choose from the following donor options:')
    print('1 = Return to main menu')
    print('2 = See a list of current donors')
    print('3 = Become a new donor or add a donation for an existing donor')
    cmd = input('>>> ')
    return cmd


def thanks(name, amount):
    """
    say thanks for the money
    :param name: donor name
    :param amount: donation amount
    :return:
    """
    print()
    print(f'Dear {name}, thank you for the kind donation of ${amount} - '
          f'it has been added to our records.')
    print()


def donor_info():
    """
    Get donor name
    :return: tuple of first and last name
    """
    first = input('Please enter your first name: ')
    last = input('Please enter your last name: ')
    return first.capitalize().strip(), last.capitalize().strip()


def donor_amount():
    """
    get donation amount
    :return: donation amount as float
    """
    while True:
        try:
            donation = float(input('Please enter an amount to donate: '))
        except ValueError:
            print('Sorry, we need a number here!')
        else:
            return donation


def donor_actions(data):
    """
    Sub-menu of user options
    :param data: Current user data base
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
        elif cmd == '3':
            my_name = donor_info()
            full_name = my_name[0] + ' ' + my_name[1]
            amount = donor_amount()
            if data.get_donor(full_name):
                data.get_donor(full_name).new_donation(amount)
                thanks(full_name, amount)
            else:
                new_donor = Donor(my_name[0], my_name[1], amount)
                data.add_donor(new_donor)
                thanks(new_donor.full_name, amount)
        else:
            print('-' * 40)
            print('Sorry, need a number between 1 and 3')
            print('-' * 40)


def factor():
    """
    Get a float to multiply by
    :return: float
    """
    while True:
        try:
            some_number = float(input('Please enter a number to'
                                      ' multiply by: '))
        except ValueError:
            print('Sorry, we need a number here!')
        else:
            return some_number


def challenge(data):
    """
    Amplify all current donations by X amount
    :param data: Current user data base
    :return: New data user database
    """
    challenge_db = DonorDataBase()
    multiplier = factor()
    for donor in data.donors:
        new_amounts = donor.amped_donations(multiplier)
        new_donor = Donor(donor.first, donor.last, new_amounts)
        challenge_db.add_donor(new_donor)

    print(f'Thank you - multiplying our current donations by {multiplier} '
          f'gives us the following new amounts:\n')
    challenge_db.print_summary()


def challenge_filtered(data):
    """
    Amplify qualifying donations by X amount
    :param data: Current user data base
    :return: New data user database
    """
    filtered_db = DonorDataBase()
    multiplier = factor()
    min_donation = float(input('Please exclude donations under: '))
    max_donation = float(input('Please exclude donations over: '))
    for donor in data.donors:
        filtered_list = donor.filtered_donations(min_donation,
                                                 max_donation)
        if not filtered_list:
            break
        else:
            amped_list = list(map(lambda x: x * multiplier, filtered_list))
            new_donor = Donor(donor.first, donor.last, amped_list)
            filtered_db.add_donor(new_donor)

    filtered_db.print_summary()


def options():
    """
    Provide a list of options for the main menu
    :return option list
    """
    user_prompt = (
        "\nWelcome to the main menu!\n"
        "Please pick a number from the following:\n"
        "1: exit the program\n"
        "2: check donor list and become a donor\n"
        "3: display a summary of current donor activity\n"
        "4: print out a thank you for each donor\n"
        "5: save a thank you note to disk for each donor\n"
        "6: AMPED: Multiply all donations by X amount\n"
        "7: AMPED, filtered: Multiply qualifying donations by X amount\n "
        ">>> "
    )

    return user_prompt


if __name__ == '__main__':
    """
    Create a database with a few donors and execute main user prompt
    """
    donor_db = DonorDataBase()

    d1 = Donor('John', 'Randal', [12.32, 34.53, 532.32])
    d2 = Donor('Sarah', 'Samson', [1.32, 324.53, 2345.33, 6602.12])
    d3 = Donor('Alex', 'Rez', [122.32, 2334.53])
    d4 = Donor('Billy', 'Durst', [5.32, 4.00])

    donors = [d1, d2, d3, d4]

    for i in donors:
        donor_db.add_donor(i)

    menu(options())

