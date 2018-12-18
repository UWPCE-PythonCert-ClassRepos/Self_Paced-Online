#-------------------------------------------------#
# Title: Object Oriented Mail Room
# Dev:   LDenney
# Date:  December 13, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/11/18, Created MailRoom Part 1 File
#   Laura Denney, 10/12/18, Modified MailRoom Part 1 File
#   Laura Denney, 10/12/18, Started Part 2
#   Laura Denney, 10/12/18, Finished Part 2
#   Laura Denney, 10/31/18, Started MailRoom Part 3
#   Laura Denney, 11/7/18, Started MailRoom Part 4
#   Laura Denney, 12/7/18, Started Object Oriented Mail Room
#   Laura Denney, 12/17/18, Added Saving / Loading Functionality
#-------------------------------------------------#

#adding date to txt file
from datetime import date

#file handling help
import os

#Donor Class contains name, donations
class Donor(object):
    name = ""
    donations = None

    @property
    def sum_donations(self):
        return sum(self.donations)
    @property
    def total_donations(self):
        return len(self.donations)
    @property
    def average_donation(self):
        return self.sum_donations / self.total_donations

    def __init__(self, name, *args):
        self.name = name.lower()
        self.donations = []
        if args:
            for arg in args:
                self.donations.append(arg)

    def __repr__(self):
        repr_str = "Donor('{}', " + ", ".join(["{}"] * len(self.donations)) + ")"
        return repr_str.format(self.name, *self.donations)

    def __eq__(self, other):
        return ((self.sum_donations, self.name) == \
                (other.sum_donations, other.name))

    def __lt__(self, other):
        return ((self.sum_donations, self.name) < \
                (other.sum_donations, other.name))

    def append(self, donation):
        self.donations.append(donation)
####################################################
#Donors Class - manipulates a list of donors
class Donors(object):
    donor_list = None

    def __init__(self, *args):
        self.donor_list = []
        for arg in args:
            self.donor_list.append(arg)

    def __repr__(self):
        repr_str = "Donors(" + ", ".join(["{}"] * len(self)) + ")"
        return repr_str.format(*self.donor_list)

    def __len__(self):
        return len(self.donor_list)

    def add_new_donor(self, donor):
        self.donor_list.append(donor)


    def is_current_donor(self, donor):
        return donor.lower() in repr(self)

    def get_list(self):
        names = [donor.name.title() for donor in self.donor_list]
        strformat = "\nWe have {} current donors: " + ", ".join(["{}"] * len(names))
        return strformat.format(len(names), *names)

    def create_string_report(self):
        self.donor_list.sort(reverse = True)
        report = '''
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------'''
        strformat = '\n{:<26}${:>13.2f}{:^12}${:>13.2f}'
        for donor in self.donor_list:
            report +=  strformat.format(donor.name.title(),donor.sum_donations,
                                    donor.total_donations, donor.average_donation)
        return report

    def get_donor(self, name):
        for donor in self.donor_list:
            if donor.name == name:
                return donor

    def check_current_donor(self, name, donation):
        if self.is_current_donor(name):
            current_donor = self.get_donor(name)
            current_donor.append(donation)
            return "\n{} is a current donor, we will update their donations.".format(name.title())

        else:
            self.add_new_donor(Donor(name, donation))
            return "\n{} is not a current donor, we will add them to our system.".format(name.title())

    def send_letters_per_donor(self):
        total_letters = 0
        for each_donor in self.donor_list:
            donor = each_donor.name.title()
            #Name formatting for one word names like 'Cher' vs normal full names
            first_last = donor.split(" ")
            if len(first_last) == 1:
                first = first_last[0]
                last = ""
            else:
                first = first_last[0]
                last = first_last[1]
            total_letters += send_email(donor, each_donor.sum_donations, "{}_{}_{}.txt".format(first, last, date.today().isoformat()))
        return total_letters

    @classmethod
    def load_list_donors(cls):
        with open("donor_list.txt", "r") as infile:
            infile_str = infile.read()
        self = eval(infile_str)
        return self


    def save_list_donors(self):
        with open("donor_list.txt", 'w') as outfile:
            outfile.write(repr(self))
