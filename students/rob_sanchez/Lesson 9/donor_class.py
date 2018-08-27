#!/usr/bin/env python3


class Donations():
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

    # Returns average donation values
    @property
    def avg_donations(self):
        return {key: sum(self.donor_dict[key])/len(self.donor_dict[key]) for key in self.donor_dict}

    # Returns a list of donor names
    def get_list_of_donors(self):
        key_list = []
        for key in self.donor_dict.keys():
            key_list.append(key)
        return key_list

    # Returns a formatted list of donor names
    def get_formatted_list_of_donors(self):
        form_string = ", ".join(["{:s}"] * len(self.donor_dict))
        return ("List of Donors: " + form_string.format(*self.donor_dict))

    # Returns the total donations for each donor
    @property
    def donation_totals(self):
        return {key: sum(self.donor_dict[key]) for key in self.donor_dict}

    # Returns donation summary ordered by donation amount
    @property
    def get_summary(self):
        headers = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
        str_format = "{:<30} ${:>17} {:>16} ${:>14}"
        print(("\n{:<30} | {:^15} | {:^15} | {:^15}").format(*headers))
        print("-"*82)

        for key, value in sorted(self.donor_dict.items(), key=lambda i: sum(i[1]), reverse=True):
            print(str_format.format(key, round(float(sum(self.donor_dict[key])), 2),
                  len(self.donor_dict[key]),
                  round(sum(self.donor_dict[key])/len(self.donor_dict[key]), 2)))

    def get_donor_summary(self, donor):
        summary = {}
        donation = self.donor_dict[donor][-1:]

        summary["donor_name"] = donor
        summary["last_donation"] = str(donation).strip('[]')
        summary["total"] = round(sum(self.donor_dict[donor])/len(self.donor_dict[donor]), 2)

        return summary


# Class that holds a history of the donor's name and donation amount
class Donor():
    def __init__(self):
        self.donor_details = {}

    def add_donor(self, name):
        self.donor_details["donor_name"] = name

    def add_donation(self, amount):
        self.donor_details["amount"] = amount

    def get_donor_details(self):
        return self.donor_details
