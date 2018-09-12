'''
Shin Tran
Python 210
Lesson 10 Assignment
'''

#!/usr/bin/env python3
# Implementing the mailroom program using object oriented programming

import copy
import sys
from functools import reduce

class Donor:

    def __init__(self, f_name, l_name, donation = None):
        self._f_name = f_name
        self._l_name = l_name
        if donation is None:
            self._donations = []
        else:
            self._donations = donation

    def f_name(self):
        return self._f_name

    def l_name(self):
        return self._l_name

    @property
    def full_name(self):
        return self._f_name + " " + self._l_name
    
    @property
    def get_donation_count(self):
        return len(self._donations)

    @property
    def get_donation_total(self):
        return sum(self._donations)

    @property
    def get_avg_donation(self):
        if len(self._donations) == 0:
            return 0
        else:
            return round(sum(self._donations) / len(self._donations), 2)

    def add_donation(self, value):
        self._donations.append(value)

    def get_email_text(self, current_donation):
        """Prints a thank you email to a donator
        Donor name and amount is passed in as a parameter"""
        return "Dear {:s} {:s},\n\
            Thank you for the generous donation of ${:,.2f}.\n\
            Sincerely,\n\
            Your Local Charity".format(*current_donation)

    def get_letter_text(self):
        """Returns a message of the donor name and donation total"""
        message = "Dear {:s},\n\
        Thank you for donating ${:,.2f}.\n\
        Sincerely,\n\
        Your Local Charity"
        return message.format(self.full_name, self.get_donation_total)

class DonorCollection:

    def __init__(self, donors):
        self.donor_dict = donors

    def generate_name_list(self):
        """Creates a list of all the distinct donors, returns a list
        helper method for print_names"""
        return list(self.donor_dict)

    def print_names(self):
        """Prints out all the names in the name list,
        references generate_name_list"""
        for name in self.generate_name_list():
            print(name)

    def send_thanks(self):
        """Prompts the user to type a name of a donor, enter a donation amount,
        prints an email thanking the donor
        If the user types exit, it would return to the main prompt"""
        temp_list = []
        donor_name = get_new_donor_name()
        if (donor_name != 'exit'):
            temp_list = donor_name.split()
            donation_amt = get_new_donor_amount()
            if (donation_amt != 'exit'):
                temp_list.append(float(donation_amt))
                if donor_name in self.donor_dict:
                    self.donor_dict[donor_name].add_donation(temp_list[2])
                else:
                    self.donor_dict[donor_name] = Donor(temp_list[0], temp_list[1], [temp_list[2]])
                print(self.donor_dict[donor_name].get_email_text(temp_list))

    def send_letters(self):
        """Goes through all the previous donators, gets their total donated,
        sends a thank you letter that is output on a .txt file"""
        for name, vals in self.donor_dict.items():
            message = vals.get_letter_text()
            with open(name + ".txt",'w') as output:
                output.write(message)
        print("Letters have been generated.")

    def generate_report(self):
        """Generates a report of all the previous donators
        Report includes name, total donated, count of donations, average gift
        Report is also formatted with a certain spacing
        returns the report as a string"""
        donation_total = [[k, v.get_donation_total, v.get_donation_count, v.get_avg_donation] for k, v in self.donor_dict.items()]
        donation_total.sort(key=lambda l: l[1], reverse = True)
        s1 = "Donor Name          |   Total Given  |  Num Gifts |  Average Gift\n"
        s2 = "-----------------------------------------------------------------\n"
        final_string = s1 + s2
        for z in range(0, len(donation_total)):
            s3 = '{:20} ${:13,.2f}{:14}  ${:13,.2f}\n'.format(*donation_total[z])
            final_string += s3
        return final_string

    def print_report(self):
        """Prints a report of all the previous donators references generate_report"""
        print(self.generate_report())

    def challenge(self):
        """Prompts the user whether they want to get an estimate or match,
        enter a number to multiply all the donations by an amount,
        enter a min and max threshold on the donation amount to filter"""
        projection = get_projection()
        factor = get_multip_factor()
        lower = get_min_donation()
        upper = get_max_donation()
        temp_sum = 0
        for donor, val in self.donor_dict.items():
            filtered_list = list(filter(lambda x: lower <= x <= upper, val._donations))
            challenge_list = list(map(lambda x: x * factor, filtered_list))
            if projection == '1': # Get estimate
                if challenge_list:
                    temp_sum += reduce(lambda x, y: x + y, challenge_list)
            else: # Get match
                self.donor_dict[donor]._donations = challenge_list
        if projection == '1':
            print("Estimated match contribution is ${:.2f}.".format(temp_sum))
        else: # projection == '2'
            print("Donations have been multiplied by a factor of {}.".format(factor))
        return self.donor_dict


# Outside the donor collection class


def main_prompt():
    """Prompts the user to enter an option"""
    response = input("\n\
        Choose from one of 5 actions:\n\
        1) Send a Thank You\n\
        2) Create a Report\n\
        3) Send letters to everyone\n\
        4) Multiply donations by a factor\n\
        5) Quit\n\
        Please type 1, 2, 3, 4, or 5: ")
    return response

def action(switch_dict):
    """Takes in a user input as a parameter, enters a donation, prints a report,
    prints list, exit, prompts again if the input is bad
    If the user types exit it'll go back to the main prompt"""
    while True:
        user_input = main_prompt()
        try:
            switch_dict.get(user_input)()
        except (TypeError, ValueError):
            print("Invalid input, {} please try again.".format(user_input))

def get_new_donor_name():
    """Prompts the user for a new donor name"""
    return input("Enter a full name: ")

def get_new_donor_amount():
    """Prompts the user for a donation amount"""
    return input("Enter a donation amount: ")

def get_multip_factor():
    """Prompts the user to enter a number to multiply the donations by a factor"""
    return float(input("Enter a factor to multiply the donations by: "))

def get_min_donation():
    """Prompts the user to enter a number that's the lower donation
    threshold for the filter"""
    return float(input("Enter a lower donation limit: "))

def get_max_donation():
    """Prompts the user to enter a number that's the upper donation
    threshold for the filter"""
    return float(input("Enter a upper donation limit: "))

def get_projection():
    """Prompts the user whether they want an estimate or an actual match"""
    the_input = input("Type (1) if you want an estimate or type (2) if you want a match: ")
    while the_input not in ['1','2']:
        the_input = input("Type (1) if you want an estimate or type (2) if you want a match: ")
    return the_input

# Python program to use main for function call
if __name__ == "__main__":
    d1 = Donor("Bom", "Trady", [500.00, 750.00, 1000.00, 1250.00, 1500.00])
    d2 = Donor("Raron", "Aodgers", [1500.00, 2000.00])
    d3 = Donor("Brew", "Drees", [2000.00, 3500.00, 5000.00])
    donor_dict = {"Bom Trady": d1, "Raron Aodgers": d2, "Brew Drees": d3}
    dc = DonorCollection(donor_dict)
    switch_dict = {
        'list': dc.print_names,
        '1': dc.send_thanks,
        '2': dc.print_report,
        '3': dc.send_letters,
        '4': dc.challenge,
        '5': sys.exit
    }
    action(switch_dict)