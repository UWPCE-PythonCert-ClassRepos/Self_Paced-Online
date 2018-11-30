#!/usr/bin/env python3

"""
A class-based system for managing donor information
"""

class Donor():

    def __init__(self, first, last, amount):
        self.first_name = first
        self.last_name = last
        self.donations = [amount]

    def add_donation(self, amount):
        self.donations.append(amount)

    @property
    def total(self):
        return sum(self.donations)

    @property
    def count(self):
        return len(self.donations)

    @property
    def average(self):
        return self.total/self.count


class DonorCollection():

    def __init__(self, donor_list=None):
        self.donorlist = donor_list

    def add_donor(self, first, last, amount):
        if self.donorlist == None:
            self.donorlist = [Donor(first, last, amount)]
        else:
            self.donorlist.append(Donor(first, last, amount))

    def load_donors(self, filename='donor_list.txt'):
        with open(filename, 'r') as f:
            for line in f:
                load = line.split(';')
                amount = [float(_) for _ in load[2].split(',')]
                self.add_donor(load[0],load[1],amount)

    def save_donors(self, filename='donor_list.txt'):
        with open(filename, 'w') as f:
            for donor in self.donorlist:
                f.write("{};{};{}\n".format(donor.first_name, donor.last_name,
                                            ','.join(str(a) for a in donor.donations)))

    def find_donor(self, first=None, last=None):
        pass


