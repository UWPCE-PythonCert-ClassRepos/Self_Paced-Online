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

#    def match_donations(self, match_value):
#        def multiplier(x):
#            return x * match_value
#        new_donor_list = Donor_List()
#        for key in self.donors:
#            new_donor_list.add_donation(key, list(map(multiplier,
#                                                      self.donors[key])))
#        return new_donor_list


def create_report(donor_list):
    print('-------List of Donors-------')
    print('{:<20}{:<20}{:<20}{:<20}'.format('Donor Name', 'Total Donated',
                                            '# of donations',
                                            'Average donation'))
    print('-----------------   '*4)
    for key in donor_list.donors.keys():
        print('{:<20}${:<20.2f}{:<20d}$'
              '{:<20.2f}'.format(key, donor_list.donors[key].total_donation,
                                 donor_list.donors[key].number_donation,
                                 donor_list.donors[key].avg_donation))


def list_donors(donor_list):
    for key in donor_list.donors:
        print('{}'.format(key))
