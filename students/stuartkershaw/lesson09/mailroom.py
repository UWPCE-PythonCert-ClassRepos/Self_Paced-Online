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
