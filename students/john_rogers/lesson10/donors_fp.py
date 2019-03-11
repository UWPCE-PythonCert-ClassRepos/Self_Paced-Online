"""
Donor classes for mailroom_fp.py
Author: JohnR
Version: 2.1
Last updated: 3/6/2019
Notes: incorporating feedback from Natasha
"""

from datetime import date


class Donor(object):
    """
    Class for single donor methods and attributes
    """
    def __init__(self, first, last, donations=None):
        self.first = first
        self.last = last
        if isinstance(donations, float):
            donations = [donations]
        self.donations = list(donations)

    def __repr__(self):
        return f'{self.first} {self.last} is' \
            f' listed as a donor.'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @property
    def total_donations(self):
        return round(sum(self.donations), 2)

    @property
    def number_of_donations(self):
        return len(self.donations)

    @property
    def get_donations(self):
        return self.donations

    @property
    def avg_donation_amount(self):
        return round(self.total_donations / self.number_of_donations, 2)

    def amped_donations(self, factor):
        return list(map(lambda x: x * factor, self.get_donations))

    def filtered_donations(self, min_amount=0, max_amount=999999999):
        return list(filter(lambda x: min_amount <= x <= max_amount,
                           self.get_donations))

    def new_donation(self, amount):
        self.donations.append(amount)

    def form_letter(self):
        """
        create a form letter
        :return: form letter filled in with donor and amount
        """
        letter = (
            f'Hey {self.full_name}, thanks for your donations! '
            f'As of today, {DonorDataBase.today}, you have donated a total of '
            f'${self.total_donations}.'
        )

        return letter


class DonorDataBase(object):
    """
    Class for managing multiple donors
    """
    today = date.today()

    def __init__(self, donors=None):
        self.donors = []
        if donors:
            self.donors = donors

    def add_donor(self, donor):
        self.donors.append(donor)

    def donor_names(self):
        return [d.full_name for d in self.donors]

    def total_amount_raised(self):
        return sum([d.total_donations for d in self.donors])

    def total_number_donations(self):
        return sum([d.number_of_donations for d in self.donors])

    def thank_all(self):
        for donor in self.donors:
            letter = donor.form_letter()
            print(letter)
            print()

    def save_report(self):
        print('Saving database to disk...')
        for donor in self.donors:
            letter = donor.form_letter()
            user_file = "{}.{}.txt".format(donor.full_name,
                                           self.today)
            with open(user_file, 'w') as outfile:
                outfile.write(letter)
                print(user_file, ' has been saved to disk.')

    def print_summary(self):
        recipients = self.sorted_list()
        print()
        print('Donor Name       | Total Given | Num Gifts | Avg Gift Amount')
        print('-' * 60)

        for donor in recipients:
            print(f'{donor[0][0]:<17} ${donor[1][0]:^15} {donor[2][0]:^13}'
                  f'${donor[3][0]:^8}')

    def sorted_list(self):
        """
        Sort a give list of donors by total amount given, large to small
        :return: sorted list of donors
        """
        sorted_donors = []

        for donor in self.donors:
            sorted_donors.append([[donor.full_name],
                                 [donor.total_donations],
                                 [donor.number_of_donations],
                                 [donor.avg_donation_amount]])

        sorted_donors.sort(key=lambda x: x[1], reverse=True)
        return sorted_donors

    def get_donor(self, name):
        for i in self.donors:
            if i.full_name == name:
                return i

