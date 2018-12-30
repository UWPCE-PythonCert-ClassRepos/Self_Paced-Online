#!/usr/bin/env python3
"""
mailroom.py -
    1) prompt user for 3 actions - Send thank you, create report or quit
Author: JohnR
Version: 1.3
Last updated: 12/29/2018
Notes: Menu is currently working, but is part of main()

  v2.0 requirements:
    1) use dict where appropriate
    2) create a dict-based menu
    3) create a single template using .format(**d) method for the letter
    4) write a full set of letters to everyone on disk in individual files
    5) add a function that goes through all donors, generates a thank you
        letter, and writes it to disk as a text file.
        A) use donor name and date for file name
"""


def main():
    """
    Create a list of donor and amounts, then get user input for the
    various actions available.
    :return: none
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
    main_prompt = (
        "\nWelcome to the main menu!\n"
        "Please pick a number from the following:\n"
        "1: exit the program\n"
        "2: check donor list and become a donor\n"
        "3: create an interactive report of current donors\n"
        "4: write a thank you note for each donor and write to file\n"
        ">>>\n"
    )

    main_dispatch = {
        '1': exit_menu,
        '2': thank_you,
        '3': create_report,
        '4': write_report,
    }

    # Call the main menu - currently uses a static variable, db
    while True:
        selection = input(main_prompt)

        if selection in main_dispatch:
            main_dispatch.get(selection)(db)
        else:
            print('Please enter a number between 1 and 4')


def write_report():
    pass


def exit_menu():
    print('Exiting program -')
    raise SystemExit


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

    # Create a list from the donor dictionary so we can sort by size
    d_list = []
    for donor in data:
        total_amount = round(float(sum(data[donor].values())), 2)
        num_donations = round(len(data[donor].values()), 2)
        avg_donation = total_amount / num_donations
        avg_donation = round(avg_donation, 2)

        d_list.append([[donor], [total_amount, num_donations, avg_donation]])

    # Sort the list from largest to smallest donation
    d_list.sort(key=lambda x: x[1])
    d_list.reverse()

    # Print the sorted list in a nice format
    print()
    print('Donor Name       | Total Given | Num Gifts | Avg Gift Amount')
    print('-' * 60)

    for d in d_list:
        print(f'{d[0][0]:<17} ${d[1][0]:^15} {d[1][1]:<10} ${d[1][2]}')


if __name__ == '__main__':
    main()