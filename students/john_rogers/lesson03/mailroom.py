#!/usr/bin/env python3
"""
mailroom.py -
    1) prompt user for 3 actions - Send thank you, create report or quit
Author: JohnR
Version: 1.0
Last updated: 12/27/2018
Notes: Code complete from a requirements standpoint.
"""


def main():
    """
    Create a list of donor and amounts, then get user input for the
    various actions available.
    :return: none
    """

    # Nested dictionaries seems like the most intuitive data structure
    # for this type of record keeping
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
                    },
          'yoko': {'d1': 64.24,
                   'd2': 67.03,
                   'd3': 990.34,
                   },
          'santa': {'d1': 45.43,
                    'd2': 98345.32,
                    'd3': 54.34,
                    'd4': 456.23,
                    },
         }

    while True:
        choice = get_input()

        if choice == 1:
            print('Exiting program.')
            exit()
        elif choice == 2:
            thank_you(db)
        elif choice == 3:
            create_report(db)


def get_input():
    """
    Get user input
    :return: User choice from menu
    """
    print()
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
    :return: None
    """

    while True:
        print('Enter q to exit to main menu.')
        cmd = input("Enter 'list' to see a current list of donors or "
                    "a new name to become a new donor: ")
        cmd = cmd.lower()

        # TODO: v-next decompose this into smaller, more discrete functions
        # TODO: validate donations are digits instead of strings
        if cmd.isdigit():
            break
        elif cmd == 'q':
            break
        elif cmd == 'list':
            print()
            for i in names.keys():
                print(i.capitalize())
        elif cmd in names.keys():
            # name already in list, solicit new donation and add to dict
            donation = input('Please enter an amount to donate: ')
            donation = float(donation)

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
            new_donation = float(new_donation)
            names[cmd] = {'d1': new_donation}

            print(f'Thank you, {cmd.capitalize()}, for your kind'
                  f' donation of ${new_donation}.')


def create_report(data):
    """
    Print a list of donors sorted by historical donation amount.
    List donor name, number of donations and average donation amount.
    :return: none
    """
    print()
    print('Donor Name       | Total Given | Num Gifts | Avg Gift Amount')
    print('-' * 60)

    # Not the prettiest formatting, but works well enough for v1
    for donor in data:
        total_amount = round(float(sum(data[donor].values())), 2)
        num_donations = round(len(data[donor].values()), 2)
        avg_donation = total_amount / num_donations
        avg_donation = round(avg_donation, 2)
        dollar = '$'

        print(f'{donor.capitalize():20} {dollar:1} {total_amount:3n}'
              f' {num_donations:12n} {avg_donation:12n}')


if __name__ == '__main__':
    main()
