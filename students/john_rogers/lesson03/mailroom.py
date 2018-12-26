#!/usr/bin/env python3
"""
mailroom.py -
    1) prompt user for 3 actions - Send thank you, create report or quit
Author: JohnR
Version: .5
Date: 12/26/2018
Notes: Thank_you function mostly complete, need to validate numbers
        as float (presumably).
"""


def main():
    """
    Create a list of donor and amounts, then get user input for the
    various actions available.
    :return:
    """

    db = {'sting': {'d1': 13.45,
                    'd2': 214.34,
                    'd3': 453.23,
                    },
          'bono': {'d1': 54.54,
                   'd2': 778.01,
                   'd3': 564.35,
                   },
          'oprah': {'d1': 66.34,
                    'd2': 664.33,
                    'd3': 566.45,
                    }
         }

    while True:
        choice = get_input()

        if choice == 1:
            print('Exiting program.')
            exit()
        elif choice == 2:
            thank_you(db)
        elif choice == 3:
            print('we would print a report here')


def get_input():
    """
    Get user input
    :return: User choice from menu
    """
    print('Please choose from the following menu: ')
    print('1 Quit')
    print('2 Send a thank you')
    print('3 Create a report')

    # TODO: Time permitting, check if string
    while True:
        cmd = input('Please pick a number between 1 and 3: ')
        cmd = int(cmd)
        if cmd not in range(1, 4):
            break
        else:
            return cmd


def thank_you(names):
    """
    send a thank you, check the donor list or add donation
    :return: thank you
    """

    while True:
        print('Enter q to exit to main menu.')
        cmd = input("Enter 'list' to see a current list of donors or "
                    "a new name to become a new donor: ")
        cmd = cmd.lower()
        if cmd == 'q':
            break
        elif cmd == 'list':
            print()     # TODO: clean up how names are printed to screen
            print(names.keys())
        elif cmd in names.keys():
            # TODO: Need to validate numbers/ convert to float?
            donation = input('Please enter an amount to donate: ')

            # add donation as a new key value pair
            d_num = len(names[cmd].keys()) + 1
            d_num = str(d_num)
            new_key = 'd' + d_num
            names[cmd][new_key] = donation

            print(f'Thank you, {cmd.capitalize()}, for your kind'
                  f' donation of ${donation}.')
        else:
            # add the new name and prompt for donation
            print(f'Welcome aboard, {cmd.capitalize()}, how much would '
                  f'you like to donate?')
            new_donation = input('Please an amount to donate: ')
            names[cmd] = {'d1': new_donation}

            print(f'Thank you, {cmd.capitalize()}, for your kind'
                  f' donation of ${new_donation}.')


def create_report():
    """
    create a report
    :return: report
    """
    # TODO: Print a list of donors sorted by historical donation amount
    # TODO:     List donor name, number of donation and average donation
    # TODO:     amount (summary of each only)
    # TODO: Return to original prompt
    # TODO: User should be able to quit current task and return to prompt
    pass


if __name__ == '__main__':
    main()
