# Joshua Bone - UW Python 210 - Lesson 9
# 03/01/2019
# Assignment: Mailroom, Object Oriented

from donor import Donor


class Donors:
    def __init__(self):
        self._index = {}

    @property
    def names(self):
        return list(self._index.keys())

    def get_all(self):
        return self._index.values()

    def add_donor(self, donor):
        self._index.update({donor.name: donor})

    def get_donor(self, name):
        return self._index.get(name)

    def add_donation(self, name, amt):
        d = self.get_donor(name)
        if d is None:
            d = Donor(name, amt)
            self.add_donor(d)
        else:
            d.add_donation(amt)
