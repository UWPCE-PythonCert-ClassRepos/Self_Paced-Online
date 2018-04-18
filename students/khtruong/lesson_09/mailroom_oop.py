#!/usr/bin/env python

"""This module runs the mailroom script using oop paradigm."""

from datetime import date


class Donor:
    def __init__(self, firstname, lastname, donations=None):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = '{} {}'.format(firstname, lastname)
        if donations:
            self.donations = donations
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


class DataBase:

    def __init__(self, donors=None):
        if donors:
            self.donors = donors
        else:
            self.donors = []

    def donor_and_amount(self):
        """Return prompt for donor name and donation amount and print to
        screen.
        """
        fullname = fullname_input()
        amount = amount_input()
        for donor in self.donors:
            if fullname == donor.fullname:
                donor.add_donation(amount)
                break
        else:
            self.add_donor(fullname, [amount])
        print(self._format_letter(fullname, amount))

    def add_donor(self, fullname, donations=None):
        self.donors.append(Donor.from_fullname(fullname, donations))

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
            filename = ''.join([fullname, ' ',
                                str(date.today()),
                                '.txt'])
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


# initialize the database
db = DataBase([Donor('Jeff', 'Bezos', [3.65, 54.50]),
               Donor('Mark', 'Zuckerberg', [36.54, 1.25, 54.87]),
               Donor('Paul', 'Allen', [17.38]),
               Donor('William', 'Gates', [25.55, 33.33, 78.14])
               ])


def menu_selection(prompt, selection_dict):
    """Return options for user to select from."""
    while True:
        userinput = input(prompt)
        if selection_dict.get(userinput) is None:
            print('\n{} is not a valid selection. '
                  'Please try again!'.format(userinput))
        else:
            if selection_dict.get(userinput)() == 'Exit Menu':
                break


def fullname_input():
    """Return prompt asking for full name."""
    return input('Enter a donor first and last name > ').title()


def amount_input():
    """Return prompt asking for donation amount."""
    while True:
        try:
            amount = float(input('Enter donation amount! > '))
        except ValueError:
            print('\nPlease enter dollar amount and NOT text!')
        else:
            break
    return amount


def exit_menu():
    """Return 'Exit Menu'."""
    return 'Exit Menu'


def send_thankyou_email():
    """Return a menu selection to send thank you email to donor."""
    menu_selection(thankyou_prompt, thankyou_dict)


main_prompt = ('\nEnter "q" to "Exit Menu" \n'
               'Enter "1" to "Send a Thank You" \n'
               'Enter "2" to "Create a Report" \n'
               'Enter "3" to "Send Letters to Everyone" \n'
               'What do you want to do? > '
               )

main_dict = {'q': exit_menu,
             '1': send_thankyou_email,
             '2': db.create_report,
             '3': db.send_letters
             }

thankyou_prompt = ('\nEnter "q" to "Exit Menu" \n'
                   'Enter "1" to "List Donors" \n'
                   'Enter "2" to "Enter a Donor Name" \n'
                   'What do you want to do? > '
                   )

thankyou_dict = {'q': exit_menu,
                 '1': db.list_donors,
                 '2': db.donor_and_amount
                 }


if __name__ == "__main__":
    menu_selection(main_prompt, main_dict)
