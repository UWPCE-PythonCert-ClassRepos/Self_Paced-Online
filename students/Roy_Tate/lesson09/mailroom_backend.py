#!/usr/bin/python3

## Author/student:  Roy Tate (githubtater)

import os

class Donor:

    donor_dict = {}

    def __init__(self, name, amount):
        if not name:
            raise ValueError('Please provide a donor name.')
        if not amount:
            raise ValueError('Please provide a donation amount')
        self.name = name.title()
        self.donations = []
        self.add_donation(amount)

        # self.donor_dict[self._ln, self._fn] = [self._donations]
        # print(self.donor_dict)

    def __add__(self, other):
        new_donation = self.amount
        if isinstance(other, (int, float)):
            new_donation += other
        elif isinstance(other, Donor):
            new_donation += other.amount
        return Donor(new_donation)


    def __str__(self):
        return 'Donor name: {}  Donations: {}'.format(self.name, sum(self.donations))

    def __repr__(self):
        return 'Donor({}, {})'.format(self.name, sum(self.donations))

    def add_donation(self, new_donation):
        self.donations.append(round(new_donation, 2))

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

    def __repr__(self):
        return 'DonorCollection()'

    def print_all(self):
        print('\n{:-^20}'.format('Donor List'))
        for donor in sorted(self.donors):
            print(donor)
        print('\n')

    def add(self, name, amount):
        name = name.title()
        if name in self.donors:
            self.donors[name].add_donation(amount)
        else:
            self.donors[name] = Donor(name, amount)


    def create_report(self):
        format_str = '{:<20}{:<15}{:^13}{:<20}'
        report = '\n{:-^58}\n'.format('DONATION REPORT')
        report += (format_str+'\n').format('Name', 'Total Given', '# of Gifts', 'Avg. Gift')
        for v in self.donors.values():
            donor_values = (v.name, '$' + str(v.total_donations), v.num_gifts, '$' + str(v.average))
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

