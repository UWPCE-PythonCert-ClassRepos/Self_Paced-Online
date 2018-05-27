#!/usr/bin/env python3

from collections import OrderedDict
import textwrap
import sys
import copy

# Global dictionary containing donor list and donation amounts
donor_dict = {
            "Harry Potter": [10, 20, 30],
            "Ronald Weasley": [100, 500],
            "Hermione Granger": [50, 100, 150],
            "Draco Malfoy": [5, 1000],
            "Neville Longbottom": [1000]
            }


def get_donor():
    """
    Prompts user to enter a donor's name.

    Args: None.
    """

    donor_name = input("Please enter the full name of a donor. You can also enter 'list' to see all current donors or 'e' to exit: ")
    if donor_name == "e":
        menu_selection(main_prompt, main_dispatch)
    elif donor_name == "list":
        print(list_donors())
        menu_selection(main_prompt, main_dispatch)
    else:
        return donor_name


def list_donors():
    """
    Returns a list of all donors.

    Args: None.
    """
    donor_list = "\n"+ "\n".join(donor_dict.keys())
    return donor_list


def add_new_donor(donor_name):
    """
    Adds a new donor and donation to the dictionary.

    Args:
    donor_name:  The donor's name.
    """
    donor_dict[donor_name] = []


def get_donation():
    """
    Prompts the user for a donoation amount and returns the value.

    Args: None.
    """
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


def add_donation(donor_name, donation_amount):
    """
    Adds a new donation amount for new and existing donors.

    Args:
    donor_name:  A donor.
    donation_amount:  Donation amount for the donor.
    """
    if donor_name in donor_dict:
        donor_dict[donor_name].append(donation_amount)
    else:
        add_new_donor(donor_name)
        donor_dict[donor_name].append(donation_amount)


def send_thankyou():
    """
    Provides the following functionality:
    1. Lists all donors
    2. Adds new donors
    3. Enters new donations
    4. Sends a thank you email

    Args: None
    """
    donor = get_donor()
    donation = get_donation()
    add_donation(donor, donation)
    print(send_mail(donor, donation))
    return


def create_report():
    """
    Prints a report of all donors sorted by total donations descending.

    Args: None.
    """
    print ("{:30s} | {:11s} | {:9s} | {:12s}".format("Donor Name", "Total Given", "Num donations", "Average donation"))
    print ("-" * 79)

    sorted_donor_dict = OrderedDict(sorted(donor_dict.items(), key=lambda i: sum(i[1]), reverse=True))
    
    for (donor, donations) in sorted_donor_dict.items():
        donor_name = donor
        total_given = sum(donations)
        num_donations = len(donations)
        average_donation = (total_given / num_donations)
        print ("{:30s}  ${:11.2f}   {:12d}    ${:12.2f}".format(donor_name, total_given, num_donations, average_donation))


def send_mail(donor_name, donation_amount):
    email = textwrap.dedent('''
        Dear {:s},

        Thank you for your very kind donation of ${:.2f}.
        It will be put to very good use.

        Sincerely,
        -Hogwarts School of Witchcraft and Wizardry''')

    return email.format(donor_name, donation_amount)


def create_mail_file():
    """
    Creates a text file with a thank you message.

    Args: None.
    """
    for donor, donation in donor_dict.items():
        filename = donor + ".txt"
        letter = send_mail(donor, donation[-1])
        try:
            with open(filename, 'w') as outfile:
                outfile.write(letter)
        except IOError:
            print("Unable to open file or write file.")


def get_total_donations(temp_dict):
    """
    Returns the sum of all donations.

    Args:
    temp_dict: A donor dictionary.
    """
    total_given = 0
    for donation in temp_dict.values():
        for x in donation:
            total_given += x
    return total_given


def filter_donations(min_donation, max_donation, temp_dict):
    """
    Filters donations between the min/max donation constraints.

    Args:
    min_donation: Minimum donation amount.
    max_donation: Maxiumum donation amount.
    temp_dict: A donor dictionary
    """
    filtered_dict = {}
    for (donor, donations) in temp_dict.items():
        filtered_dict[donor] = list(filter(lambda x: x > min_donation and x < max_donation, donations))
    return filtered_dict


def multiply_donations(factor, temp_dict):
    """
    Returns dictionary with donation multiplied by factor.

    Args:
    factor: Muliplier variable.
    temp_dict: A donor dictionary.
    """
    for donations in temp_dict.values():
        donations[:] = list(map(lambda x: x * factor, donations))
    return temp_dict


def challenge(factor, min_donation, max_donation, donor_dict):
    """
    Returns a new dictionary, filtered, with donation amounts multiplied by factor.

    Args:
    factor: Muliplier variable.
    min_donation: Minimum donation amount.
    max_donation: Maxiumum donation amount.
    donor_dict: Donor dictionary.
    """
    new_donor_dict = copy.deepcopy(donor_dict)
    new_donor_dict = multiply_donations(factor, filter_donations(min_donation, max_donation, new_donor_dict))
    
    return new_donor_dict


def donation_projections():
    """
    Crate a report with original and projected donations totals.

    Args:
    None.
    """
    factor = int(input("Please enter a multiplier factor: "))
    min_donation = int(input("Please enter a min donation amount: "))
    max_donation = int(input("Please enter a max donation amount: ")) 
    
    print()
    print ("{:^22s} | {:^20s} | {:^22s}".format("Current Donation Total", "User Projected Total", "Model Projected Total (3 x Donatins > 50)"))
    print ("-" * 89)
    print ("${:^22.2f} ${:^20.2f} ${:^40.2f}".format(get_total_donations(donor_dict), get_total_donations(challenge(factor, min_donation, max_donation, donor_dict)), get_total_donations(challenge(3, 50, 10000000, donor_dict))))


def abort():
    """
    Quit the script

    Args: None
    """
    print("Bye!")
    sys.exit()


"""
The funtion below produce the main selection menu
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
      3 - Send Letters to Everyone
      4 - View Donation Models/Projections
      5 - Quit
      : """)

main_dispatch = {"1": send_thankyou,
                 "2": create_report,
                 "3": create_mail_file,
                 "4": donation_projections,
                 "5": abort,
                 }

if __name__ == '__main__': 
    menu_selection(main_prompt, main_dispatch)