"""
Author: Alyssa Hong
Date: 1/12/2019
Update:
Lesson10 Assignments > Mailroom, Object Oriented Mailroom
"""

#!/usr/bin/env python3

import os


class Donor:
    def __init__(self, first_name, last_name, donations = None):
        self.first = first_name
        self.last = last_name
        self.donations = donations

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def add_donations(self, new_donations):
        return self.donations.append(new_donations)

    def total_donations(self):
        return sum(self.donations)

    def multi_donations(self, factor, donations_list):
        return list(map(lambda x: x * factor, donations_list))

    def min_max_donations(self, min_donations, max_donations):
        return list(filter(lambda x: min_donations < x < max_donations, self.donations))

    def donations_less_than_value(self, value):
        return list(filter(lambda x: x < value, self.donations))

    def donations_more_than_value(self, value):
        return list(filter(lambda x: x > value, self.donations))

def donor_input():
    return input("Type the donor's name: ")

def donations_input():
    return float(input("Type your donations: "))

def donate_times_input():
    return int(input("How many times will you challenge to donate?: "))

def min_donations_input():
    return float(input("How much is the minimum donations?: "))

def max_donations_input():
    return float(input("How much is the maximum donations?: "))


class DornorList:
    def __init__(self, donors = None):
        if donors is None:
            self.donors = []
        else:
            self.donors = donors

    def new_donor(self, donor):
        self.donors.append(donor)

    def check_donor_list(self):
        return [donor.full_name for donor in self.donors]

    def send_thanks(self):
        donor_name = None
        while not donor_name:
            donor_name = donor_input()
            if donor_name.lower() == "list":
                print(self.check_donor_list())
        donations = None
        while not donations:
            try:
                donations = donations_input()
            except ValueError:
                print("Please enter a number: ")

        if donor_name not in self.check_donor_list():
            try:
                first, last = donor_name.split(" ")
                self.new_donor(Donor(first, last, [donations]))
            except ValueError:
                print("Please type the full name")
        else:
            for donor in self.donors:
                if donor.full_name == donor_name:
                    donor.add_donations(donations)

        print('\n' + 'Dear {:s}, thank you for your ${:.2f} donations!'.format(donor_name, donations) + '\n')

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
                        'Thank you for your donations of ${:.2f}.'.format(sum(donor.donations))+
                        '\n' + '\t'*1 + 'It will be put to very good use.\n'+'\t'*5 +'Sincerely,\n' +
                        '\t'*5 +'-The Team')

    def challenge(self):
        factor = donate_times_input()
        min_donations = min_donations_input()
        max_donations = max_donations_input()
        for donor in self.donors:
            new_dh.append(Donor(donor.full_name, donor.multi_donations(factor, donor.min_max_donations(min_donations, max_donations))))
            print("{}:{}".format(donor.full_name, donor.multi_donations(factor, donor.min_max_donations(min_donations, max_donations))))

    def projections(self):
        for donor in self.donors:
            d_double = donor.donations_less_than_value(100)*2
            d_triple = donor.donations_more_than_value(50)*3
            print("{}'s current donations is {}".format(donor.full_name, donor.donations))
            print("(a) what {}'s total contribution would come to in dollars if they were to double contributions under $100: {}".format(donor.full_name, sum(d_double)))
            print("(b) what {}'s total contribution would come to in dollars if they were to triple contributions under $50: {}".format(donor.full_name, sum(d_triple)))


list_col = ['Donor Name','Total Given','Num Gifts','Average Gift']
d1 = Donor('Fred', 'Lillywhite', [70,450])
d2 = Donor('Alex', 'Kim', [300,300,100])
d3 = Donor('Henry', 'Ford', [50])
d4 = Donor('Alyssa', 'Hong', [120,300,400])
d5 = Donor('Leo', 'Jeon', [107,53])

dh = DornorList([d1, d2, d3, d4, d5])
new_dh = []

def main():
    while True:
        print('\n'
            'Choose an action\n'
            '1 - Send a Thank you\n'
            '2 - Create a Report\n'
            '3 - Send letters to everyone\n'
            '4 - Challenge the donors\n'
            '5 - Donations Projections \n'
            '6 - Quit')

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
            dh.challenge()
        elif choice_action == 5:
            dh.projections()
        elif choice_action == 6:
            print('Quit current task!')
            break


if __name__ == '__main__':
    main()
