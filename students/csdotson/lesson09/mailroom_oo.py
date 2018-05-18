#!/usr/bin/env python3
# Lesson 9 - Object-oriented Mailroom

class Donor:
    """ Create Donor class representing a donor and all donations """
    def __init__(self, name, donations):
        self.name = name
        self.donations = donations


    @property
    def total_donation(self):
        return sum(self.donations)


    @property
    def number_of_donations(self):
        return len(self.donations)


    @property
    def average_donation(self):
        return self.total_donation / self.number_of_donations


    def add_donation(self, donation):
        if donation < 0:
            raise ValueError("Donation can't be negative :)")
        self.donations.append(donation)


    def __repr__(self):
        return "Donor({},{})".format(self.name, repr(self.donations))



class DonorCollection:

    def __init__(self, donors):
        self.donors = donors


    def add_new_donor(self, new_donor, new_donation):
        pass


    def find_donor(self, donor):
        pass 
