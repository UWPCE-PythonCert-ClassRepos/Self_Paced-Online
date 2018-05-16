"""
Thomas Horn

Object Oriented refactor of mailroom_oo.py
"""

import os


class Donor:
    """
    Information about single donors.
    """
    def __init__(self, name, donations=None):
        self.name = name
        self.donations = donations

    @property
    def donor_totals(self):
        # Takes in a list --> use sum this time
        return sum(self.donations)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def average_donations(self):
        return self.donor_totals / self.num_donations

    def add_donation(self, donation):
        self.donations.append(donation)


class DonorList:
    """
    Holds a list of donor objects.

    Performs following after user inputs a donor:
        'list' input --> shows a list of donor names and reprompts
        adds donor if they do not exist or uses existing user
        prompts for a donation amd adds to donor
        prints thank you note
    """
    def __init__(self, donors=None):
        # Accepts only a list of donors now
        self.donors = donors

    def list_donor_names(self):
        # Better way of doing this?
        donor_names = [donor.name for donor in self.donors]
        return ('\n'.join(donor_names))

    def add_donor(self, new_donor):
        self.donors.append(new_donor)

    def add_donation(self, target_donor, new_donation):
        target_donor.add_donation(new_donation)
    
    def add_donor_and_donation(self, target_donor, new_donation):
        """ Called for a brand new donor only. """
        self.add_donor(target_donor)
        self.add_donation(target_donor, new_donation)
    
    def print_thanks(self, target_donor, new_donation):
        message = f"""Dear {target_donor},
        Thank you for you generous donation of ${new_donation:.2f}.
        It will truly help the children.

        Sincerely,
        # Donation Recievers"""
        print(message)

    def order_donors(self):
        """ 
        Orders the donors based on the sum of their total donations. 
        """
        ordered_donors = []
        for donor in self.donors:
            ordered_donors.append([donor])
        
        ordered_donors.sort(key=lambda x: x.donor_totals, reverse=True)
        return ordered_donors
        
        
        


if __name__ == "__main__":
    # Default collection of donors
    d1 = ("Tom Horn", [599.23, 1000.00])
    d2 = ("Theo Hartwell", [0.01, 0.01, 0.1])
    d3 = ("Bailey Kimmitt", [8723.22, 27167.22, 91817.66])
    d4 = ("Paul Hubbell", [90012.32, 2312.24])
    d5 = ("David Beckham", [1817266.11, 123123.66, 111335.112])

    # Add to donor book


