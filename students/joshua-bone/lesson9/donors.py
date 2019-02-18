# Joshua Bone - UW Python 210 - Lesson 9
# 02/10/2019
# Assignment: Mailroom, Object Oriented

from donor import Donor

class Donors:
    def __init__(self):
        self._index = {}

    @property
    def donor_names(self):
        return self._index.keys()

    def add_donor(self, donor):
        self._index.update({donor.name: donor})

    def get_donor(self, name):
        return self._index.get(name)

    def add_donation(self, name, amt):
        d = self.get_donor(name)
        if d is None:
            self.add_donor(Donor(name, amt))
        else:
            d.add_donation(amt)

