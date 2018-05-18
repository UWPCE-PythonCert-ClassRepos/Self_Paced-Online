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
        Expected input format is a list of tuples containting a donor name
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
        return self.total / self.count


class Donorlist:
    """
    Instance of a list of donors, implemented as a dictionary.  Implements
    methods used in mailroom5.
    """
    def __init__(self, **kwargs):
        """Takes dictionary value using format {'donor1', ['donations1']} """
        self._donors = kwargs.copy()

    @property
    def donor_names(self):
        return sorted(self._donors.keys())

    @property
    def get_donor(self, val):
        if val in self._donors.keys():
            return self._donor[val]
