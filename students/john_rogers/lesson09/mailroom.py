#!/usr/bin/env python3
"""
test file for mailroom classes
"""

from donors import DonorDataBase as DDB
from donors import Donor as D


def main():
    """
    Main script loop and user interaction
    :return:
    """

    donor_db = DDB()
    d1 = D('John', 'Rogers', [12.32, 34.53])
    d2 = D('Sarah', 'Rogers', [1.32, 324.53])
    d3 = D('Alex', 'Rogers', [122.32, 2334.53])
    d4 = D('Dino', 'Rogers', [15.32, 34.00])

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

    main_dispatch = {
        '1': exit_menu,
        '2': donor_actions,
        '3': DDB.print_summary,
        '4': DDB.thank_all,
        '5': DDB.save_report,
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


def exit_menu(data):
    print()
    save = input('Enter Y to save all data to disk before exiting. ')
    save = save.lower()
    if save == 'y':
        DDB.save_report(data)

    raise SystemExit


def donor_actions(data):
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
            print('We currently have the following donors on file: ')
            for i in data.donor_names():
                print(i)


if __name__ == '__main__':
    main()
