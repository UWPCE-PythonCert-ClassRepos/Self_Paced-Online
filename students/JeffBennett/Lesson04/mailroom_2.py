#!/usr/bin/env python3

import datetime

# Data

donors = {
    'Lorenzo Currie': [3000, 250, 5000],
    'Marie Kane': [1000, 195, 50.50],
    'John Beresford Tipton': [10000, 3000, 2500],
    'Janna Adams': [35.50, 19.75],
    'LeSean Haskell': [100],
    'Laila Samir': [1000, 250]
}

# Needs format arguments
letter_to_all_donors = '''\nDear {}\n\nI write to thank you again for all the
support you have provided to Northwest Lifeboats.
\n\nDuring the past year your total gifts of ${:,.2f} have greatly
furthered our activities.
\n\nI have exciting news that one of our prospective donors may be prepared
to match your next donation, which would double your impact on our efforts.
I will be back in touch with you soon with more details.\n\nSincerely yours
\n\nJ A Bennett\nDirector'''

# Input/Output


def print_menu():
    """print menu and prompt for user choice."""
    print('\nMain Menu\n' + '-'*25 +
          '\n(1)\tSend a Thank You\n(2)\tCreate a Report'
          '\n(3)\tSend Letters to All Donors\n(4)\tQuit')


def menu_choice():
    int_choice = int(input('\nPlease enter the number of your choice: '))
    return int_choice


def print_donor_list(donors):
    """print list of donor names."""
    print('\nOur Current List of Donors:\n' + '-' * 25)
    for key in donors:
        print(key)


def print_email_to_donor(donor, gift):
    """print email thanking donor for recent donation."""
    print(f"\nDear {donor}\n\nThank you very much for your gift of ${gift}."
          "\nYour donation supports fishermen all along the Northwest coast."
          "\n\nSincerely yours\n\nJ A Bennett\nDirector")


def print_sorted_donors(sorted_donors):
    """print list of donors sorted by total donation history."""
    print('{0:32}{1:13}{2:14}{3:13}'.format
          ('Donor Name', '| Total Gifts', '| Num Gifts', '| Average Gift'))
    print('-' * 73)
    for row in sorted_donors:
        print('{0:30s}  ${1:12.2f}{2:12d}  ${3:12.2f}'.format(*row))


# Processing


def update_donors(donors, name, donation):
    """update the dictionary of donors and their gift history. """
    if name in donors:
        donors[name].append(donation)
    else:
        donors[name] = donation
    return donors


def create_report(donors):
    """sort donors from largest to smallest aggregate givers, calculate
    average gift and number of gifts per donor, and print report. """
    data_table = [[key, sum(donors[key]), len(donors[key]),
                   sum(donors[key]) / len(donors[key])] for key in donors]
    sorted_donors = sorted(data_table, key=lambda x: x[1], reverse=True)
    print_sorted_donors(sorted_donors)


def email_all_donors(donors):
    """write letters to all donors to current file."""
    strDate = datetime.date.today().strftime("%Y-%m-%d")
    for key in donors:
        file_name = key.replace(' ', '_') + '_' + strDate + '.txt'
        message = letter_to_all_donors.format(key, sum(donors[key]))
        print(file_name, message)
        with open(file_name, 'w') as fout:
            fout.write(message)


switch_dict = {
    1: 'placeholder',
    2: create_report,
    3: email_all_donors,
    4: 'placeholder'
}

# Main


if __name__ == "__main__":
    while True:
        print_menu()
        menu_choice()
