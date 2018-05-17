#!/usr/bin/env python3

import pathlib
pth = pathlib.Path('./')


class Donor:

    def __init__(self, name):
        self._name = name
        self._donations = []

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


class DonorList:

    def __init__(self):
        self._donors = {}

    @property
    def donors(self):
        return self._donors

    def add_donor(self, name):
        donor = Donor(name)
        self._donors[donor.name] = {"donations": donor.donations}
