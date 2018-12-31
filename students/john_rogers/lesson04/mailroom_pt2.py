#!/usr/bin/env python3
"""
mailroom.py -
    1) prompt user for 3 actions - Send thank you, create report or quit
Author: JohnR
Version: 1.3
Last updated: 12/30/2018
Notes: Completed feedback from Natasha, need to create write_report function
        next. Check and see if shutil is allowed in solution.

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

    # removed globals

    # converted away from nested dict per N.
    db = {'sting': [13.45, 214.34, 123.45, 1433.23, 1243.13],
          'bono': [7843.34, 35.55, 732.34],
          'oprah': [66.34, 32.23, 632.21, 66.67],
          'yoko': [34.34, 4.34],
          'santa': [5334.00, 254.34, 64324.23, 2345.23, 5342.24],
         }

    # create the main user prompt
    main_prompt = (
        "\nWelcome to the main menu!\n"
        "Please pick a number from the following:\n"
        "1: exit the program\n"
        "2: check donor list and become a donor\n"
        "3: create an interactive report of current donors\n"
        "4: write a thank you note for each donor and write to file\n"
        ">>>\n"
    )

    # create the main menu using dict switch
    main_dispatch = {
        '1': exit_menu,
        '2': donor_actions,
        '3': create_report,
        '4': write_report,
    }

    menu(main_prompt, main_dispatch, db)


def menu(main_prompt, main_dispatch, db):
    """
    Get user input
    :return: call the appropriate menu item
    """
    while True:
        response = input(main_prompt)
        main_dispatch[response](db)


def say_thanks(name, donation):
    """
    Print out a thank you note
    :param name: donor name
    :param donation: amount of donation as a float
    :return: None
    """
    print(f'Hey {name.capitalize()}, thanks for giving us ${donation}! '
          f'We promise to spend it all on booze!')


def write_report(db):
    for donor, amount in db:
        say_thanks(donor, amount)


def exit_menu(db):
    """
    write to file and exit the program
    :return: SystemExit
    """
    # write db to file on exit
    write_report(db)
    print('Exiting program -')
    raise SystemExit
    # NOTE: sys.exit() does not work/ resolve and SystemExit doesn't seem
    # to work on it's own here. So far I can only get 'raise SystemExit
    # to produce the intended effect. Not sure what I'm doing wrong.


def seek_donation(name):
    """
    Prompt user for a donation.
    :param name: name of donor
    :return: donation amount as a float
    """
    donation_amount = input(f'Hi {name.capitalize()}, how much would you '
                            f'like to give today? ')
    donation_amount = round(float(donation_amount), 2)
    say_thanks(name, donation_amount)
    return donation_amount


def donor_actions(names):
    """
    send a thank you, check the donor list or add donation
    :return: None
    """

    while True:
        print('Enter q to exit to main menu.')
        cmd = input("Enter 'list' to see a current list of donors or "
                    "a new name to become a new donor: ")
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
            # name already in list, solicit new donation and add to dict
            donation = seek_donation(cmd)
            names[cmd].append(donation)
        else:
            # add new donor to list and seek contribution
            names[cmd] = []
            donation = seek_donation(cmd)
            names[cmd].append(donation)


def sorted_list(data):
    # create a list of the summaries
    sorted_donors = []
    for name, donations in data.items():
        total = round(sum(donations), 2)
        number = round(len(donations), 2)
        avg = total / len(donations)
        avg = round(avg, 2)
        sorted_donors.append([[name], [total], [number], [avg]])

    # Sort the list by largest total donation
    sorted_donors.sort(key=lambda x: x[1])
    sorted_donors.reverse()
    return sorted_donors


def create_report(db):
    """
    Print a list of donors sorted by historical donation amount.
    List donor name, number of donations and average donation amount.
    :return: none
    """
    donors = sorted_list(db)
    print()
    print('Donor Name       | Total Given | Num Gifts | Avg Gift Amount')
    print('-' * 60)

    for donor in donors:
        print(f'{donor[0][0]:<17} ${donor[1][0]:^15} {donor[2][0]:^13}'
              f'${donor[3][0]:^8}')


if __name__ == '__main__':
    main()

