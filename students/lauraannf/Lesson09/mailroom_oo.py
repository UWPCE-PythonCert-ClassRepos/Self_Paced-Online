# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:50:47 2018

@author: Laura.Fiorentino
"""


#class Donor():
#    def __init__(self, name, donation):
#        if type(donation) is list:
#            self.donors = {name: donation}
#        else:
#            self.donors = {name: [donation]}
#
#    def new_donation(self, name, donation):
#        if type(donation) is not list:
#            donation = [donation]
#        try:
#            self.donors[name].append(donation)
#        except KeyError:
#            self.donors[name] = donation
#
#    def total_donation(self, name):
#        return sum(self.donors[name])
#
#    def number_donations(self, name):
#        return len(self.donors[name])
#
#    def avg_donation(self, name):
#        return sum(self.donors[name]) / len(self.donors[name])

class Donor():
    def __init__(self, name, donation):
        self.name = name
        if type(donation) is list:
            self.donations = donation
        else:
            self.donations = [donation]

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


class Donor_List():
    def __init__(self):
        self.donor_list = {}

    def add_donation(self, name, donation):
        if name in self.donor_list:
            self.donor_list[name].add_donation(donation)
        else:
            self.donor_list[name] = Donor(name, donation)
