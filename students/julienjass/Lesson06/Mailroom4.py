#!/usr/bin/env python3

import sys

# Data object storing donor information
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


def thank_you():
    """Thank You menu"""
    print()
    print('You have chosen to Send a Thank You message')
    user_choice = ''
    switch_func_dict = {
        '1': get_name_donation,
        '2': print_donor_list
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


def gen_letter(name, amount):
    """Generate text of letter"""
    return "Dear {:s},\n\nThank you for your donation of ${:,.2f}.\n\nBest regards,\nThe Organization".format(name, amount)


def filename(name):
    'Generate a file name based on the donor name'
    return name.replace(' ', '_') + '.txt'


def write_letters_on_disk(dict=donors):
    """Generate one letter for each donor and write on disk"""
    for n, d in dict.items():
        print('Creating a letter for {:s}'.format(n))
        letter = gen_letter(n, d[-1])
        with open(filename(n), 'w') as outfile:
            outfile.write(letter)
    print()


def add_donation(name, amount, dict=donors):
    """Add donation to donors' database"""
    return dict.setdefault(name, []).append(amount)


def enter_name(name, amount):
    """Input name and donation"""
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
    add_donation(name, amount)
    print(gen_letter(name, amount))
    print()


def get_name_donation():
    """Input donor name and donation amount"""
    print('\nEnter the full name of the donor:')
    donor_name = input('Name: ')
    print('Enter an amount:')
    donor_amount = input('Amount: ')
    print()
    enter_name(donor_name, donor_amount)


def donor_list(dict=donors):
    """Print list of names of donors"""
    name_list = []
    for name in dict:
        name_list.append(name + '\n')
    return ''.join(name_list)


def print_donor_list():
    """Print list of donors"""
    print('\nDonors:')
    print(donor_list())
       

def avg_donations(donations):
    """Compute average"""
    return sum(donations[1]) / len(donations[1])


def sum_donations(donations):
    """Compute total sum"""
    return sum(donations[1])


def report_data(dict=donors):
    """Generate content of the formatted report"""
    sorted_donors = list(dict.items())
    sorted_donors.sort(key=sum_donations, reverse=True)
    report_rows = []
    for d in sorted_donors:
        report_rows.append('{:24s} {:>12s} {:^13d} {:>12s}\n'.format(d[0], ('{:,.2f}'.format(sum(d[1]))), len(d[1]), ('{:,.2f}'.format(avg_donations(d)))))
    return ''.join(report_rows)


def report():
    """Generate formatted report"""
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('-' * 67)
    print(report_data())


def leave():
    """Quit the application"""
    sys.exit()


if __name__ == '__main__':
    """Always executed by the script"""
    mainloop()
