#!/usr/bin/env python3
import sys
from collections import defaultdict

class Donor:

    '''Donor class with attributes name and donations'''
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

    def number_donations(self):
        return len(self.donations)

    def total_donation(self):
        try:
            return sum(self.donations)
        except TypeError:
            return self.donations

    def avg_donation(self):
        try:
            return self.total_donation()/ self.number_donations()
        except TypeError:
            return self.donations


class Roster:

    def __init__(self, donors=None):
        self.donor_list = donors

    def donor_roster(self):

        ''' Returns a list of the names from the donor objects'''

        donor_names = []
        for donor in self.donor_list:
            donor_names.append(donor.name)
        return donor_names

    def thank_you(self, new_donor, amount):

        '''Adds a new donation, and prints a thank you note for the donation'''

        if new_donor in self.donor_list:
            try:
                donor_list[new_donor].add_donation(amount)
                print('Thank you {} for your generous donation of ${:.2f}'.format(new_donor, amount))
            except ValueError:
                print("Please enter a round number!")
        else:
            new_donor_object = Donor(new_donor, [amount])
            self.donor_list.append(new_donor_object)
            print('Thank you {} for your generous donation of ${:.2f}'.format(new_donor, amount))

    def donor_report(self):

        '''Outputs a string that is a table of the donors and contributions'''

        print('Here is a list of donors and contributions')
        report = []
        report.append('|{:<20}|{:<20}|{:<20}|{:<20}|'.format('Name', 'Total', 'Donations', 'Average'))
        for donor in self.donor_list:
           report.append('|{:<20}|{:>20}|{:>20}|{:>20}|'.format(donor.name, donor.total_donation(), donor.number_donations(), donor.avg_donation()))
        return '\n'.join(report)

    def print_donors(self):
        print(self.donor_report())


    def batch_file(self):

        '''Creates a text file with a thank you message for each of the donors in the donor list'''

        for donor_data in self.donor_list:
            filename = donor_data.name.replace(" ", "_") + ".txt"
            total_donation = donor_data.total_donation()
            letter = ('Thank you {} for you generous contributions totalling {:.2f}!'.format(donor_data.name, total_donation))
            with open(filename, 'w') as letter_file:
                letter_file.write(letter)
            print(f"{donor_data.name}'s letter has been saved to " + filename)

    def challenge(self, factor, min=None, max=None):

        '''Sends the current Donors through the map and filter function,
           and returns a list of modified Donors'''

        challenge = []
        for name in self.donor_list:
            challenge.append(Donor(name.name, self.map_filter(factor, name.donations, min, max)))
        return challenge

    def map_filter(self, factor, money, min=None, max=None):

        '''Takes a map factor, a list of donations, and optional min and max donations,
            and returns a list of modified donations'''

        if min and max:
            if min > max:
                raise ValueError('Max must be greater than min')
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


    def make_roster(self, factor, min=None, max=None):

        ''' Uses the Challenge function output to create a new Roster object'''

        philanthropist_donation = self.challenge(factor, min, max)
        return Roster(philanthropist_donation)

    def donation_projection(self, factor, min=None, max=None):
        projection = []
        for name in self.donor_list:
            projection.append(self.map_filter(factor, name.donations, min, max))
        return sum(list(sum(projection, [])))


def add_philanthropist():

    '''User input for matching donations'''

    print('Please enter the minimum and maximum values of the donations you wish to match:')
    min = float(input('Minimum >'))
    max = float(input('Maximum >'))
    factor = float(input('Please enter the factor you wish to multiply these donations by'))
    big_money = mailroom.make_roster(factor, min, max)
    big_money.print_donors()
    return big_money

def projection():

    '''User input for projecting donations'''

    print('Please enter the minimum and maximum values of the donations you wish to match:')
    min = float(input('Minimum >'))
    max = float(input('Maximum >'))
    factor = float(input('Please enter the factor you wish to multiply these donations by'))
    fake_money = mailroom.donation_projection(factor, min, max)
    print(f"{fake_money} is the total donation projected")

def create_thank_you():

    '''User input for adding donations and printing a thank you letter'''

    print('Please enter the donor name\n (Type "list" for a list of current donor names)\n '
          'Press "q" to return to console')
    new_donor = input(':')
    if new_donor.lower() == 'list':
        mailroom.donor_roster()
    elif new_donor.lower() == 'q':
        quit_console()
    else:
        amount = float(input('Please enter the donation amount:'))
        mailroom.thank_you(new_donor, amount)

def menu_selection(prompt, dispatch_dict):
    '''Creates a menu that accepts user input and then selects a function based on that input'''
    while True:
        try:
            response = input(prompt)
            dispatch_dict[response]()
        except KeyError:
            print('Please enter a valid selection from the menu')

def quit_console():
    sys.exit("Exiting the program")

if __name__ == '__main__':

    Andy = Donor('Andy', [10.00])
    Bill = Donor('Bill', [15.00, 25.00])
    Chuck = Donor('Chuck', [20.00, 30.00, 40.00])
    mailroom = Roster([Andy, Bill, Chuck])


    console_prompt = ("\nWelcome to the Donor Tracking System\n"
                      "Please press a number to make a selection\n"
                      "1.) Send a thank you note\n"
                      "2.) Create a Report\n"
                      "3.) Send letters to everyone!\n"
                      "4.) Match donations!\n"
                      "5.) Project a matching donation amount\n"
                      "6.) Quit(press 'q')\n")

    console_dict = {'1': create_thank_you,
                    '2': mailroom.print_donors,
                    '3': mailroom.batch_file,
                    '4': add_philanthropist,
                    '5': projection,
                    '6': quit_console,
                    'q': quit_console,
                    'Q': quit_console}


    menu_selection(console_prompt, console_dict)

# def challenge(factor):
#    challenge = []
#    for donor in mailroom.donor_list:
#        challenge.append(donor.total_donation())
#    return list(map(lambda x: x* factor, challenge))


# def make_roster(factor, min = None, max = None):
#    donor_names = mailroom.donor_roster()
#    philanthropist_donation = challenge(factor, min, max)
#    donors_new = list(zip(donor_names, philanthropist_donation))
#    for name in donors_new:
#        new_list = []
#        name = Donor(name[0], name[1])
#        new_list.append(name)
#    return Roster(new_list)
