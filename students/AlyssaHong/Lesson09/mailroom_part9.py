"""
Author: Alyssa Hong
Date: 1/11/2019
Update: add new_donor
Lesson9 Assignments > Mailroom, Object Oriented Mailroom
"""

#!/usr/bin/env python3

import os

list_col = ['Donor Name','Total Given','Num Gifts','Average Gift']


class Donor:
    def __init__(self, first_name, last_name, donations = None):
        self.first = first_name
        self.last = last_name
        self.donations = donations

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def add_donation(self, new_donation):
        return self.donations.append(new_donation)

    def total_donation(self):
        return sum(self.donations)

def donor_input():
    return input("Type the donor's name: ")

def donation_input():
    return float(input("Type your donations: "))

class DornorList:
    def __init__(self, donors = None):
        if donors is None:
            self.donors = []
        else:
            self.donors = donors

    def add_donor(self, donor):
        self.donors.append(donor)

    def check_donor_list(self):
        return [donor.full_name for donor in self.donors]

    def send_thanks(self):
        donor_name = None
        while not donor_name:
            donor_name = donor_input()
            if donor_name.lower() == "list":
                print(self.check_donor_list())
        donation = None
        while not donation:
            try:
                donation = donation_input()
            except ValueError:
                print("Please enter a number: ")

        if donor_name not in self.check_donor_list():
            try:
                first, last = donor_name.split(" ")
                self.add_donor(Donor(first, last, [donation]))
            except ValueError:
                print("Please type the full name")
        else:
            for donor in self.donors:
                if donor.full_name == donor_name:
                    donor.add_donation(donation)

        print('\n' + 'Dear {:s}, thank you for your ${:.2f} donation!'.format(donor_name, donation) + '\n')

    def donations_report(self):
        reports = []
        for donor in self.donors:
            reports.append([donor.full_name, sum(donor.donations), len(donor.donations)])
        return reports

    def create_report(self):
        print('{:<20} | {:^10} | {:^10} | {:^10}'.format(*list_col))
        print('{}'.format("-"*63))

        for donor_report in self.donations_report():
            print('{:<20} | {:^10} | {:^10} | {:^10}'.format(donor_report[0], donor_report[1], donor_report[2], donor_report[1] / donor_report[2]))

    def send_letters(self):
        for donor in self.donors:
            file_name = donor.full_name + '.txt'
            with open(file_name, "w") as f:
                # f.write(letter_content(i, j))
                f.write('Dear {},'.format(donor.full_name) + '\n'*2 + '\t'*1 +
                        'Thank you for your donation of ${:.2f}.'.format(sum(donor.donations))+
                        '\n' + '\t'*1 + 'It will be put to very good use.\n'+'\t'*5 +'Sincerely,\n' +
                        '\t'*5 +'-The Team')

d1 = Donor('Fred', 'Lillywhite', [7000,4500])
d2 = Donor('Alex', 'Kim', [30000,30000,10000])
d3 = Donor('Henry', 'Ford', [5000])
d4 = Donor('Alyssa', 'Hong', [120000,30000,40000])
d5 = Donor('Leo', 'Jeon', [107000,53500])

dh = DornorList([d1, d2, d3, d4, d5])


def main():
    while True:
        print('\n'
            'Choose an action\n'
            '1 - Send a Thank you\n'
            '2 - Create a Report\n'
            '3 - Send letters to everyone\n'
            '4 - Quit')

        try:
            choice_action = int(input(': '))
        except ValueError:
            print("Your choice was wrong.\n""Choose an action again!")
        else:
            pass

        if choice_action == 1:
            dh.send_thanks()
        elif choice_action == 2:
            dh.create_report()
        elif choice_action == 3:
            dh.send_letters()
        elif choice_action == 4:
            print('Quit current task!')
            break


if __name__ == '__main__':
    main()
