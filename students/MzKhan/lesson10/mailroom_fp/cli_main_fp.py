'''
Name: Muhammad Khan
Date: 04/09/2019
Assignment09
'''
import sys
from mailroom_fp import Donor
from mailroom_fp import DonorCollection

def prompt_user():
    """Return user's selected option as an integer"""
    print()
    while True:
        print('Please choose one of the following options:')
        print("1: Send a Thank You")
        print("2: Create a report")
        print("3: Send letters to everyone")
        print("4: Match donations")
        print("5: Quit")
        try:
            return int(input("Option:  "))
        except ValueError as e:
            print("***INVALID Option Selected***")


def name_prompt(input_msg):
    """Return a name string"""
    while True:
        donor_name = input(input_msg)
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
    input_msg = """Please enter the donor's full name OR
    \rtype 'list' for the existing donors: """
    name = name_prompt(input_msg)
    while name.lower() == "list":
        display_list(d)
        name = name_prompt(input_msg)
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


def match_donations(d):
    print()
    print("The total amount donated = $ {:.2f}".format(d.total_amount_donated))
    input_msg = "Please enter the donor's name: "
    while True:
        print("Please choose one of the following options:")
        print("1: Match to total amount donated")
        print("2: Custom donation")
        print("3: Leave the menu ")
        try:
            user_response = int(input("Option: "))
            if user_response not in [1,2,3]:
                print("***INVALID option selected: Try Again!***")
                continue
            if user_response == 3:break
            name = name_prompt(input_msg) ; name = name.title()
            min_amt, max_amt = None, None
            if user_response == 2:
                min_amt=float(input("Enter minimum amount to match: "))
                max_amt=float(input("Enter maximum amount to match: "))
            mul_factor=float(input("Please enter contribution multiplier: "))
            donation = d.projected_amount(name , mul_factor, min_amt, max_amt)
            print("Your total contribution is = $ {}".format(donation))
            print("With your contribution, the total donation amount = $ {}"
                                               .format(d.total_amount_donated))
        except ValueError as e:
            print("***INVALID Option Selected: Please Try Again!***")


if __name__=="__main__":
    """The flow control of the program. It separates the business logic from
    the data manipulation"""

    options = {1:thank_you,2:print_report,3:send_letter_everyone,
    4:match_donations,5:quit}

    donor_1 = Donor("Adam Johnson",[30., 20, 10,10])
    donor_2 = Donor("Matt Marvin",[40, 10, 5])
    donor_3 = Donor("Ashley Wiggins",[55, 25, 20])
    donor_4 = Donor("Kristina Laughrey",[50, 30, 20])
    donor_5 = Donor("Kimberley Allen",[10, 90])
    donor_6 = Donor("Doug Boolinger",[100])
    donor_7 = Donor("Sherry Henning",[60, 30])

    d = DonorCollection(donor_1,donor_2,donor_3,donor_4,donor_5,donor_6,donor_7)
    while True:
        user_response = prompt_user()
        if user_response == 5:
            quit()
        try:
             options[user_response](d)
        except (KeyError, ValueError):
            print("***INVALID Option Selected: Please try Again***")
