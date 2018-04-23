#!/usr/bin/env python3
"""
File Name: mailroom2.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 4/22/2018
Python Version: 3.6.4
"""


''' Dictionary template '''
donor_template = {'first': '', 'last': '', 'donations': []}

''' Populating initial donors list'''
donors = {}
donors['Tom Selleck'] = {'first': 'Tom', 'last': 'Selleck',  'donations': [2000.00, 1500.00, 500.00]}
donors['Burt Reynolds'] = {'first': 'Burt', 'last': 'Reynolds', 'donations': [45.00]}
donors['Nick Offerman'] = {'first': 'Nick', 'last': 'Offerman', 'donations': [1000.00, 1000.00]}
donors['Sam Elliot'] = {'first': 'Sam', 'l_name': 'Elliot', 'donations': [1200.00, 550.00]}
donors['John Waters'] = {'first': 'John', 'l_name': 'Waters', 'donations': [20.00, 20.00, 20.00]}



# updated
def list_donors():
    ''' Prints list of donors '''
    for d in donors:
        print(d)
    return


# Updated
def add_donor(d_name):
    '''Adds a new donor to donors'''
    donor = donor_template.copy()
    donor['first'], donor['last'] = d_name.split()
    donors[d_name] = donor
    add_donation(d_name)
    return


# Updated
def add_donation(d_name):
    '''Appends a donation to existing donor '''
    # Formats float to 2 decimal places"
    d_amount = round(float(input(f"Enter a Donation amount for {d_name}\n")), 2)
    # Using same index for donors and donations
    donors[d_name]['donations'].append(d_amount)
    print_email(d_name, d_amount)
    return


#come back to
def print_email(d_name, amount):
    template = "Dear {}, thank you for your generous donation of ${:.2f}"
    print(template.format(name, amount))
    print('\n')
    return


def create_report():
    categories = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    print("{:<20}| {:>10} | {:>10} | {:>10}".format(*categories))
    for name, donor in donors.items():
        total = sum(d['donations'])
        num = len(d['donations'])
        avg = total / num
        spacing = "{:<20} $ {:>10.2f} {:>10}     $ {:>10.2f}"
        print(spacing.format(name, total, num, avg))
    print('\n')
    return


def mail_all():
    return


def t_menu():
    ''' Prints Thank You menu.'''
    # Wasn't sure how to implement this using dispatch func
    while True:
        print("Type list to see a list of donors. Type quit to exit")
        prompt = "Please enter donor name: "
        entry = input(prompt)
        if entry == "list":
            list_donors()
        elif entry == "quit":
            break
        elif entry in donors:
            add_donation(entry)
        else:
            print(f'{entry} is not in List')
            add_donor(entry)
    return


main_prompt = ('\nDonation Tracker\n'
               'Please enter a selection\n'
               '1. Send a Thank You\n'
               '2. Create a report\n'
               '3. Mail all donors\n'
               '0. Exit menu\n'
               )

main_dispatch = {'1': t_menu,
                 '2': create_report,
                 '3': mail_all,
                 '0': quit
                 }


def menu(prompt, dispatch):
    while True:
        entry = input(prompt)
        if dispatch[entry]() == "exit menu":
            break


def quit():
    print("Exiting Menu")
    return 'exit menu'


if __name__ == "__main__":
    menu(main_prompt, main_dispatch)
