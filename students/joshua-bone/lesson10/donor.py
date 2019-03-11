# Joshua Bone - UW Python 210 - Lesson 10
# 03/08/2019
# Assignment: Functional Mailroom


class Donor:
    def __init__(self, name, donation=None):
        self._name = name
        self._donations = []
        if donation is not None:
            self.add_donation(donation)

    @property
    def name(self):
        return self._name

    # Returns immutable copy of donation list.
    @property
    def donations(self):
        return tuple(self._donations)

    @donations.setter
    def donations(self, donations):
        self._donations = donations

    @property
    def total_amt(self):
        return sum(self.donations)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def avg_donation(self):
        if len(self.donations) == 0:
            return 0
        return self.total_amt / float(self.num_donations)

    def add_donation(self, donation):
        self._donations.append(donation)

    def copy(self, *, mapFn=None, filterFn=None):
        new_donor = Donor(self.name)
        amts = self.donations
        if filterFn is not None:
            amts = filter(filterFn, amts)
        if mapFn is not None:
            amts = map(mapFn, amts)
        new_donor.donations = list(amts)
        return new_donor

    def __eq__(self, other):
        return type(self) == type(other) \
               and self.name == other.name \
               and self.donations == other.donations
