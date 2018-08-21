#!/usr/bin/env python3


class Donor():
    def __init__(self):
        self.donor_dict = {}

    # Add donor if it doesn't exist in current dictionary,
    # otherwise append their last contribution
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

    # Returns a list of donor names
    def list_of_donors(self):
        form_string = ", ".join(["{:s}"] * len(self.donor_dict))
        return ("List of Donors: " + form_string.format(*self.donor_dict))

    # Returns donation summary ordered by donation amount
    @property
    def get_summary(self):
        headers = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
        str_format = "{:<30} ${:>17} {:>16} ${:>14}"
        print(("\n{:<30} | {:^15} | {:^15} | {:^15}").format(*headers))
        print("-"*82)

        # sorted(self.donor_dict, key=self.donor_dict.sort_by_total)

        for key, value in self.donor_dict.items():
            print(str_format.format(key, round(float(sum(self.donor_dict[key])), 2),
                  len(self.donor_dict[key]),
                  round(sum(self.donor_dict[key])/len(self.donor_dict[key]), 2)))

    @staticmethod
    def sort_by_total(self):
        return self.avg_donations
