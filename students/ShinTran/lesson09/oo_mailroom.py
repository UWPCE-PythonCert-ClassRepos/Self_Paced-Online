'''
Shin Tran
Python 210
Lesson 9 Assignment
'''

#!/usr/bin/env python3
# Implementing the mailroom program using object oriented programming

import sys

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
        letter_list = []
        message = "Dear {:s},\n\
        Thank you for donating ${:,.2f}.\n\
        Sincerely,\n\
        Your Local Charity"
        for name, vals in self.donor_dict.items():
            with open(name + ".txt",'w') as output:
                output.write(message.format(name, vals.get_donation_total))
                letter_list.append(message.format(name, vals.get_donation_total))
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


# Outside the donor collection class


def main_prompt():
    """Prompts the user to enter an option"""
    response = input("\n\
        Choose from one of 4 actions:\n\
        1) Send a Thank You\n\
        2) Create a Report\n\
        3) Send letters to everyone\n\
        4) Quit\n\
        Please type 1, 2, 3, or 4: ")
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

# Python program to use main for function call
if __name__ == "__main__":
    d1 = Donor("James", "Smith", [33558.77, 30929.47, 27173.01])
    d2 = Donor("John", "Williams", [41113.42])
    d3 = Donor("Robert", "Jones", [21067.11, 30160.42])
    donor_dict = {"James Smith": d1, "John Williams": d2, "Robert Jones": d3}
    dc = DonorCollection(donor_dict)
    switch_dict = {
        'list': dc.print_names,
        '1': dc.send_thanks,
        '2': dc.print_report,
        '3': dc.send_letters,
        '4': sys.exit
    }
    action(switch_dict)