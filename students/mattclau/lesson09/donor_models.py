from operator import itemgetter
import os

class Donor:

    def __init__(self, name, donations = [None]):
        """creates a Donor object"""
        self.name = name
        self.donations = []
        if donations != [None]:
            for donation in donations:
                self.donations.append(donation)


    def create_letter(self,donor):
        """Creates letter for the supplied donor name and amount"""
        letter = f'Dear {donor.name},\n'
        letter += f'\tThank you for your donation of ${donor.donations[-1]:,.2f} to the foundation.'

        if len(donor.donations) > 1:
            letter += f'\tWe also thank you for your continuing support and appreciate that you are a repeat giver.'

        letter += '\tYour generous gift will make a tremendous difference in the coming years.\n\n'
        letter += 'Sincerely,\n\tDirector of the Foundation\n'
        return letter

    def add_donation(self, amount):
        """Adds donation amount for donor"""
        self.donations.append(amount)

    def donation_avg(self):
        """returns average of donations for donor"""
        return sum(self.donations)/len(self.donations)

    def sort_sum(self):
        return sum(self.donations)

    def sort_len(self):
        return len(self.donations)

    def sort_avg(self):
        return self.donation_avg()


    def __eq__ (self, donor2):
        """override equality for comparing donors based on donations"""
        return sum(self.donations) == sum(donor2.donations) and self.name == donor2.name

    def __lt__ (self, donor2):
        """override less than for comparing donors based on less than"""
        return sum(self.donations) < sum(donor2.donations)

class DonorCollection:

    def __init__(self, donors = None):
        """set initial list of donors"""
        self.donors = []

        if donors == None:
            d1 = Donor("Douglas Adams",donations = [1000])
            d2 = Donor("Bruce Lee",donations = [9876.55])
            d3 = Donor("Charles Barkley",donations = [999999.99,55555.55,7777.77])
            d4 = Donor("Scottie Pippen",donations = [1, 5])
            d5 = Donor("Ursula K Le Guin",donations = [534567.89])

            donorlist = [d1, d2, d3, d4, d5]
        else:
            donorlist = donors

        for donor in donorlist:
            self.donors.append(donor)

    def check_for_donor(self, name):
        """checks to see if donor has already been added"""
        for donor in self.return_donors():
            if name == donor.name:
                return True
        return False

    def add_donor(self, donor):
        """adds new donor to collection"""
        self.donors.append(donor)

    def return_donors(self):
        """returns all donors currently in collection"""
        return self.donors

    def get_donor_from_name(self, name):
        """returns the donor object for the name passed in"""
        for donor in self.donors:
            if donor.name == name:
                return donor

    def aggregate_donations(self, desc=False, sort_type='sum'):
        """Aggregates the donations from the donors and returns them in a sorted list as requested"""
        donor_list = []
        for donor in self.return_donors():
            donor_list.append(donor)

        if sort_type == 'sum':
            donor_list.sort(key=Donor.sort_sum, reverse=desc)
        elif sort_type == 'avg':
            donor_list.sort(key=Donor.sort_avg, reverse=desc)
        elif sort_type == 'len':
            donor_list.sort(key=Donor.sort_len, reverse=desc)

        donor_totals = [[donor.name,sum(donor.donations),len(donor.donations),donor.donation_avg()] for donor in donor_list]

        return donor_totals