####################################################
####################################################

#Non-class variables and functions

donors = None

main_prompt = '''
What would you like to do today?
1) Send a Thank You
2) Create a Report
3) Send letters to everyone
4) Load previously saved list of donors from file
5) Save current list of donors to file
6) Quit
Please choose the number of your choice >> '''

thank_you_prompt = '''
You have chosen to Send a Thank You.
1) See List of Current Donors
2) I'm Ready to Thank a Donor
3) Quit this submenu
Please choose the number of your choice >> '''

def send_thank_you():
    while True:
        try:
            response = input(thank_you_prompt)
            if sub_choice_dict[response]() == 'quit':
                print("\nYou have chosen to leave this submenu.")
                break
        except KeyError:
            print("\nThat is not a valid selection. Please choose 1, 2, or 3.")

def create_report():
    print("\nYou have chosen to Create a Report.")
    print(donors.create_string_report())

def send_letters():
    print("\nYou have chosen to send letters to everyone.")
    total_letters_sent = donors.send_letters_per_donor()
    print(f"\nA total of {total_letters_sent} letters have been successfully sent to our donors.")
    print("A copy of those letters are now saved in your current directory.")

def quit():
    return 'quit'

def print_list():
    print(donors.get_list())

def thank_a_donor():
    name = input("\nPlease enter the full name of the donor you would like to thank: ").lower()
    donation = input("How much money did they donate? (type 100 for $100) >> ")
    donation = validate_donation(donation)
    print(donors.check_current_donor(name, donation))
    print("The email you are sending is as follows:")
    print(send_email(name.title(), donation))
    print("You have successfully sent a Thank You to {}.".format(name.title()))

def validate_donation(donation):
    try:
        num = float(donation)
    except ValueError:
        print("\nERROR: Invalid donation amount entered, marking donation as $0.")
        num = 0.0
    return num

#modified to either print to screen or disk
def send_email(donor, amount, dest = 0):
    fstring =f'''
    Dear {donor},

    We would like to thank you for your generous donation
    of ${amount:.2f}. It will be put to great use!

    Thank you!
    <3 The MailRoom
    '''
    if not dest:
        return fstring
    else:
        with open(dest, 'w') as outfile:
            outfile.write(fstring)
        return 1

def load_list():
    global donors
    donors = Donors.load_list_donors()

def save_list():
    donors.save_list_donors()

def first_run():
    exists = os.path.isfile("donor_list.txt")
    if not exists:
        global donors
        donors = Donors(Donor("john doe",100.50, 200.00),
        Donor("laura denney",5.00),
        Donor("bill gates",4000),
        Donor("samuel jackson",1,2,3),
        Donor("mr. bean", 500, 100))

#Main Menu options for user
main_choice_dict = {
    "1": send_thank_you,
    "2": create_report,
    "3": send_letters,
    "4": load_list,
    "5": save_list,
    "6": quit
}

#Send Thank You Sub Menu options for user
sub_choice_dict = {
    "1": print_list,
    "2": thank_a_donor,
    "3": quit
}

#Main menu to prompt user
def prompt_user():
    first_run()
    while True:
        try:
            response = input(main_prompt)
            if main_choice_dict[response]() == 'quit':
                print("\nYou have chosen to quit. Have a good day!")
                break
        except AttributeError:
            print("\nIt appears there are no donors on file, we recommend loading a saved list.")
        except KeyError:
            print("\nThat is not a valid selection. Please choose option 1 - 6.")
        except FileNotFoundError:
            print("\nNo saved list of donors found, please work with current list.")
##########################################################

if __name__ == '__main__':
    prompt_user()



