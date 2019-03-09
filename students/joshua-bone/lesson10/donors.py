# Joshua Bone - UW Python 210 - Lesson 10
# 03/08/2019
# Assignment: Functional Mailroom

from donor import Donor


class Donors:
    def __init__(self):
        self._index = {}

    @property
    def names(self):
        return list(self._index.keys())

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, index):
        self._index = index

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

    def challenge(self, factor, *, min_amt=None, max_amt=None):
        min_filter = ((lambda d: d > min_amt) if min_amt is not None
                      else (lambda d: True))
        max_filter = ((lambda d: d < max_amt) if max_amt is not None
                      else (lambda d: True))
        donors = Donors()
        donors.index = {name:
                        donor.copy(
                            filterFn=lambda d: min_filter(d) and max_filter(d),
                            mapFn=lambda amt: amt * factor
                        )
                        for name, donor in self.index.items()}
        return donors
