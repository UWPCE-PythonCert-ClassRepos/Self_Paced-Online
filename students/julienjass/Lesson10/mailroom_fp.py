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

    @donations.setter
    def donations(self, first):
        self._donations = first

    def add_donation(self, donation):
        self._donations.append(donation)

    @property
    def total_donations(self):
        return sum(self._donations)

    @property
    def count_donations(self):
        return len(self._donations)

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
            report_rows.append('{:26s} {:>12s} {:^13d} {:>12s}'.format(d.name, '${:,.2f}'.format(d.total_donations), d.count_donations, '${:,.2f}'.format(d.average_donation)))
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

    @property
    def projection(self):
        return {d[0]:d[1] for d in self._projection}

    def challenge(self, x=1, mn=0, mx=float("inf")):
        self._projection = []
        for k, v in self.export.items():
            self._projection.append((k, list(map(lambda y: y * x, list(filter(lambda z: z >= mn and z <= mx, v))))))
        self._projection.sort(key=lambda z: sum(z[1]), reverse=True)
        # self.projection = {d[0]:d[1] for d in self._projection}

    def projection_report(self):
        report_rows = []
        for d in self._projection:
            report_rows.append('{:26s} {:>12s} {:^13d} {:>12s}'.format(d[0], '${:,.2f}'.format(sum(d[1])), len(d[1]), '${:,.2f}'.format(sum(d[1]) / len(d[1]))))
        header = ('Donor Name                | Total Given | Num Gifts | Average Gift\n') + ('-' * 66) + '\n'
        return header + '\n'.join(report_rows) + '\n'


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


def print_projection():
    print('\nProjection totals for a donation challenge:\n')
    print('Please enter a donation multiplying factor')
    factor = input('Your Choice: ')
    ex = 0
    while ex == 0:
        try:
            factor = float(factor)
        except ValueError:
            print('Please enter a valid multiplier')
            multiplier = input('Your Choice: ')
            continue
        else:
            ex = 1
    print('Please enter the minimum donation to consider (Just write 0 if there is no minimum)')
    minimum = input('Your Choice: ')
    check = 0
    while check == 0:
        try:
            minimum = float(minimum)
        except ValueError:
            print('Please enter a minimum which is valid.')
            mn = input('Your Choice: ')
            continue
        else:
            check = 1
    print('Enter the maximum donation to consider (leave blank for no maximum)')
    maximum = input('Your Choice: ')
    while (maximum != '') and (type(maximum) not in [int, float]):
        print('Please enter a maximum which is valid')
        maximum = input('Your Choice: ')
    if maximum == '':
        maximum = float("inf")
    donor_db.challenge(factor, minimum, maximum)
    print('\nProjected report based on past donations:')
    print(donor_db.projection_report())
    return


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
    '3': ['Create a Projected Report', print_projection],
    '4': ['Send letters to all donors', write_letters_on_disk],
    '5': ['Quit', leave]
    }

thank_you_menu = {
    '1': ['Enter a donor', get_name_donation]
    , '2': ['See a list of donor names', print_donor_list]
    , '3': ['Return to Main Menu', return_to_main]
    }

def mainloop():
    print('Welcome to Mailroom\n')
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
