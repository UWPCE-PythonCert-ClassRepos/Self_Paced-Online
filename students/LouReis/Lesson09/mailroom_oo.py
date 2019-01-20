#!/usr/bin/env python3.7
# mailroom_oo.py
# Coded by LouReis
# Lesson09

"""
Refactor the following code to use classes.

Write a small command-line script called mailroom.py.
It should have a data structure that holds a list of your donors and a history
of the amounts they have donated. This structure should be populated at first
with at least five donors, with between 1 and 3 donations each.
The script should prompt the user (you) to choose from a menu of 3 actions:
“Send a Thank You”, “Create a Report” or “quit”)

Report should look like the following:
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
Joe Donor                  $  653784.49           2  $   326892.24
John Rich                  $   16396.10           3  $     5465.37
Sally Neighbor             $     877.33           1  $      877.33
Mack Jack                  $     708.42           3  $      236.14

"""

# The below snippet will display the instances in memory.
"""
 import gc
 for obj in gc.get_objects():
     if isinstance(obj, Donor):
         print (obj.name, obj.donations)
"""

from functools import total_ordering
import sys
import math
from textwrap import dedent

donations = {}

# Utility so we have data to test with, etc.
def enter_sample_data():
    """
    Returns a list of donor objects to use as sample data to populate the DB
    """
    return [Donor("Robin Hood", [50000, 50000, 50000]),
            Donor("Tycoon Reis", [25000000, 25000000, 25000000]),
            Donor("Howie Long", [100000]),
            Donor("Joe Neighbor", [25, 25]),
            Donor("Rick Retiree", [0.50, 0.50]),
            ]

# Below is the main menu function that continues prompting until quit.
def main_menu(main_prompt,menu_options_dict):
    while True:
        try:
            response = input(main_prompt)
            menu_options_dict[response]()
        except KeyError:
            print("\n\n----------------PLEASE TRY AGAIN! PLEASE ENTER A VALID VALUE!----------------\n\n")
            print("\n\n----------------PLEASE TRY AGAIN! PLEASE ENTER A VALID VALUE!----------------\n\n")
            print("\n\n----------------PLEASE TRY AGAIN! PLEASE ENTER A VALID VALUE!----------------\n\n")

class Donor():
    """
    A class that holds the information about a single donor.
    """

    def __init__(self, name, donations=None):
        """
        Create a new Donor object
        name: the full name of the donor
        donations=None: iterable of past donations
        """

        self.name = name
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def avg_donation(self):
        return self.total_donations / len(self.donations)

    def add_donation(self, amount):
        """
        add a new donation
        """
        amount = float(amount)
        self.donations.append(amount)

class DonorDB():
    """
    Contains entire database of donors and data associated with them.
    """

    def __init__(self, donors=None):
        """
        Initialize a new donor database
        :param donors=None: iterable of Donor objects
        """
        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {d.name: d for d in donors}

    @property
    def donors(self):
        """
        an iterable of all the donors
        """
        return self.donor_data.values()

    def list_donors(self):
        """
        creates a list of the donors as a string, so they can be printed
        Not calling print from here makes it more flexible and easier to
        test
        """
        listing = ["Donor list:"]
        for donor in self.donors:
            listing.append(donor.name)
        return "\n".join(listing)

    def find_donor(self, name):
        """
        find a donor in the donor db
        :param: the name of the donor
        :returns: The donor data structure -- None if not in the self.donor_data
        """
        return self.donor_data.get(Donor.name(name))

    def add_donor(self, name):
        """
        Add a new donor to the donor db
        :param: the name of the donor
        :returns: the new Donor data structure
        """
        donor = Donor(name)
        self.donor_data[donor.name] = donor
        return donor

    def gen_letter(self, donor):
        """
        Generate a thank you letter for the donor
        :param: donor tuple
        :returns: string with letter
        note: This doesn't actually write to a file -- that's a separate
              function. This makes it more flexible and easier to test.
        """
        return dedent('''Dear {0:s},
              Thank you for your very kind donation of ${1:.2f}.
              It will be put to very good use.
                             Sincerely,
                                -The Team
              '''.format(donor.name)
                      )

    def get_report(self):
        for donor_obj in self.donor_data.values():
            print ('{:25} ${:>15,.2f} {:>15} ${:>15,.2f}'.format(donor_obj.name, donor_obj.total_donations, donor_obj.num_donations, donor_obj.avg_donation))

