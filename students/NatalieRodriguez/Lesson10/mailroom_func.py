#!/usr/bin/env python3

#Natalie Rodriguez
#Lesson 10: Mailroom with Functional Programming
#May 20, 2018

import sys

class Donor:


    def __init__(self, name, donations=None):

        self.name = name
        if donations is None:
            self.donations = []
        else:
            self.donations = donations

    def add_donation(self, amount):
        try:
            self.donations.append(int(amount))
        except ValueError:
            print("Please enter a number!")

    def donation_amount(self):
        return len(self.donations)

    def total_donation(self):
        try:
            return sum(self.donations)
        except TypeError:
            return self.donations

    def donation_avg(self):
        try:
            return self.total_donation()/ self.donation_amount()
        except TypeError:
            return self.donations


class DonorHistory:

    def __init__(self, donors=None):
        self.donor_list = donors

    def donor_histlist(self):

        donor_names = []
        for donor in self.donor_list:
            donor_names.append(donor.name)
        return donor_names

    def thank_you(self, new_donor, amount):

        if new_donor in self.donor_list:
            try:
                donor_list[new_donor].add_donation(amount)
                print('Thank you {}, for your generous donation of ${:.2f}.'.format(new_donor, amount))
            except ValueError:
                print("Please enter a valid amount.")
        else:
            new_donor_object = Donor(new_donor, [amount])
            self.donor_list.append(new_donor_object)
            print('Thank you {}, for your generous donation of ${:.2f}.'.format(new_donor, amount))

    def donor_report(self):

        print('Here is a list of donors and contributions')
        report = []
        report.append(
            '|{:<20}|{:<20}|{:<20}|{:<20}|'.format('    Donor Name', '   Total Donation', '  No. of Donations',
                                                   '  Average Donation'))
        for donor in self.donor_list:
            report.append(
                '|{:<20}|{:>20}|{:>20}|{:>20}|'.format(donor.name, donor.total_donation(), donor.donation_amount(),
                                                       donor.donation_avg()))
        return '\n'.join(report)

    def print_donors(self):
        print(self.donor_report())


    def write_files(self):

        for donor_data in self.donor_list:
            filename = donor_data.name.replace(" ", "_") + ".txt"
            total_donation = donor_data.total_donation()
            letter = ('Thank you {}, for you generous donations of {:.2f}!'.format(donor_data.name, total_donation))
            with open(filename, 'w') as letter_file:
                letter_file.write(letter)
            print(f"{donor_data.name}'s thank you has been saved at: " + filename)

    def challenge(self, factor, min=None, max=None):

        challenge = []
        for name in self.donor_list:
            challenge.append(Donor(name.name, self.map_filter(factor, name.donations, min, max)))
        return challenge

    def map_filter(self, factor, money, min=None, max=None):


        if min and max:
            if min > max:
                raise ValueError('Maximum must be greater than minimum amount.')
            else:
                for donor in money:
                    return list(map(lambda x: x * factor, filter(lambda y: min <= y <= max, money)))


        elif min:
            for donor in money:
                return list(map(lambda x: x * factor, filter(lambda y: y >= min, money)))


        elif max:
            for donor in money:
                return list(map(lambda x: x * factor, filter(lambda y: y <= max, money)))


        else:
            for donor in money:
                return list(map(lambda x: x * factor, money))


    def make_newlist(self, factor, min=None, max=None):


        phil_donation = self.challenge(factor, min, max)
        return DonorHistory(phil_donation)

    def donation_projected(self, factor, min=None, max=None):
        projected = []
        for name in self.donor_list:
            projected.append(self.map_filter(factor, name.donations, min, max))
        return sum(list(sum(projected, [])))


def add_phil():

    print('Please enter the minimum and maximum amounts of the donations you would like to match:')
    min = float(input('Minimum:'))
    max = float(input('Maximum:'))
    factor = float(input('Please enter the factor by which you want to multiply your donation:'))
    don_mult = mailroom.make_newlist(factor, min, max)
    don_mult.print_donors()
    return don_mult

def projected():

    print('Please enter the minimum and maximum values of the donations you wish to match:')
    min = float(input('Minimum donation:'))
    max = float(input('Maximum donation:'))
    factor = float(input('Please enter the factor you wish to multiply these donations by'))
    proj_don = mailroom.donation_projected(factor, min, max)
    print(f"{proj_don} is the amount of the projected donation.")

def create_thank_you():

    print('Please enter the donor name or enter "list" for a list of current donors.)\n '
          'Enter "quit" to return to the Donor Dashboard.')
    new_donor = input(':')
    if new_donor.lower() == 'list':
        mailroom.donor_histlist()
    elif new_donor.lower() == 'quit':
        quit_dashboard()
    else:
        amount = float(input('Please enter the donation amount:'))
        mailroom.thank_you(new_donor, amount)

def menu_selection(prompt, find_dict):

    while True:
        try:
            response = input(prompt)
            find_dict[response]()
        except KeyError:
            print('Please enter a selection from the dashboard.')

def quit_dashboard():
    sys.exit("Exiting the Nature Conservancy Donor Dashboard. Goodbye!")

if __name__ == '__main__':

    Luke = Donor('Luke Rodriguez',[5512.75, 3250.50, 42.50])
    River = Donor('River Tails',[63.00, 1200.00, 300.00, 450.00, 4000.00])
    Virgil = Donor('Virgil Ferdinand',[350.00, 5000.00])
    Jokib = Donor('Joseph Kibson',[3498.00, 5.50])
    mailroom = DonorHistory([Luke, River, Virgil, Jokib])


    donor_dashboard = ("\nWelcome to the Nature Conservancy Donor Dashboard!\n"
                      "Please make a numerical selection.\n"
                      "1.) Send a thank you note.\n"
                      "2.) Create a Report.\n"
                      "3.) Send thank you notes to all donors.\n"
                      "4.) Match an existing donation.\n"
                      "5.) Create a projected donation amount. \n"
                      "6.) Quit(Enter 'quit')\n")

    dashboard_dict = {'1': create_thank_you,
                    '2': mailroom.print_donors,
                    '3': mailroom.write_files,
                    '4': add_phil,
                    '5': projected,
                    '6': quit_dashboard,
                    'quit': quit_dashboard,
                    'Quit': quit_dashboard}


    menu_selection(donor_dashboard, dashboard_dict)


def challenge(factor):
    challenge = []
    for donor in mailroom.donor_list:
        challenge.append(donor.total_donation())
    return list(map(lambda x: x* factor, challenge))




def make_dlist(factor, min = None, max = None):
    donor_names = mailroom.donor_histlist()
    phil_donation = challenge(factor, min, max)
    donors_new = list(zip(donor_names, phil_donation))
    for name in donors_new:
        new_list = []
        name = Donor(name[0], name[1])
        new_list.append(name)
    return DonorHistory(new_list)