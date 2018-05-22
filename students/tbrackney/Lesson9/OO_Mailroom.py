#!/usr/bin/env python3
"""
File Name: OO_Mailroom.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 5/20/2018
Python Version: 3.6.4
"""
from donation_tracker import Donor, Donorlist
from io import StringIO

init_donors = ['Tom Selleck', 'Burt Reynolds', 'Nick Offerman', 'Sam Elliot', 'John Waters']
init_donations = [[2000.00, 1500.00, 500.00], [45.00], [1000.00, 1000.00], [1200.00, 550.00], [20.00, 20.00, 20.00]]
init_tuple = tuple(zip(init_donors, init_donations))
dl = Donorlist(init_tuple)


def get_donation(d_name):
    """Appends a donation to existing donor """
    # Formats float to 2 decimal places"
    prompt = f"Enter a Donation amount for {d_name}\n"
    error_message = 'Invalid donation amount'
    while True:
        try:
            d_amount = round(float(input(prompt)), 2)
        except ValueError:
            print(error_message)
        else:
            return d_amount


def print_list():
    for donor in dl.list_donors():
        print(donor)


def t_menu():
    """ Prints Thank You menu."""
    # Wasn't sure how to implement this using dispatch func
    # Not liking this, need to refactor.
    while True:
        prompt = ('Type list to see a list of donors. Type quit to exit\n'
                  'Please enter donor name: ')
        entry = input(prompt)
        if entry.lower() == "list":
            print_list()
        elif entry.lower() == "quit":
            break
        elif entry in dl.list_donors():
            donation = get_donation(entry)
            dl.add_donation(entry, donation)
            print(dl.send_thankyou(entry, donation))
        else:
            print(f'{entry} is not in List')
            dl.add_donor(entry)
            donation = get_donation(entry)
            dl.add_donation(entry, donation)
            print(dl.send_thankyou(entry, donation))


def create_report():
    """Prints report of all donors"""
    output = StringIO()
    dl.create_report(output)
    print(output.getvalue())
    output.close()


def mail_all():
    """
    Generates letter from template for all donors.  Saves to file and Prints
    to consoleself.
    """
    for donor_name in dl.list_donors():
        filename = donor_name.replace(' ', '_') + '.txt'
        total = dl.get_total(donor_name)
        letter = dl.send_thankyou(donor_name, total, template='long')
        try:
            outfile = open(filename, 'w')
            outfile.write(letter)
            outfile.close()
        # Catches invalid characters in name
        except FileNotFoundError:
            print(f'Unable to write to file {filename}')
        else:
            print(letter)


def quit():
    print("Exiting Menu")
    return 'exit menu'


def menu(prompt, dispatch):
    while True:
        entry = input(prompt).lower()
        try:
            if dispatch.get(entry)() == "exit menu":
                break
        except TypeError:
            print('Please enter one of the following selections')


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
