'''
Name: Muhammad Khan
Date: 04/14/2019
Assignment09
'''
import sys
from mailroom_oo import Donor
from mailroom_oo import DonorCollection

def prompt_user():
    """Return user's selected option as an integer"""
    print()
    while True:
        print('Please choose one of the following options:')
        print("1: Send a Thank You")
        print("2: Create a report")
        print("3: Send letters to everyone")
        print("4: Quit")
        try:
            return int(input("Option:  "))
        except ValueError as e:
            print("***INVALID Option Selected***")


def name_prompt():
    """Return a name string"""
    while True:
        donor_name = input("Please enter the donor's full name OR \n"
                 +"type 'list' for the existing donors: ")
        try:
            if not "".join(donor_name.split()).isalpha():
                raise Exception("The name should be all Alphabetic characters:")
            return donor_name.title()
        except Exception as e:
            print("INVALID Name: ",e)


def donation_prompt(name):
    """
    prompt the user for the donation amount for the given donor.
    :parm 1: name - required parameter.
    :return: donation_amount in decimal form.
    """
    input_msg = "Please enter the donation amount for {}: "
    donation_amount = input(input_msg.format(name))
    while True:
        try:
            return float(donation_amount)
        except ValueError:
            donation_amount=input("INVALID Amount: "+input_msg.format(name))


def display_list(d):
    """Print the donor's list to the user."""
    print("\nOur generous donors: \n")
    for donor_name in iter(d.donors):
        print(donor_name)
    print("\n")


def quit():
    """Exit out from the user interaction."""
    print("Thank you. Have a nice day:")
    sys.exit()


def thank_you(d):
    """
    This method was created to utilize the dictionary (options) in the program
    main flow
    """
    name = name_prompt()
    while name.lower() == "list":
        display_list(d)
        name = name_prompt()
    donation = donation_prompt(name)
    donor = Donor(name, donation)
    print(donor.thank_you())
    d.add_donation(name, donation)


def print_report(d):
    """Print the donors' report in the formatted tabular form."""
    report_data = d.get_report_data()
    title = "{:24} | {:12} | {:10} | {:20}"
    dashes=67*('-');print(dashes)
    print(title.format('Donor Name','Total Given','Num Gifts','Average Gift'))
    strf_format = "{:24} ${:12.2f}   {:^10d}  ${:12.2f}"
    print(dashes)
    for donor in report_data:
        print(strf_format.format(*donor))
    print(dashes)


def send_letter_everyone(d):
    """This method creates the letter for each donor in the donor's database"""
    print("Letters have been sent to all the donors!!!")
    d.send_letter_everyone()



if __name__=="__main__":
    """The flow control of the program. It separates the business logic from
    the data manipulation"""

    options = {1:thank_you,2:print_report,3:send_letter_everyone,4:quit}

    donor_1 = Donor("Adam Johnson",[6000.20, 2200, 1050,100])
    donor_2 = Donor("Matt Marvin",[550,1000,250])
    donor_3 = Donor("Ashley Wiggins",[55.66,270,1000])
    donor_4 = Donor("Kristina Laughrey",[500, 500,200])
    donor_5 = Donor("Kimberley Allen",[12000.99, 5000])
    donor_6 = Donor("Doug Boolinger",[260.57, 930.90])
    donor_7 = Donor("Sherry Henning",[6000, 2460.20, 900])

    d = DonorCollection(donor_1,donor_2,donor_3,donor_4,donor_5,donor_6,donor_7)

    while True:
        user_response = prompt_user()
        if user_response == 4:
            quit()
        try:
             options[user_response](d)
        except (KeyError, ValueError):
            print("***INVALID Option Selected: Please try Again:)***")
