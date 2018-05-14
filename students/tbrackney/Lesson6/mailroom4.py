#!/usr/bin/env python3
"""
File Name: mailroom4.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 5/8/2018
Python Version: 3.6.4
"""
from operator import itemgetter


def list_donors():
    ''' Prints list of donors '''
    for d in donors:
        print(d)


# Updated
def add_donor(d_name):
    '''Adds a new donor to donors'''
    donors[d_name] = []


def get_donation(d_name):
    '''Appends a donation to existing donor '''
    # Formats float to 2 decimal places"
    prompt = f"Enter a Donation amount for {d_name}\n"
    error_message = 'Please enter a numerical value'
    while True:
        try:
            d_amount = round(float(input(prompt)), 2)
        except ValueError:
            print(error_message)
        else:
            return d_amount


# Updated
def add_donation(d_name, d_amount):
    '''Appends a donation to existing donor '''
    donors[d_name].append(d_amount)


# updated
def print_email(d_name, amount):
    '''Prints thank you after new donation'''
    template = "Dear {}, thank you for your generous donation of ${:.2f}\n"
    return template.format(d_name, amount)


def sort_donors():
    '''converts donors dict to ordered list of tuples'''
    d_sum = {}
    for donor in donors.keys():
        d_sum[donor] = sum(donors[donor])
    return sorted(d_sum.items(), key=itemgetter(1), reverse=True)


# Updated
def create_report():
    '''Prints report of all donors'''
    categories = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    print("{:<20}| {:>10} | {:>10} | {:>10}".format(*categories))
    d_list = sort_donors()
    for d_tuple in d_list:
        name = d_tuple[0]
        total = d_tuple[1]
        count = len(donors[name])
        try:
            avg = total / count
        except ZeroDivisionError:
            avg = float(0)
        spacing = "{:<20} $ {:>10.2f} {:>10}     $ {:>10.2f}"
        print(spacing.format(name, total, count, avg))
    print('\n')


def mail_all():
    '''Mails all donors'''
    template = ('Dear {},\n'
                '\n'
                '        Thank you for your kind donations totaling {:.2f}\n'
                '\n'
                '        Your gifts will be put to very good use.\n\n'
                '                            Sincerely\n'
                '                                -The Team\n'
                )

    for donor, donations in donors.items():
        filename = donor.replace(' ', '_') + '.txt'
        try:
            outfile = open(filename, 'w')
            outfile.write(template.format(donor, sum(donations)))
        # Catches invalid characters in name
        except FileNotFoundError:
            print(f'Unable to save letter for {donor}.  Please add new donor')
        else:
            print(template.format(donor, sum(donations)))
        outfile.close()


def t_menu():
    ''' Prints Thank You menu.'''
    # Wasn't sure how to implement this using dispatch func
    while True:
        prompt = ('Type list to see a list of donors. Type quit to exit\n'
                  'Please enter donor name: ')
        entry = input(prompt)
        if entry.lower() == "list":
            list_donors()
        elif entry.lower() == "quit":
            break
        elif entry in donors:
            donation = get_donation(entry)
            add_donation(entry, donation)
            print(print_email(entry, donation))
        else:
            print(f'{entry} is not in List')
            add_donor(entry)
            donation = get_donation(entry)
            print(print_email(entry, donation))


def quit():
    print("Exiting Menu")
    return 'exit menu'


def main_default():
    print('Please enter one of the following selections')


def menu(prompt, dispatch):
    while True:
        entry = input(prompt).lower()
        try:
            if dispatch.get(entry)() == "exit menu":
                break
        except TypeError:
            print('Please enter one of the following selections')


# Populating initial donors list
# key is donor name, values are list of donations
# Rewrote using a dict comprehension
donor_list = ['Tom Selleck', 'Burt Reynolds', 'Nick Offerman', 'Sam Elliot', 'John Waters']
donations_list = [[2000.00, 1500.00, 500.00], [45.00], [1000.00, 1000.00], [1200.00, 550.00], [20.00, 20.00, 20.00]]
donors = dict(zip(donor_list, donations_list))

main_keys = ['1', '2', '3', '0']
main_vals = [t_menu, create_report, mail_all, quit]
main_dispatch = dict(zip(main_keys, main_vals))
main_prompt = ('\nDonation Tracker\n'
               'Please enter a selection\n'
               '1. Send a Thank You\n'
               '2. Create a report\n'
               '3. Mail all donors\n'
               '0. Exit menu\n'
               )

if __name__ == "__main__":
    menu(main_prompt, main_dispatch)
