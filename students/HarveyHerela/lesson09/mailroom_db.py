class Donor:
    def __init__(self, firstname, lastname):
        self.name = (firstname, lastname)
        self.donations = list()


    def add_donation(self, amount):
        self.donations.append(amount)


    def get_donations(self):
        return self.donations


    def get_key(self):
        return self.name


    def get_name(self):
        return "{0} {1}".format(*self.name)


class DonorCollection:
    def __init__(self):
        self.donors = dict()


    def add_donor(self, donor):
        self.donors[donor.get_key()] = donor


    def get_donors(self):
        return self.donors.values()


    def add_donation(self, firstname, lastname, amount):
        d = Donor(firstname, lastname)
        key = d.get_key()
        if key not in self.donors:
            self.donors[key] = d
        self.donors[key].add_donation(amount)
