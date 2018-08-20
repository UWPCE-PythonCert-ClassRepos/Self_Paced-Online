#!/usr/bin/env python3


class Donor():
    def __init__(self):
        self.donor_dict = {}

    def add_donation(self, name, amount):
        self.donor_dict.setdefault(name, []).append(float(amount))

    # Returns number of donations
    @property
    def num_donations(self):
        return {key: len(self.donor_dict[key]) for key in self.donor_dict}

    # Returns number of donations
    @property
    def avg_donations(self):
        return {key: sum(self.donor_dict[key])/len(self.donor_dict[key]) for key in self.donor_dict}

    # Informal string representation of an object
    def list_of_donors(self):
        form_string = ", ".join(["{:s}"] * len(self.donor_dict))
        return ("List of Donors: " + form_string.format(*self.donor_dict))
