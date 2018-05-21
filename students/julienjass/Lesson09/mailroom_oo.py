#!/usr/bin/env python3

import os
import sys

db = {
    'William Gates, III': [261514, 392270],
    'Mark Zuckerberg': [4918, 9837, 1639],
    'Jeff Bezos': [877.33],
    'Paul Allen': [354, 212, 141]
    }


class Donor:
    
    def __init__(self, name, *donations):
        self._name = name
        self._donations = list(donations)

    @property
    def name(self):
        return self._name

    @property
    def donations(self):
        return self._donations

    def add_donation(self, donation):
        self._donations.append(donation)

    @property
    def count_donations(self):
        return len(self._donations)

    @property
    def total_donations(self):
        return sum(self._donations)

    @property
    def average_donation(self):
        return self.total_donations / self.count_donations

    @property
    def letter(self):
        return "Dear {:s},\n\nThank you for your donation of ${:,.2f}.\n\nBest regards,\nThe Organization".format(self._name, self._donations[-1])

    @property
    def filename(self):
        return self._name.replace(' ', '_') + '.txt'

    def __repr__(self):
        return "{}: {}".format(self._name, self._donations)  

class DonorDB:
    
    def __init__(self):
        self._donors = {}

    def add_donor(self, donor):
        if donor.name.lower() in self._donors:
            self._donors[donor.name.lower()].add_donation(*(donor.donations))
        else:
            self._donors[donor.name.lower()] = donor

    def get_total_from_donor(self, donor_name):
        return self._donors[donor_name.lower()].total_donations

    def get_donor(self, donor_name):
        try:
            return self._donors[donor_name.lower()]
        except KeyError:
            print('This Donor doesn''t exist in the database')

    @property
    def export(self):
        return {donor.name:donor.donations for donor in self._donors.values()}

    def donor_list(self):
        name_list = [donor.name for donor in self._donors.values()]
        return '\n'.join(name_list)

    def letters_on_disk(self):
        for donor in self._donors.values():
            print('Creating a letter for {:s}'.format(donor.name))
            with open(donor.filename, 'w') as outfile:
                outfile.write(donor.letter)
        print()

    def report(self):
        sorted_donors = [donor for donor in self._donors.values()]
        sorted_donors.sort(key=lambda donor: donor.total_donations, reverse=True)
        report_rows = []
        for d in sorted_donors:
            report_rows.append('{:27s} {:>12s} {:^13d} {:>12s}'.format(d.name, '${:,.2f}'.format(d.total_donations), d.count_donations, '${:,.2f}'.format(d.average_donation)))
        header = ('Donor Name                | Total Given | Num Gifts | Average Gift\n') + ('-' * 66) + '\n'
        return header + '\n'.join(report_rows) + '\n'

    @property
    def count_donors(self):
        return len(self._donors)

    @property
    def count_donations(self):
        return sum([len(donor.donations) for donor in self._donors.values()])

    @property
    def total_donations(self):
        return sum([donor.total_donations for donor in self._donors.values()])

    @property
    def average_total_donation(self):
        return self.total_donations / self.count_donors

    @property
    def average_single_donation(self):
        return self.total_donations / self.count_donations

    def __repr__(self):
        return str([d for d in self._donors.values()])


class Menu:
    
    response = None

    def __init__(self, title, menu):
        self._title = title
        self._menu = menu
        error_msg = 'This is not a valid response. Please enter '
        for key in self._menu:
            error_msg += key + ', '
        self._error = error_msg[:-3] + 'or ' +  error_msg[-3] + '.\n'

    def menu(self):
        m = [str(k) + ') ' + str(v[0]) + '\n' for k, v in self._menu.items()]
        return ''.join(m)

    def get_response(self):
        print(self._title)
        print(self.menu())
        response = input('Your choice: ')
        while response not in self._menu:
            print(self._error)
            response = input('Your choice: ')
        self.response = response

    @property
    def switch(self):
        return {k:v[1] for k, v in self._menu.items()}

    
def print_report():
    print(donor_db.report())


def return_to_main():
    return


def write_letters_on_disk():
    donor_db.letters_on_disk()
    return


def enter_name(name, amount):
    check = 0
    while check == 0:
        try:
            amount = float(amount)
        except ValueError:
            print('Please enter an amount which is valid')
            amount = input('Amount: ')
            continue
        else:
            ex = 1
    d = Donor(name, amount)
    donor_db.add_donor(d)
    print(d.letter)
    print()


def get_name_donation():
    print('\nEnter the name of the donor')
    donor_name = input('Name: ')
    print('Enter an amount')
    donation_amount = input('Amount: ')
    print()
    enter_name(donor_name, donation_amount)
    return


def print_donor_list():
    print('\nList of donors:')
    print(donor_db.donor_list(), '\n')
    pass


def thank_you():
    thank = Menu('Thank You Menu:', thank_you_menu)
    thank.get_response()
    thank.switch.get(thank.response)()
    return


def leave():
    sys.exit()


main_menu = {
    '1': ['Send a Thank You message', thank_you],
    '2': ['Create a Report', print_report],
    '3': ['Send letters to all donors', write_letters_on_disk],
    '4': ['Quit', leave]
    }

thank_you_menu = {
    '1': ['Enter a donor name', get_name_donation],
    '2': ['See a list of donor names', print_donor_list],
    '3': ['Return to the Menu', return_to_main]
    }

def mainloop():
    print('Mailroom Application\n')
    main = Menu('Main Menu:', main_menu)
    while True:
        main.get_response()
        main.switch.get(main.response)()

if __name__ == '__main__':
    donor_db = DonorDB()
    for n, d in db.items():
        donor = Donor(n, *d)
        donor_db.add_donor(donor)
    mainloop()
