#!/usr/bin/env python3

import pathlib
pth = pathlib.Path('./')


class Donor:

    def __init__(self, name):
        self._name = name
        self._donations = []
        self._rollup = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if not val:
            raise ValueError("A Donor must have a name.")
        self._name = val

    @property
    def donations(self):
        return self._donations

    def add_donation(self, val):
        if val < 1:
            raise ValueError("A positive donation value is required.")
        self.donations.append(val)

    @property
    def rollup(self):
        return self._rollup

    @rollup.setter
    def rollup(self, val):
        if not val:
            raise ValueError("Rollup values are required.")
        self._rollup = val


class DonorList:

    def __init__(self):
        self._donors = {}

    @property
    def donors(self):
        return self._donors

    def add_donor(self, name):
        donor = Donor(name)
        self.donors[donor.name] = donor

    def get_donor(self, name):
        if not name:
            raise ValueError("Please provide a donor name.")

        if name in self.donors:
            return self.donors[name]
        else:
            return "Donor not found."

    def get_donations(self, name):
        if not name:
            raise ValueError("Please provide a donor name.")

        if name in self.donors:
            return self.donors[name].donations
        else:
            return "Donor not found."

    def compose_thank_you(self, donor):
        if not donor:
            raise ValueError("Please provide a donor.")

        message_obj = {
            'donor_name': donor.name,
            'donation': donor.donations[-1]
        }
        message = 'Dear {donor_name}, thanks so much '\
                  'for your generous donation in the amount of: '\
                  '${donation}.'.format(**message_obj)
        return message

    def get_donor_names(self):
        print("\n".join([donor for donor in self.donors]))

    def generate_rollup(self):
        for donor in self.donors:
            cur_donor = self.donors[donor]
            number = len(cur_donor.donations)
            total = sum(cur_donor.donations)
            average = float(
                format(
                    sum(
                        cur_donor.donations) / len(
                            cur_donor.donations
                        ), '.2f'
                    )
                )
            cur_donor.rollup = dict(zip(('number', 'total', 'average'),
                                        (number, total, average)))

    def generate_table(self):
        self.generate_rollup()
        headings = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
        print('{:20}{:<15}{:<15}{:<15}'.format(*headings))
        print('{:_<65}'.format(''))
        for donor in self.donors:
            cur_donor = self.donors[donor]
            print('{:<20}'.format(cur_donor.name), ('{:<15}' * len(cur_donor.rollup))
                  .format(*cur_donor.rollup.values()))

    def generate_letters(self):
        self.generate_rollup()
        for donor in self.donors:
            with open(donor.replace(' ', '_') + '.txt', 'w') as outfile:
                outfile.write(self.compose_thank_you(self.donors[donor]))
        print('Letters generated: ')
        for f in pth.iterdir():
            if '.txt' in str(f):
                print(f)
