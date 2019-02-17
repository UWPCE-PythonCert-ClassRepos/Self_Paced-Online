"""
Donor classes for mailroom_L9.py
Author: JohnR
Version: .1 (Lesson 09)
Last updated: 2/17/2019
Notes: Guidelines:
        Works with one donor --> Donor class
        Works with multiple donors --> DonorDB
        User input --> Main script
        Complete separation of input and data handling
"""


class Donor(object):
    """
    Class for single donor methods and attributes
    """
    def __init__(self, first, last, donations=None):
        self.first = first
        self.last = last
        if isinstance(donations, int):
            donations = [donations]
        self.donations = list(donations)

    def __repr__(self):
        return f'{self.first.capitalize} {self.last.capitalize} is' \
            f' listed as a donor.'

    @property
    def full_name(self):
        return f'{self.first.capitalize} {self.last.capitalize}'

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def number_of_donations(self):
        return len(self.donations)

    @property
    def avg_donation_amount(self):
        return self.total_donations / self.number_of_donations

    def new_donation(self, amount):
        self.donations.append(amount)


class DonorDataBase(object):
    """
    Class for managing multiple donors
    """
    def __init__(self, donors=None):
        self.donors = []
        if donors:
            self.donors = donors

    def add_donor(self, donor):
        self.donors.append(donor)

    @property
    def donor_names(self):
        return [d.full_name for d in self.donors]

    @property
    def total_amount_raised(self):
        return sum([sum(d.donations for d in self.donors)])

    @property
    def total_number_donations(self):
        return sum([len(d.donations) for d in self.donors])




