#!/usr/bin/env python3
"""Mail Room 2 Module

This module contains all of the functions for the updated Mail Room 2 module.
"""

THANK_YOU_OPT = 1
REPORT_OPT = 2
QUIT_OPT = 3

GIFTS_KEY = 'Gifts'
NUM_GIFTS_KEY = 'Number of Gifts'
TOTAL_KEY = 'Total'
AVE_KEY = 'Average'
DONATION_DB = {'Toni Morrison': {GIFTS_KEY: [1000, 5000, 10000],
                                 NUM_GIFTS_KEY: 0,
                                 TOTAL_KEY: 0,
                                 AVE_KEY: 0},
               'Mike McHargue': {GIFTS_KEY: [12000, 50000, 27000],
                                 NUM_GIFTS_KEY: 0,
                                 TOTAL_KEY: 0,
                                 AVE_KEY: 0},
               "Flannery O'Connor": {GIFTS_KEY: [38734, 6273, 67520],
                                     NUM_GIFTS_KEY: 0,
                                     TOTAL_KEY: 0,
                                     AVE_KEY: 0},
               'Angela Davis': {GIFTS_KEY: [74846, 38470, 7570, 50],
                                NUM_GIFTS_KEY: 0,
                                TOTAL_KEY: 0,
                                AVE_KEY: 0},
               'Bell Hooks': {GIFTS_KEY: [634547, 47498, 474729, 4567],
                              NUM_GIFTS_KEY: 0,
                              TOTAL_KEY: 0,
                              AVE_KEY: 0}}


def get_usr_input():
    """Get input from user.

    Prompt user to select one of three choices. If the user selects one of
    these three, that value is returned. If not, the user is prompted again to
    select.

    Returns:
        int: Value corresponding to user choice
    """
    select_prompt = '\nPlease select from the following options:\n'\
                    '\t1. Send a Thank You\n'\
                    '\t2. Create a Report\n'\
                    '\t3. quit\n'\
                    ' --> '
    usr_in = int(input(select_prompt))

    while usr_in not in (THANK_YOU_OPT, REPORT_OPT, QUIT_OPT):
        print('\nPlease enter either a "1", "2", or "3"')
        usr_in = int(input(select_prompt))

    return usr_in


def add_donation(donor, amount):
    """Add a new donation to the donation database.

    Args:
        donor (str): Name of donor in donation database.
        amount (int): Amount to add to donation database.
    """
    DONATION_DB[donor][GIFTS_KEY].append(amount)
    DONATION_DB[donor][NUM_GIFTS_KEY] += 1
    DONATION_DB[donor][TOTAL_KEY] += amount
    DONATION_DB[donor][AVE_KEY] = DONATION_DB[donor][TOTAL_KEY] / \
        DONATION_DB[donor][NUM_GIFTS_KEY]


def send_thank_you():
    """Send a thank you.

    Prompt for a Full Name.
    If the user types ‘list’, show them a list of the donor names and re-prompt
    If the user types a name not in the list, add that name to the data
    structure and use it.
    If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
    Turn the amount into a number – it is OK at this point for the program to
    crash if someone types a bogus amount.
    Once an amount has been given, add that amount to the donation history of
    the selected user.
    Finally, use string formatting to compose an email thanking the donor for
    their generous donation. Print the email to the terminal and return to the
    original prompt.
    """
    name_prompt = '\nPlease enter name of "Thank You" recipient:\n'\
        '(Enter "list" to see all donors)\n'\
        '(Enter "quit" to return to main menu)\n'\
        ' --> '
    amount_prompt = '\nPlease enter the donation amount:\n'\
                    '(Enter "quit" to return to main menu)\n'\
                    ' --> '
    thank_you_fmt = '\nThank you {:s} for your generous donation of ${:.2f}!'
    names = [donor.lower() for donor in DONATION_DB]

    while True:
        new_donor = False
        usr_in = input(name_prompt).strip().lower()

        if usr_in.startswith('q'):
            break
        elif usr_in == 'list':
            print()
            for dnr in DONATION_DB:
                print(dnr)
        else:
            if usr_in in names:
                for dnr in DONATION_DB:
                    if usr_in in dnr.lower():
                        donor = dnr
            else:
                donor = " ".join([name.title() for name in usr_in.split()])
                new_donor = True

            usr_in = input(amount_prompt).strip().lower()
            if usr_in.startswith('q'):
                break
            else:
                donation = float(usr_in)

            if new_donor:
                DONATION_DB[donor] = {GIFTS_KEY: [],
                                      NUM_GIFTS_KEY: 0,
                                      TOTAL_KEY: 0,
                                      AVE_KEY: 0}

            add_donation(donor, donation)
            print(thank_you_fmt.format(donor, donation))
            break


def create_report():
    """Generate and print a report of donors in the database

    Prints a list of donors, sorted by total historical donation amount.
    Includes Donor Name, total donated, number of donations and average
    donation
    """
    min_width = 12
    def_space = 5
    col_sep = ' | '

    max_name = len(max([dnr for dnr in DONATION_DB], key=len)) + def_space
    max_total = len(max([str(val[TOTAL_KEY])
                         for val in DONATION_DB.values()], key=len)) + def_space
    max_gifts = len(max([str(val[NUM_GIFTS_KEY])
                         for val in DONATION_DB.values()], key=len)) + def_space
    max_ave = max_total

    if max_name < min_width:
        max_name = min_width
    if max_total < min_width:
        max_total = max_ave = min_width
    if max_gifts < min_width:
        max_gifts = min_width

    header = (f'\n{{:^{max_name}s}}{col_sep}{{:^{max_total}s}}{col_sep}'
              f'{{:^{max_gifts}s}}{col_sep}{{:^{max_ave}s}}\n')
    header += '-' * (max_name + max_total + max_gifts +
                     max_ave + len(col_sep) * 3)
    header = header.format('Donor Name', 'Total Given',
                           'Num Gifts', 'Average Gift')
    row_fmt = (f'{{:<{max_name}s}}{col_sep}${{:>{max_total - 1}.2f}}{col_sep}'
               f'{{:>{max_gifts}d}}{col_sep}${{:>{max_ave - 1}.2f}}')

    sorted_dnr_keys = sorted(
        DONATION_DB, key=lambda dnr: DONATION_DB[dnr][TOTAL_KEY], reverse=True)

    print(header)
    for dnr in sorted_dnr_keys:
        print(row_fmt.format(dnr, DONATION_DB[dnr][TOTAL_KEY],
                             DONATION_DB[dnr][NUM_GIFTS_KEY],
                             DONATION_DB[dnr][AVE_KEY]))


def quit_mailroom():
    """Exit operations when quitting mail room"""
    print('Quitting mailroom...')


def main():
    """Main function"""

    opt_dict = {THANK_YOU_OPT: send_thank_you,
                REPORT_OPT: create_report,
                QUIT_OPT: quit_mailroom}

    # Initialize database
    for values in DONATION_DB.values():
        values[NUM_GIFTS_KEY] = len(values[GIFTS_KEY])
        values[TOTAL_KEY] = sum(values[GIFTS_KEY])
        values[AVE_KEY] = values[TOTAL_KEY] / values[NUM_GIFTS_KEY]

    choice = ''
    while choice != QUIT_OPT:
        choice = get_usr_input()
        opt_dict.get(choice)()


if __name__ == '__main__':
    main()
