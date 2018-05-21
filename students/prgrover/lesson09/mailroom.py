#!/usr/bin/env python3

import textwrap
import sys


class Donor:
    '''
    Base class that encapsulates all donor information per donor.

    For example, donor name, donation amount, total donation amount, numeber of donations, etc.
    '''

    def __init__(self, donor_name):
        self.donor_name = donor_name
        self.donations = []

    @property
    def donation_total(self):
        return sum(self.donations)

    @property
    def donation_number(self):
        return len(self.donations)

    @property
    def donation_average(self):
        return self.donation_total / self.donation_number

    def add_donation(self, donation_amount):
        self.donations.append(donation_amount)


class DonorDirectory:
    '''
    Encapsulates "database type" functions (e.g. insert, query, list, etc.)
    '''

    def __init__(self):
        self.donor_list = []

    def add_donor(self, donor_name, donation_amount):
        donor = self.find_donor(donor_name)
        if donor:
            donor.add_donation(donation_amount)
        else:
            donor = Donor(donor_name)
            donor.add_donation(donation_amount)
            self.donor_list.append(donor)

    def find_donor(self, donor_name):
        for donor in self.donor_list:
            if donor.donor_name == donor_name:
                return donor

    def list_donors(self):
        output = '\n'.join([donor.donor_name for donor in self.donor_list])
        if len(output) == 0:
            output = "\nCurrently there are no donor records."
        return output

    def create_report(self):
        donor_name = [donor.donor_name for donor in self.donor_list]
        total_given = [donor.donation_total for donor in self.donor_list]
        num_donations = [donor.donation_number for donor in self.donor_list]
        average_donation = [donor.donation_average for donor in self.donor_list]
        sorted_donor_list = sorted(zip(donor_name, total_given, num_donations, average_donation), key=lambda x: int(x[1]), reverse=True)

        print("{:30s} | {:11s} | {:9s} | {:12s}".format("Donor Name", "Total Given", "Num Donations", "Average Donation"))
        print("-" * 79)

        for index in range(len(sorted_donor_list)):
            row = sorted_donor_list[index]
            print("{:30s}  ${:11.2f}   {:12d}    ${:12.2f}".format(*row))


    def send_mail(self, donor_name, donation_amount):
        email = textwrap.dedent('''
            Dear {:s},

            Thank you for your very kind donation of ${:.2f}.
            It will be put to very good use.

            Sincerely,
            -Hogwarts School of Witchcraft and Wizardry''')

        return email.format(donor_name, donation_amount)

    def create_mail_files(self):
        for donor in self.donor_list:
            filename = donor.donor_name + ".txt"
            letter = self.send_mail(donor.donor_name, donor.donations[-1]) 
            try:
                with open(filename, 'w') as outfile:
                    outfile.write(letter)
            except IOError:
                print("Unable to open file or write file.")


'''
The functions below provide user prompts for donor information.
'''

ddir = DonorDirectory()

def get_donor():
    donor_name = input("Please enter the full name of a donor. You can also enter 'list' to see all current donors or 'e' to exit: ")
    if donor_name == "e":
        menu_selection(main_prompt, main_dispatch)
    elif donor_name == "list":
        print(ddir.list_donors())
        menu_selection(main_prompt, main_dispatch)
    else:
        return donor_name

def get_donation():
    while True:
        donation_amount = input("Please enter the donation amount or 'e' to exit: ")
        if donation_amount == "e":
            menu_selection(main_prompt, main_dispatch)
        else:
            try:
                donation_amount = float(donation_amount)
            except ValueError:
                print("Invalid donation amount. Please try again.\n")
            else:
                return donation_amount

def abort():
    print("Bye!")
    sys.exit()

def send_thankyou():
    donor_name = get_donor()
    donation_amount = get_donation()
    ddir.add_donor(donor_name, donation_amount)
    print(ddir.send_mail(donor_name, donation_amount))


"""
The funtions below produce the main menu
"""

def menu_selection(prompt, menu_dict):
    while True:
        try:
            response = input(prompt)
            menu_dict[response]()
        except KeyError:
            print("Please select a valid selection from the menu.")


main_prompt = ("""\nChoose an action:
      1 - Send a Thank You
      2 - Create a Report
      3 - Send letters to everyone
      4 - Quit
      : """)

main_dispatch = {"1": send_thankyou,
                 "2": ddir.create_report,
                 "3": ddir.create_mail_files,
                 "4": abort,
                 }

if __name__ == '__main__': 
    menu_selection(main_prompt, main_dispatch)
