#!/usr/bin/env python3
"""
test file for mailroom classes
"""

from donors import Donor as D
from donors import DonorDataBase as DDB


def main():
    """
    Main script loop and user interaction
    :return:
    """

    donor_db = DDB()

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
        '1': exit_menu,
        '2': donor_actions,
        '3': print_summary,
        '4': thank_all,
        '5': save_report,
    }

    menu(main_prompt, main_dispatch, donor_db)


def menu(main_prompt, main_dispatch, donor_db):
    """
    Get user input
    :return: call the appropriate menu item
    """
    while True:
        response = input(main_prompt)
        try:
            main_dispatch[response](donor_db)
        except KeyError:
            print('Please enter a number between 1 and 5.')


if __name__ == '__main__':
    main()