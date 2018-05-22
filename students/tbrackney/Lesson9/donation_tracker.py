#!/usr/bin/env python3
"""
File Name: donation_tracker.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 5/16/2018
Python Version: 3.6.4
"""


class Donor:
    """
    Instance of donor class for each donor.  Takes a tuple of
    (name, [donations]) and has methods for finding total donations and
    average donation.  Sorts on donor name or total donations
    """
    def __init__(self, *args, **kwargs):
        """
        Expected input format is a tuple containting a donor name
        and a list of donation values.
        """
        self.name = str(args[0])
        # Using protected _donations value because I don't want people
        # overwriting These values.  I don't mind if they change the donor name.
        try:
            self._donations = [float(x) for x in args[1]]
        except IndexError:
            self._donations = []

    def add_donation(self, val):
        """ Appends a positive numerical value to donations"""
        if val < 0:
            raise ValueError('Donation must be greater than 0')
        self._donations.append(float(val))

    def sort_key(self):
        return self.name

    def sort_by_total(self):
        return self.total

    @property
    def donations(self):
        return self._donations

    @property
    def total(self):
        return sum(self._donations)

    @property
    def count(self):
        return len(self._donations)

    @property
    def average(self):
        try:
            return self.total / self.count
        except ZeroDivisionError:
            return 0


class Donorlist:
    """
    Instance of a list of donors, implemented as a dictionary.  Implements
    methods used in mailroom5.
    """
    def __init__(self, init_list=None):
        """Takes dictionary value using format {'donor1', ['donations1']} """
        self._donor_objects = {}
        self._short_template = "Dear {}, thank you for your generous donation of ${:.2f}\n"
        self._long_template = ('Dear {},\n'
                               '\n'
                               '        Thank you for your kind donations totaling ${:.2f}\n'
                               '\n'
                               '        Your gifts will be put to very good use.\n\n'
                               '                            Sincerely\n'
                               '                                -The Team\n'
                               )

        if init_list:
            for d in init_list:
                self._donor_objects[d[0]] = Donor(*d)

    def __contains__(self, val):
        """ Returns if a name is in the list of donors"""
        return val in self._donor_objects.keys()
        pass

    def get_donor(self, val):
        """Returns a single donor object.  Not using in mailroom"""
        if val in self._donor_objects.keys():
            return self._donor_objects[val]

    def list_donors(self):
        """Returns a list of donors sorted by name"""
        return sorted(self._donor_objects.keys())

    def list_by_total(self):
        """Returns a list of donors sorted by total donations"""

        return tuple(
                     sorted(self._donor_objects.values(),
                            key=Donor.sort_by_total,
                            reverse=True))

    def list_donations(self, name):
        """Returns list of donations for a donor"""
        if name in self._donor_objects.keys():
            return self._donor_objects[name].donations
        else:
            raise ValueError('Donor not in list')

    def add_donor(self, name):
        """Adds a new donor to the list with a blank donation history"""
        if name not in self._donor_objects.keys():
            self._donor_objects[name] = Donor(name, [])
        else:
            raise ValueError(f"Duplicate name in {type(self)}")

    def add_donation(self, name, amt):
        self._donor_objects[name].add_donation(amt)

    def send_thankyou(self, name, amt, template='short'):
        """
        Sends thank you note after donation.  Can pass an alternate template
        if desired.
        """
        if template == 'short':
            template = self._short_template
        elif template == 'long':
            template = self._long_template
        return template.format(name, amt)

    def create_report(self, file_out):
        """Prints report of all donors"""
        categories = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
        spacing = "{:<20} $ {:>10.2f} {:>10}     $ {:>10.2f}\n"
        sorted_tuple = self.list_by_total()
        header = "{:<20}| {:>10} | {:>10} | {:>10}\n"
        file_out.write(header.format(*categories))
        for donor in sorted_tuple:
            file_out.write(spacing.format(donor.name, donor.total, donor.count, donor.average))

    def get_total(self, name):
        """Returns total donations for donor"""
        return self._donor_objects[name].total
