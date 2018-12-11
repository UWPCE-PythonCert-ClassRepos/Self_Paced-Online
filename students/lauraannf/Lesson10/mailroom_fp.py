# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:50:47 2018

@author: Laura.Fiorentino
"""


class Donor():
    def __init__(self, name, donation):
        self.name = name
        if type(donation) is list:
            self.donations = donation
        else:
            self.donations = [donation]

    def __iter__(self):
        return iter(self.donations)

    def add_donation(self, donation):
        self.donations.append(donation)

    @property
    def total_donation(self):
        return sum(self.donations)

    @property
    def number_donation(self):
        return len(self.donations)

    @property
    def avg_donation(self):
        return sum(self.donations) / len(self.donations)

    @property
    def list_donations(self):
        print(self.name + ' Donations: ' + ', '.join('${}'.format(d)
              for d in self.donations))

    @property
    def last_donation(self):
        return self.donations[-1]


class Donor_List():
    def __init__(self):
        self.donors = {}

    def __iter__(self):
        return self

    def add_donation(self, name, donation):
        if name in self.donors:
            self.donors[name].add_donation(donation)
        else:
            self.donors[name] = Donor(name, donation)

    def is_donor(self, name):
        if name in self.donors:
            return True
        else:
            return False
