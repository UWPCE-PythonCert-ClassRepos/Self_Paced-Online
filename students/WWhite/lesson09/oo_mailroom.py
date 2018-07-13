#!/usr/bin/env python3

# -------------------------------------#
# Desc: Object Oriented Mailroom
# Dev: Will White
# Date: 7/2/2018
# ChangeLog: (When,Who,What)
# -------------------------------------#
import math


class Donor(object):
    def __init__(self, name="", donation=0):
        self.name = name
        self.total_donation = 0
        self.donationCount = 0

        self.donation = donation

    @property
    def name(self):
        return self._name

    @property
    def donation(self):
        return self._donation

    @name.setter
    def name(self, name):
        self._name = name

    @donation.setter
    def donation(self, donation):
        self._donation = donation
        self.total_donation += donation
        self.donationCount += 1

    def print_letter(self):
        dict_donor_info = {'name': self.name, 'donation': self.donation}
        str_letter = '''
    Dear {name},

    Thank you for your donation of {donation:.2f}, it is very much appreciated.

    Kind Regards,
    Your Favorite Local Charity
    '''.format(**dict_donor_info)  # Thank you email with formatting to include donor name and amount
        return str_letter


class DonorCollection(object):
    def __init__(self):
        self.donors = []

    def add_donor(self, name, amount):
        newDonor = Donor(name, amount)
        self.donors.append(newDonor)

    def add_donation_amount(self, donor_name, donation_amount):
        for donor in self.donors:
            if donor.name == donor_name:
                donor.donation = donation_amount
                print(donor.print_letter())
                break
        else:
            self.add_donor(donor_name, donation_amount)
            print(self.donors[-1].print_letter())

    def print_donor_names(self):
        for donor in self.donors:
            print(donor.name)

    def sort_list(self):
        dict_to_list = []
        for donor in self.donors:
            dict_to_list.append([donor.name, donor.total_donation, donor.donationCount])
        sorted_list = sorted(dict_to_list, key=lambda x: x[1], reverse=True)
        return sorted_list

    def create_a_report(self):  # Function to create a report of all the current donor info
        sorted_list = self.sort_list()
        title_header = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
        print('{:<10}{:>20}{:>20}{:>20}'.format(*title_header))
        print('----------------------------------------------------------------------')

        for i in sorted_list:
            donor_count = i[2]
            print('{:<10}{:>20.2f}{:>20}{:>20.2f}'.format(i[0].title(), i[1], donor_count, (i[1] / donor_count)))

    def send_letters(self):
        for donor in self.donors:
            with open("{}.txt".format(donor.name), 'w') as txt_file:
                txt_file.write(donor.print_letter())


donor_list = DonorCollection()
donor_list.add_donor("bill gates", 25000.00)
donor_list.add_donor("monet holt", 50000.00)
donor_list.add_donor("jeff bezos", 123500.09)
donor_list.add_donor("john wick", 120000.00)
donor_list.add_donor("john snow", 10.56)


def prompt_for_number_in_range(prompt_text, min_limit, max_limit):

    min_limit = float(min_limit)
    max_limit = float(max_limit)

    while True:
        try:
            return_number = input(prompt_text)
            return_number = float(return_number)

            if min_limit <= return_number <= max_limit:
                break
            else:
                print("Number out of range.")
        except ValueError:
            print("Input could not be converted to a float")

    return return_number


def menu_options():  # Function to run the menu options
    user_input = prompt_for_number_in_range(
        'Please enter a number from the following options:\n\n' +
        '[1] Send a Thank You\n' +
        '[2] Create a Report\n' +
        '[3] Send Letters to Everyone\n' +
        '[4] Quit the Program\n', 1, 4)
    return user_input  # Function returns user_input


def prompt_for_name():  # Function to prompt the user for a name
    donor_name = input("Please input the donor's name, or type 'list' to see a list of donor names: \n")
    while donor_name == 'list':  # If user inputs "list", program will print a list of current donors
        donor_list.print_donor_names()
        donor_name = input("\nPlease input the donor's name: \n").lower()
    return donor_name  # Function returns the donor's name


def add_donation():  # Function for the user to add a donation
    donor_name = prompt_for_name()
    donation_amount = prompt_for_number_in_range("Please input the donation amount: ", 0, math.inf)
    donor_list.add_donation_amount(donor_name, donation_amount)


switch_func_dict = {
    1: add_donation,
    2: donor_list.create_a_report,
    3: donor_list.send_letters
}

if __name__ == "__main__":  # If this is the main file, run the below

    while True:
        option_selected = menu_options()  # Run the menu options function and save the input
        option_selected = int(option_selected)
        if option_selected < 4:  # If user entered 1, get the name and run the add_donation function
            try:
                switch_func_dict.get(option_selected)()
            except KeyError:
                print("Option doesn't exist.")
        else:  # If the user enters anything else, quit the program
            break

    print("Thank you, the program will now exit")
    raise SystemExit  # Exit the progra