# create a DB with the sample data which is also contained in donations dict
donations = DonorDB(enter_sample_data())

# This function uses the Donor Class for values to sort by.
def donation_report():
    # DonorCollection.get_report(donations)
    print('\nYou Chose Option 1\n\n')
    print('DONATION SUMMARY REPORT\n\n')
    print('{:25} | {:^13} | {:^13} |   {:>13}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('---------------------------------------------------------------------------')
    print()
    DonorDB.get_report(donations)

# This Option generates a thank you letter for a new donation and prints to the screen.
def thanks_letter():
    print('\nYou Chose Option 2\n\n')
    print('Create a Thank You Letter\n\n')
    donor = 'L'
    while donor == 'L':
        donor=input("Enter the full name of the Donor (Type 'L' for a donor list):")
        if donor == 'L':
            print("\n")
            for key in sorted(donations):
                print(key)
            print("\n")
    donation = 0
    if donor in Donor:
        print("You have entered an existing donor:", donor)
        try:
            donation = float(input("Please enter the donation amount '0.00':"))
        except ValueError:
            print("\n\n----------You have entered an invalid value, returning to Main Menu----------\n\n")
            main_menu(main_prompt,menu_options_dict)
        temp = Donor(donor)
        temp.add_donation(donation)
    else:
        print("You have entered a new donor:", donor)
        try:
            donation = float(input("Please enter the donation amount '0.00':"))
        except ValueError:
            print("\n\n----------You have entered an invalid value, returning to Main Menu----------\n\n")
            return
        DonorDB.add_donor(donor)
        temp = Donor(donor)
    print_letter(donor, donation)

# This Option generates a letter saved in a text file for each donor.
def thanks_letter_all():
    print('\nYou Chose Option 3\n\n')
    print('Send a Thank You Letter to Everyone.\n')
    for item in (donations):
        filename = ""
        filename = item.replace(" ","") + '.txt'
        print(filename)
        with open(filename, 'w') as f:
            for i in range(1):
                f.write(f"\n\nSubject: Donation\n\nDear {item},\n\nThank you for your donation, it will be used to help meet our goals.")
                f.write("\nWe will welcome any future donations and appreciate your support.")
                f.write("\n\n\nSincerely,\n\nMDTS Staff\n\n\n")
    print("\n\nA Letter has been created for each donor and stored in a text file.\n\n")

def quit():
    import sys
    print('\nYou Chose Option 4\n\n')
    print('Thanks for using MDTS, Goodbye!\n')
    sys.exit()

# Below is the dict defining the menu options.
menu_options_dict = {
    "1": donation_report,
    "2": thanks_letter,
    "3": thanks_letter_all,
    "4": quit,
}

# The following function prints out an email when the user enters a donation.
def print_letter(donor, amount):
    message = "We will welcome any future donations and appreciate your support."
    letter_dict = {'donor_name': donor, 'amount_donated': amount}
    print('\n\nSubject: Donation\n\nDear {},\n\nThank you for your ${:,.2f} donation, it will be used to help meet our goals.'.format(donor, amount))
    print(message,'\n\nSincerely,\n\nMDTS Staff\n\n\n')

main_prompt = ("\nMailroom Donation Tracking System - MDTS\n\nMAIN MENU\n\n""Please choose from the following Menu Options:\n\n"
"1 - Generate A Donation Report\n\n""2 - Create a Thank You Note\n\n""3 - Send a Thank You Letter to Everyone\n\n""4 - Quit Program\n\n""Enter Menu Option: ")

# Put your main interaction into an if __name__ == '__main__' block.
if __name__ == '__main__':
    main_menu(main_prompt,menu_options_dict)
