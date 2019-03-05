# Joshua Bone - UW Python 210 - Lesson 9
# 02/10/2019
# Assignment: Mailroom, Object Oriented


class Donor:
    def __init__(self, name, donation):
        self._name = name
        self._donations = []
        self.add_donation(donation)

    @property
    def name(self):
        return self._name

    # Returns immutable copy of donation list.
    @property
    def donations(self):
        return tuple(self._donations)

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

    def __eq__(self, other):
        return type(self) == type(other) \
               and self.name == other.name \
               and self.donations == other.donations
