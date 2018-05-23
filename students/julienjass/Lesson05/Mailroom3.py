#!/usr/bin/env python3

import sys

# Data base made of a dictionary containing the donors' information
donors = {
    'William Gates, III': [261514, 392270.49],
    'Mark Zuckerberg': [4918.83, 9837.66, 1639.61],
    'Jeff Bezos': [877.33],
    'Paul Allen': [354.21, 212.53, 141.68]
    }


def mainloop():
    """Main menu"""
    print('Mailroom Application')
    response = ''
    switch_dict = {
        '1': thank_you,
        '2': report,
        '3': write_letters_on_disk,
        '4': leave
    }
    while response != '4':
        print('Please select one of the 3 options:')
        print('''
        1) Send a Thank You
        2) Create a Report
        3) Creating letters for all donors
        4) Quit''')
        print()
        response = input('Your answer: ')
        try:
            switch_dict.get(response)()
        except TypeError:
            print('This is not a valid response. Please type either 1, 2, 3, or 4\n')
        continue


def thank_you():
    """Thank You menu"""
    print()
    print('You have chosen to Send a Thank You message')
    user_choice = ''
    switch_func_dict = {
        '1': get_name_donation,
        '2': donor_list
    }
    while user_choice != '3':
        print('''
        1) Enter the name of the donor
        2) See the list of donors
        3) Return''')
        print()
        user_choice = input('Your choice: ')
        try:
            switch_func_dict.get(user_choice)()
        except TypeError:
            print('This is not a valid response. Please type either 1, 2, or 3\n')
        continue
    return


def names():
    """Refresh the list of the current donors"""
    names = []
    for person in donors:
        names.append(person[0])
    return names


def gen_letter(donor):
    """Generate text of letter"""
    return "Dear {:s},\n\nThank you for your donation of ${:,.2f}.\n\nBest regards,,\nThe Organization".format(donor[0], donor[1])


def write_letters_on_disk():
    """Generate one letter for each donor and write on disk"""
    for name, donation in donors.items():
        print('Creating a letter for {:s}'.format(name))
        donor = (name, donation[-1])
        letter = gen_letter(donor)
        filename = name.replace(' ', '_') + '.txt'
        with open(filename, 'w') as outfile:
            outfile.write(letter)
    print()
    return


def enter_name(name, amount):
    """Add name and/or donation to donors' database"""
    check = 0
    while check == 0:
        try:
            amount = float(amount)
        except ValueError:
            print('Please enter an amount which is valid.\n')
            amount = input('Amount: ')
            continue
        else:
            check = 1
    donors.setdefault(name, []).append(amount)
    print(gen_letter([name, amount]))
    print()


def get_name_donation():
    """Input donor name and donation amount"""
    print('\nEnter the name of the donor:')
    donor_name = input('Name: ')
    print('Enter an amount:')
    donor_amount = input('Amount: ')
    print()
    enter_name(donor_name, donor_amount)


def donor_list():
    """Print list of names of donors"""
    print('\nDonors:')
    for name in donors:
        print(name)
    print()


def avg_donation(donation):
    """Compute average"""
    return sum(donation[1]) / len(donation[1])


def sum_donation(donation):
    """Compute total sum"""
    return sum(donation[1])


def report():
    """Generate the formatted report"""
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('-' * 67)
    sorted_donors = list(donors.items())
    sorted_donors.sort(key=sum_donation, reverse=True)
    report_rows = []
    for element in sorted_donors:
        report_rows.append('{:24s} {:>12s} {:^13d} {:>12s}\n'.format(element[0], ('{:,.2f}'.format(sum(element[1]))), len(element[1]), ('{:,.2f}'.format(avg_donation(element)))))
    print(''.join(report_rows))
    return


def leave():
    """Quit the application"""
    sys.exit()


if __name__ == '__main__':
    """Always executed by the script"""
    mainloop()
