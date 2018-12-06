#!/usr/bin/env python3

"""
A class-based system for managing donor information
"""

class Donor():

    def __init__(self, first, last, amount):
        self.first_name = first
        self.last_name = last
        if type(amount) is list:
            self.donations = amount
        else:
            self.donations = [amount]

    def add_donation(self, amount):
        if type(amount) is list:
            self.donations.extend(amount)
        else:
            self.donations.append(amount)

    def challenge(self, factor, min_donation=None, max_donation=None):
        if min_donation is not None:
            self.donations = list(filter(lambda x : x > min_donation, self.donations))
        if max_donation is not None:
            self.donations = list(filter(lambda x : x < max_donation, self.donations))
        self.donations = list(map(lambda x : x*factor, self.donations))

    @property
    def total(self):
        return sum(self.donations)

    @property
    def count(self):
        return len(self.donations)

    @property
    def average(self):
        if self.count == 0:
            return 0
        else:
            return self.total/self.count

    def __lt__(self, other):
        return self.total < other.total

    def __le__(self, other):
        return self.total <= other.total

    def __eq__(self, other):
        return self.total == other.total

    def __ge__(self, other):
        return self.total >= other.total

    def __gt__(self, other):
        return self.total > other.total

    def __ne__(self, other):
        return self.total != other.total


class DonorCollection():

    def __init__(self, donors=None):
        self.donorlist = donors

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

    @property
    def names(self):
        return [(donor.last_name, donor.first_name) for donor in self.donorlist]

    def find(self, first, last):
        if (last, first) in self.names:
            return self.donorlist[self.names.index((last, first))]
        else:
            return None

    def update(self, first, last, amount):
        if (last, first) in self.names:
            self.find(first, last).add_donation(amount)
        else:
            self.add_donor(first, last, amount)

    def challenge(self, factor, min_donation=None, max_donation=None):
        self.save_donors()
        new_data = DonorCollection()
        new_data.load_donors()
        for donor in new_data.donorlist:
            donor.challenge(factor, min_donation, max_donation)
        return new_data




