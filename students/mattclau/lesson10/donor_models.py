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


    def create_letter(self):
        """Creates letter for the supplied donor name and amount"""
        letter = f'Dear {self.name},\n'
        letter += f'\tThank you for your donation of ${self.donations[-1]:,.2f} to the foundation.'

        if len(self.donations) > 1:
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
        """sort key by sum of donations"""
        return sum(self.donations)

    def sort_len(self):
        """sort key by count of donations"""
        return len(self.donations)

    def sort_avg(self):
        """sort key by average of donations"""
        return self.donation_avg()


    def __eq__ (self, donor2):
        """override equality for comparing donors based on donations"""
        return sum(self.donations) == sum(donor2.donations) and self.name == donor2.name

    def __lt__ (self, donor2):
        """override less than for comparing donors based on less than"""
        return sum(self.donations) < sum(donor2.donations)

class DonorCollection:

    def __init__(self, donors):
        """set initial list of donors"""
        self.donors = donors

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

    def match_donations(self, factor, min_don=0, max_don=999999999, projection = False):
        """creates new donor database with matching donations, use min and max to filter values if passed in"""
        donor_list = []
        prev_donations = 0.0
        new_donations = 0.0

        for donor in self.donors:
            name = donor.name
            donations = donor.donations


            donations = list(filter(lambda donation: min_don <= donation <= max_don, donations))

            donations = list(map(lambda donation: donation * factor, donations))

            if donations != []:
                new_donor = Donor(name, donations)
                donor_list.append(new_donor)
                prev_donations += sum(donations) / factor
                new_donations += sum(donations)

        projected_total = new_donations - prev_donations

        new_donors = DonorCollection(donor_list)

        return new_donors, projected_total

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
