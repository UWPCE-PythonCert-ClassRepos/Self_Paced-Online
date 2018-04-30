#!/usr/bin/env python

"""This module runs the mailroom script using oop paradigm."""
import sys
from datetime import date
from functools import reduce


class Donor:
    def __init__(self, firstname, lastname, donations=None):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = '{} {}'.format(firstname, lastname)
        if donations:
            if type(donations) is list:
                self.donations = donations
            else:
                self.donations = [donations]
        else:
            self.donations = []

    def __lt__(self, other):
        return ((self.totaldonation, self.firstname) <
                (other.totaldonation, other.firstname))

    def add_donation(self, amount):
        self.donations.append(amount)

    @property
    def totaldonation(self):
        return sum(self.donations)

    @property
    def numdonation(self):
        return len(self.donations)

    @property
    def avgdonation(self):
        return self.totaldonation / max(self.numdonation, 1)

    @classmethod
    def from_fullname(cls, fullname, donations):
        firstname, lastname = fullname.split(' ')
        return cls(firstname, lastname, donations)

    def factordonation(self, factor, min_donation, max_donation):
        return list(map(
            lambda x: x * factor,
            self.filter_donations(self.donations, min_donation, max_donation)))

    @staticmethod
    def filter_donations(donations, min_donation, max_donation):
        if max_donation is None:
            return list(filter(lambda x: x >= min_donation, donations))
        else:
            return list(filter(lambda x: min_donation <= x <= max_donation,
                               donations))


class DataBase:

    def __init__(self, donors=None):
        if donors:
            self.donors = donors
        else:
            self.donors = []

    def add_donor_and_amount(self, fullname, amount):
        for donor in self.donors:
            if fullname == donor.fullname:
                donor.add_donation(amount)
                break
        else:
            self.donors.append(Donor.from_fullname(fullname, amount))

    def print_donor_and_amount(self, fullname, amount):
        self.add_donor_and_amount(fullname, amount)
        print(self._format_letter(fullname, amount))

    def list_donors(self):
        """Return all donors name."""
        for donor in self.donors:
            print(donor.fullname)

    def create_report(self):
        """Return a summary report of donations."""
        header = '\nDonor Name                | Total Given |' \
                 ' Num Gifts | Average Gift'
        print(header)
        print('-' * (len(header) - 1))
        sortedlist = sorted(self.donors, reverse=True)
        for donor in sortedlist:
            print('{:<26} ${:>11,.2f} {:>11d}  ${:>12,.2f}'.format(
                donor.fullname, donor.totaldonation,
                donor.numdonation, donor.avgdonation))

    def send_letters(self):
        """Create thank you letter for each donor and save as text files"""
        for donor in self.donors:
            fullname = donor.fullname
            amount = donor.donations[-1]
            filename = f'{fullname}_{date.today()}.txt'
            with open(filename, 'w') as outfile:
                # use last donated amount
                outfile.write(self._format_letter(fullname, amount))

    @staticmethod
    def _format_letter(fullname, amount):
        """Return formatted letter with donor name and donated amount"""
        return ('Dear {},\n\n'
                '    Thank you for your very kind donation of ${:,.2f}.\n\n'
                '    It will be put to very good use.\n\n'
                '                   Sincerely,\n'
                '                   -The Team'.format(fullname, amount))

    def challenge(self, factor, min_donation=0, max_donation=None):
        db2 = DataBase()
        for donor in self.donors:
            db2.add_donor_and_amount(
                donor.fullname,
                donor.factordonation(factor, min_donation, max_donation))
        db2.create_report()
        return db2

    def projection(self, projection_inputs):
        factor, min_donation, max_donation = projection_inputs
        db2 = self.challenge(factor, min_donation, max_donation)
        total = reduce(lambda x, y: x + y,
                       map(lambda x: x.totaldonation, db2.donors))
        print(f'\nProjection: total contribution would be ${total:.2f}!')

# initialize the database
db = DataBase([Donor('Jeff', 'Bezos', [3.65, 54.50]),
               Donor('Mark', 'Zuckerberg', [36.54, 1.25, 54.87]),
               Donor('Paul', 'Allen', [17.38]),
               Donor('William', 'Gates', [25.55, 33.33, 78.14])
               ])


def menu_selection(prompt, selection_dict):
    """Return options for user to select from."""
    while True:
        try:
            userinput = input(prompt)
            if userinput == 'q':
                break
            else:
                selection_dict[userinput]()
        except KeyError:
            print('\n{} is not a valid selection. '
                  'Please try again!'.format(userinput))


def fullname_input():
    """Return prompt asking for full name."""
    return input('Enter a donor first and last name > ').title()


def amount_input():
    """Return prompt asking for donation amount."""
    while True:
        try:
            return float(input('Enter donation amount! > '))
        except ValueError:
            print('\nPlease enter dollar amount and NOT text!')


def factor_input():
    """Return prompt asking for challenge factor."""
    while True:
        try:
            return float(input('Enter challenge factor! > '))
        except ValueError:
            print('\nPlease enter challenge factor and NOT text!')


def projection_input():
    """Return prompt asking for challenge factor, min, and max donation to run
    projections."""
    while True:
        string = input(
            '\nEnter challenge factor, min, and max donation! \n'
            'Challenge factor, min, and max donations are optional \n'
            'Ex1: ",," will return a factor of 1 for all contributions \n'
            'Ex2: "2,,100" will double all contributions under $100 \n'
            'Ex3: "3,50," will triple all contributions above $50 > ')
        inputs = string.split(',')
        try:
            if inputs[0] == '':
                inputs[0] = 1
            if inputs[1] == '':
                inputs[1] = 0
            if inputs[2] == '':
                inputs[2] = None
            return [input if input is None
                    else float(input)
                    for input in inputs]
        except IndexError:
            print('Provide at least 2 commas!')
        except ValueError:
            print('Enter number between commas and not texts!')


def send_thankyou_email():
    """Return a menu selection to send thank you email to donor."""
    menu_selection(thankyou_prompt, thankyou_dict)


main_prompt = ('\nEnter "q" to "Exit Menu" \n'
               'Enter "1" to "Send a Thank You" \n'
               'Enter "2" to "Create a Report" \n'
               'Enter "3" to "Send Letters to Everyone" \n'
               'Enter "4" to "Challenge Donations" \n'
               'Enter "5" to "Create Projections" \n'
               'What do you want to do? > '
               )

main_dict = {'1': send_thankyou_email,
             '2': db.create_report,
             '3': db.send_letters,
             '4': lambda: db.challenge(factor_input()),
             '5': lambda: db.projection(projection_input())
             }

thankyou_prompt = ('\nEnter "q" to "Exit Menu" \n'
                   'Enter "1" to "List Donors" \n'
                   'Enter "2" to "Enter a Donor Name" \n'
                   'What do you want to do? > '
                   )

thankyou_dict = {'1': db.list_donors,
                 '2': lambda: db.print_donor_and_amount(fullname_input(),
                                                        amount_input())
                 }


if __name__ == "__main__":
    menu_selection(main_prompt, main_dict)
