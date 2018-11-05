"""This is the file that holds the donation database, and has all the
classes for Donor, and DonorDonations
"""


class Donor(object):
    """This is the Donor class where we set up the functions that create a use-able database
    We initialize it, get the key name (first/last name) and the value (donations).
    This is used to hold the information about a SINGLE donor, so we can get name, donations
    and add, as well as the evaluation needed for sorting etc.
    """

    def __init__(self, name, donation_amount=None):
        self.name = name
        self.donation = list()
        if donation_amount is not None:
            for d in donation_amount:
                self.donation.append(d)
        else:
            self.donation = []

    def get_donation(self):
        return self.donation

    def get_name_as_key(self):
        return self.name

    def get_name_as_str(self):
        return "{}".format(self.name)

    def add_donation(self, donation_amount):
        self.donation.append(donation_amount)

    def get_num_donations(self):
        return len(self.donation)

    def get_recent_donations(self):
        return self.donation[-1]

    def get_total_donations(self):
        try:
            return sum(self.donation)
        except TypeError:
            return self.donation

    def get_avg_donations(self):
        try:
            return self.get_total_donations() / self.get_num_donations()
        except TypeError:
            return self.donation

    def __lt__(self, other_donor):
        return self.get_total_donations() < other_donor.get_total_donations()

    def __gt__(self, other_donor):
        return self.get_total_donations() > other_donor.get_total_donations()

    def __eq__(self, other_donor):
        return self.get_total_donations() == other_donor.get_total_donations()


class DonorCollection(object):
    """This is the Donor Collections class where we set up the functions to use the Donor
    class, database.
    """

    def __init__(self, db=None):
        if db is None:
            self.donors = []
        else:
            self.donors = db

    def add_new_donor(self, new_donor):
        self.donors.append(new_donor)

    def add_to_database(self, donor, donation):
        for d in self.donors:
            if d.name == donor:
                d.add_donation(donation)

    def get_all_donors(self):
        """This function lists all the donors in a database
        :return donor_list: Returns a list of all the names in the donor database
        """
        l = []
        for d in self.donors:
            l.append(d.get_name_as_key())

        return(l)

    def list_donors(self):
        """This function lists all the donors in a database
        :return donor_list: Returns a list of all the names in the donor database
        """
        for d in self.donors:
            print(d.get_name_as_str())

    def sorted_database(self):
        return(sorted(self.donors, reverse=True))
