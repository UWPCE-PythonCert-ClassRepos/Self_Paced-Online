#!/usr/bin/env python3
"""
mailroom_pt2.py:
 Prompt user for various actions ranging from send thank you notes to
 asking for new donations. Write everything to a local file on exit or
 per menu selection.
Author: JohnR
Version: 2.0
Last updated: 12/30/2018
Notes: v2 mailroom ready to submit
"""

from datetime import date


def main():
    """
    Create a list of donor and amounts, then get user input for the
    various actions available.
    :return: none
    """

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
        "3: display a summary of current donor activity\n"
        "4: print out a thank for each donor\n"
        "5: save a thank you note to disk for each donor\n"
        ">>>\n"
    )

    # create the main menu using dict switch
    main_dispatch = {
        '1': exit_menu,
        '2': donor_actions,
        '3': print_summary,
        '4': thank_all,
        '5': save_report,
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


def thank_all(db):
    """
    Print out thanks to all current donors.
    :param db: current donor db
    :return: None
    """
    donors = sorted_list(db)
    for donor in donors:
        letter = form_letter(donor[0][0], donor[1][0])
        print(letter)


def form_letter(name, donation):
    """
    create a form letter
    :param name: donor name
    :param donation: amount of donation as a float
    :return: form letter filled in with donor and amount
    """
    today = date.today()
    letter = (
        f'\nHey {name.capitalize()}, thanks for your donations! '
        f'As of today, {today}, you have donated a total of '
        f'${donation}.\n'
    )

    return letter


def save_report(db):
    """
    Generate a thank you letter for each donor and write to individual
    files on disk.
    :param db: donor database
    :return: None
    """
    # Get a sorted list, print out a thank you for each then write to disk
    today = date.today()
    donors = sorted_list(db)
    for donor in donors:
        # create a file based on donor name and time stamp
        letter = form_letter(donor[0][0], donor[1][0])
        user_file = "{}.{}.txt".format(donor[0][0], today)

        with open(user_file, 'w') as outfile:
            outfile.write(letter)
        outfile.close()


def exit_menu(db):
    """
    write to file and exit the program
    :return: SystemExit
    """
    # save a current thank you for each donor to disk and exit
    save_report(db)
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
    print(form_letter(name, donation_amount))
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
    """
    Sort a give list of donors by total amount given, large to small
    :param data: dictionary of donor data
    :return: sorted list of donors
    """
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


def print_summary(db):
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

