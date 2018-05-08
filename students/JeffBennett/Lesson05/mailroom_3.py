#!/usr/bin/env python3

import datetime
import sys

# Data

donors = {
    'Lorenzo Currie': [3000, 250, 5000],
    'Marie Kane': [1000, 195, 50.50],
    'John Beresford Tipton': [10000, 3000, 2500],
    'Janna Adams': [35.50, 19.75],
    'LeSean Haskell': [100],
    'Laila Samir': [1000, 250]
}

letter_to_all_donors = '''\nDear {}\n\n
I write to thank you again for all the support you have provided to Northwest
Lifeboats.  During the past year your total gifts of ${:,.2f} have greatly
furthered our activities.
\n\nI have exciting news that one of our prospective donors may be prepared
to match your next donation, which would double your impact on our efforts.
I will be back in touch with you soon with more details.\n\nSincerely yours
\n\nJ A Bennett\nDirector'''

# Input/Output


def print_main_menu():
    """print main menu and prompt for user choice."""
    print('\nMain Menu\n' + '-'*25 +
          '\n(1)\tSend a Thank You\n(2)\tCreate a Report'
          '\n(3)\tSend Letters to All Donors\n(4)\tQuit')


def print_donor_list(donors):
    """print list of donor names."""
    print('\nOur Current List of Donors:\n' + '-' * 25)
    for key in donors:
        print(key)


def input_gift():
    """input donor gift."""
    while True:
        try:
            gift = float(input("\nEnter amount of gift: " +
                               "or '0' to return to the main menu: "))
            return gift
        except ValueError:
            print("Enter dollar amount as a number; no '$' sign or ',' " +
                  "thousands separator: ")


def print_email_to_donor(donor, gift):
    """print email thanking donor for recent donation."""
    email_dict = {
        'greeting': f'\nDear {donor}',
        'body': f'\n\nThank you very much for your gift of ${gift:,.2f}',
        'signature': '\n\nSincerely yours\n\nJ A Bennett\nDirector'
    }
    email = "{greeting}{body}{signature}".format(**email_dict)
    print(email)


def print_sorted_donors(sorted_donors):
    """print list of donors sorted by total donation history."""
    print('{0:32}{1:13}{2:14}{3:13}'.format
          ('Donor Name', '| Total Gifts', '| Num Gifts', '| Average Gift'))
    print('-' * 73)
    for row in sorted_donors:
        print('{0:30s}  ${1:12.2f}{2:12d}  ${3:12.2f}'.format(*row))


# Processing


def send_thank_you():
    """acknowledge gift with an email and update donor and gift list.
    Final confirm of new gifts from both new and existing donors required."""
    while True:
        donor_name = input("\nEnter donor first and last name,\n " +
                           "'list' for a list of current donors: \n" +
                           "  or 'menu' to return to the main menu: ")
        if donor_name.lower() == 'menu':
            break
        elif donor_name.lower() == 'list':
            print_donor_list(donors)
            continue
        else:
            gift = input_gift()
            if gift == 0:
                break
            confirm = input(f"\nCan you confirm: {donor_name} donated " +
                            f"${gift:,.2f}? [y/n]: ")
            if confirm.lower() == 'y':
                print_email_to_donor(donor_name, gift)
                update_donors(donors, donor_name, gift)
            continue


def update_donors(donors, name, donation):
    """update the dictionary of donors and their gift history. """
    if name in donors:
        donors.setdefault(name, [])
        donors[name].append(donation)
    else:
        donors.update({name: [donation]})
    return donors


def create_report():
    """sort donors from largest to smallest aggregate givers, calculate
    average gift and number of gifts per donor, and print report."""
    data_table = [[key, sum(donors[key]), len(donors[key]),
                   sum(donors[key]) / len(donors[key])] for key in donors]
    sorted_donors = sorted(data_table, key=lambda x: x[1], reverse=True)
    print_sorted_donors(sorted_donors)


def email_all_donors():
    """write letters to all donors to working directory."""
    str_date = datetime.date.today().strftime("%Y-%m-%d")
    for key in donors:
        file_name = key.replace(' ', '_') + '_' + str_date + '.txt'
        message = letter_to_all_donors.format(key, sum(donors[key]))
        with open(file_name, 'w') as fout:
            fout.write(message)


def exit_func():
    """print exit notice and exit the script."""
    print("Exiting the program.  Changes made during session are not saved.")
    sys.exit(0)


def execute_menu_choice():
    """present menu and manage user choices with a function dictionary. """
    switch_dict = {
        1: send_thank_you,
        2: create_report,
        3: email_all_donors,
        4: exit_func
    }
    while True:
        print_main_menu()
        try:
            int_choice = int(input('\nPlease enter number of your choice: '))
            switch_dict[int_choice]()
        except KeyError:
            print("You did not enter number 1, 2, 3 or 4.  Please try again.")
        except ValueError:
            print("You did not enter an integer number.  Please try again.")


if __name__ == "__main__":
    execute_menu_choice()
