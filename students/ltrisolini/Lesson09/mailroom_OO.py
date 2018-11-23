#!/usr/bin/env python3
import sys
from collections import defaultdict

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

    def thank_you(self):
        '''Accepts user input, and then adds donors / donations to the donor dictionary.
        It also prints a thank you message for the latest donation'''
        print('Please enter the donor name\n (Type "list" for a list of current donor names)\n '
            'Press "q" to return to console')
        new_donor = input(':')

        if new_donor.lower() == 'list':
            donor_names = []
            for donor in self.donor_list:
                donor_names.append(donor.name)
            print(donor_names)

        elif new_donor.lower() == 'q':
            return

        else:
            if new_donor in self.donor_list:
                try:
                    amount = float(input('Please enter the donation amount:'))
                    donor_list[new_donor].add_donation(amount)
                    print('Thank you {} for your generous donation of ${:.2f}'.format(new_donor, amount))
                except ValueError:
                    print("Please enter a round number!")
            else:
                amount = float(input('Please enter the donation amount for the new donor:'))
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
        '''Creates a text file with a thank you message for each of the donors in the dictionary'''
        for donor_data in self.donor_list:
            filename = donor_data.name.replace(" ", "_") + ".txt"
            total_donation = donor_data.total_donation()
            letter = ('Thank you {} for you generous contributions totalling {:.2f}!'.format(donor_data.name, total_donation))
            with open(filename, 'w') as file:
                file.write(letter)
            print(f"{donor_data.name}'s letter has been saved to " + filename)


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
                      "4.) Quit(press 'q')\n")

    console_dict = {'1': mailroom.thank_you,
                    '2': mailroom.print_donors,
                    '3': mailroom.batch_file,
                    '4': quit_console,
                    'q': quit_console,
                    'Q': quit_console}

    menu_selection(console_prompt, console_dict)