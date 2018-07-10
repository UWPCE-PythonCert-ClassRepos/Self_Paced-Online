#!/usr/bin/python3

## Author/student:  Roy Tate (githubtater)

import os
import copy


class Donor:

    def __init__(self, name, amount):
        if not name:
            raise ValueError('Please provide a donor name.')
        if not amount:
            raise ValueError('Please provide a donation amount')
        self.name = name.title()
        self.donations = []
        self.add_donation(amount)

    def __add__(self, other):
        new_donation = self.amount
        if isinstance(other, (int, float)):
            new_donation += other
        elif isinstance(other, Donor):
            new_donation += other.amount
        return Donor(new_donation)

    def __str__(self):
        return 'Donor name: {}  Donations: {}'.format(self.name, self.donations)
        # return '{}'.format(self.donations)

    def __repr__(self):
        # return 'Donor({}, {})'.format(self.name, sum(self.donations))
        return 'Donor({}, {})'.format(self.name, self.donations)

    def add_donation(self, new_donation):
        self.donations.append(new_donation)

    @property
    def total_donations(self):
        return round(sum(self.donations), 2)

    @property
    def average(self):
        return round(self.total_donations / self.num_gifts, 2)

    @property
    def num_gifts(self):
        return len(self.donations)

    @property
    def max_donation(self):
        return max(self.donations)

    @property
    def min_donation(self):
        return min(self.donations)

    @property
    def all_donations(self):
        return self.donations

    @property
    def letter(self):
        text = '''\n
From:    A Charity Thankful For Your Kindness
To:      {0}
Subject:  This Year's Challenge!

Dear {0},

First, we would like to thank you for your continued generosity throughout the 
years. Without contributions like yours, the good things that we are able to do 
simply would not be possible. 

Your contributions to date have totaled ${1:.2f}. 

This years challenge is to see if you can donate more than your current total
in one year. This would effectively double your current donations to the 
organization!  Remember, it is for a good cause!

Sincerely,

The good guys at the best organization
'''

        return text.format(self.name, sum(self.donations))


class DonorCollection():

    def __init__(self):
        self.donors = {}
        self.factor = 1.0
        self.lowest = 0.0
        self.highest = 1e11

    def __repr__(self):
        return 'DonorCollection()'

    def print_all(self):
        print('\n{:-^20}'.format('Donor List'))
        for donor in sorted(self.donors):
            print(donor)
        print('\n')

    def add(self, name, amount):
        name = name.title()
        if isinstance(amount, list):
            for amounts in amount:
                if name in self.donors:
                    self.donors[name].add_donation(amounts)
                else:
                    self.donors[name] = Donor(name, amounts)
        elif name in self.donors:
            self.donors[name].add_donation(amount)
        else:
            self.donors[name] = Donor(name, amount)

    def create_report(self):
        format_str = '{:<25}{:<15}{:<15}{:<15}{:<15}{:<15}'
        report = '\n{:-^100}\n'.format('DONATION REPORT')
        report += (format_str+'\n').format('Name', 'Total Given', '# of Gifts', 'Average', 'Max', 'Min')
        for v in self.donors.values():
            donor_values = (v.name, '$' + str(v.total_donations), v.num_gifts, str(v.average),
                            str(v.max_donation), str(v.min_donation))
            report += (format_str + '\n').format(*donor_values)
        return report

    def create_projection_report(self, title):
        format_str = '{:<25}{:<17}{:<15}{:<15}{:<15}'
        report = '\n{:*^100}\n'.format(f'  Projection Report - {title}  ')
        report += (format_str+'\n').format('Name', 'New_Total_Given', 'New_Max', 'New_Min', 'Average')
        for v in self.donors.values():
            donor_values = (v.name, '$' + str(v.total_donations), str(v.max_donation), str(v.max_donation),
                            str(v.min_donation), str(v.average))
            report += (format_str + '\n').format(*donor_values)
        return report

    def save_emails(self, directory=''):
        cwd = os.getcwd()
        if not directory:
            directory = cwd
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass
        finally:
            os.chdir(directory)
            directory = os.getcwd()
            emails = {k + '.txt': v.letter for k, v in self.donors.items()}
            for filename, text in emails.items():
                with open(filename, 'w+') as f:
                    f.write(str(text))
            return directory

    def challenge(self, factor, min_donation=1.00, max_donation=1e11):
        """Increase all donations in the database by a factor
        Args:
            factor:  the amount to multiply the donatoins by
            min_donation:  the minimum donation to filter
            max_donation:  the maximum donation to filter
        Return
            self.new_collection:  a DonorCollection() of the donors with donation values multiplied by the factor"""
        self.factor = factor
        self.new_collection = DonorCollection()
        multiplied_data = dict(list((name, list(map(lambda x: x * factor, donations.donations))) for name, donations in self.donors.items()))
        for donor, donations in multiplied_data.items():
            # new_donation_map = map(self.multiply_donations, new_donation_list)
            self.new_collection.add(donor, donations)
        return self.new_collection


    def run_projections(self):
        """Run an automated projection report for tripling donations under $50 and doubling donations over $100
        Args:
            None
        Returns:
            self.projection_collection50:  a DonorCollection() with donors and their donations under $50, tripled
            self.projection_collection100:  a DonorCollection() with donors and their donations over $100, doubled"""
        self.projection_collection100 = DonorCollection()
        self.projection_collection50  = DonorCollection()
        double_over_100 = dict(list(
            (name, list(map(lambda x: x * 2, donations.donations))) for name, donations in self.donors.items()))
        triple_under_50 = dict(list(
            (name, list(map(lambda x: x * 3, donations.donations))) for name, donations in self.donors.items()))
        for donor, donations in double_over_100.items():
            self.projection_collection100.add(donor, donations)
        for donor, donations in triple_under_50.items():
            self.projection_collection50.add(donor, donations)
        return self.projection_collection50, self.projection_collection100

