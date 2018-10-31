#!/usr/bin/env python3

class Donor:

    def __init__(self, name, amount):
        self._name = name
        self._amount = amount
        self._donation_count = 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    def add(self, donation_amount):
        self._amount += donation_amount
        self._donation_count += 1

    @property
    def donation_count(self):
        return self._donation_count

    @property
    def average(self):
        return self._amount / self._donation_count

    def __lt__(self, other):
        return self._amount < other._amount

    def __gt__(self, other):
        return self._amount > other._amount

    def __eq__(self, other):
        return self._amount == other._amount

class Donations:

    def __init__(self):
        """collection of donors"""
        self._donors = {}

    def add(self, donor):
        """ add donor"""
        # existing donor
        if donor.name in self._donors.keys():
            d =self._donors[donor.name]
            # update donation amount
            d.add(donor.amount)
        else:
            # new donor
            self._donors[donor.name] = donor
    @property
    def donors(self):
        return self._donors

