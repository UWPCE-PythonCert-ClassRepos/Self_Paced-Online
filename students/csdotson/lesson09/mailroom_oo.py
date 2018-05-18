#!/usr/bin/env python3
# Lesson 9 - Object-oriented Mailroom

class Donor:
    """ Create Donor class representing a donor and all donations """
    def __init__(self, name, donations):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be a string value")
        self.donations = donations if donations else []


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
            raise ValueError("Donation can't be negative")
        self.donations.append(donation)


    def __repr__(self):
        return "Donor({},{})".format(self.name, repr(self.donations))

    def __str__(self):
        # Probably need one of these, right?


class DonorCollection(Donor):
    """ Create container object to hold multiple donors """
    def __init__(self, donors):
        self.donors = donors
        # donors should be collection of donor objects

    ## Idexing of donor objects

    def add_new_donor(self, new_donor, new_donation):
        # Add new Donor object to the collection
        pass


    def find_donor(self, donor):
        # Return Donor object based on name
        pass

    def __repr__(self):
        pass # Take parent repr and add looping capability


d1 = Donor("Chris", [100.00, 20.00, 35.00])
d2 = Donor("Joe", [1.34, 5.67, 567.00])
d3 = Donor("Bob", [14.56, 56.78, 90.00])

donors = DonorCollection([d1, d2, d3])
