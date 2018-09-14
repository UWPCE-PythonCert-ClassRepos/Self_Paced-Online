#!/usr/bin/env python3
import sys
import re
from donor_class import Donations
from donor_class import Donor


# List of donors and donation amounts
donations_list = Donations()
donor_list = Donor()

donations_list.add_donation("Tom Cruise", 100)
donations_list.add_donation("Tom Cruise", 200)
donations_list.add_donation("Tom Cruise", 300)

donations_list.add_donation("Michael Jordan", 1300)

donations_list.add_donation("Katy Perry", 4500)
donations_list.add_donation("Katy Perry", 1500)

donations_list.add_donation("Adam Sandler", 500)
donations_list.add_donation("Adam Sandler", 2400)


def main():
    # Menu options
    options = {1: send_thank_you,
               2: create_report,
               3: send_letters,
               4: challenge,
               5: sys.exit}
    prompt = "\nChoose an action:\n"
    menu_sel = ("\n1 - Send a Thank You\n2 - Create a Report\n"
                "3 - Send letters to everyone\n4 - Projections\n5 - Quit\n")

    # User selection
    while True:
        try:
            user_selection = input(prompt + menu_sel)
            options.get(int(user_selection))()
        except ValueError:
            print("\nPlease select a numeric value...")
        except TypeError:
            print("\nOption {} is invalid. Try again...".format(user_selection))


# Sends a thank you email to the selected donor
def send_thank_you():

    # Get name of donor
    donor_name = name_prompt()

    # Display list of donors when user types "list"
    while donor_name.lower() == "list":
        print (donations_list.get_formatted_list_of_donors())
        donor_name = name_prompt()

    # Get donation amount
    amt_input = donation_prompt()

    donations_list.add_donation(donor_name, float(amt_input))

    donor_list.add_donor(donor_name)
    donor_list.add_donation(float(amt_input))

    print(send_email(donor_list.get_donor_details()))


# Creates a summary report of the donations
def create_report():
    donations_list.get_summary


# Creates a thank you file for each donor
def send_letters():

    for value in donations_list.get_list_of_donors():
        with open(value+'.txt', 'w') as f:
            f.write(create_letter(donations_list.get_donor_summary(value)))


def challenge():
    while True:
        try:
            name = name_prompt()
            min = min_prompt()
            max = max_prompt()
            multiplier = multiplier_prompt()
            print(donations_list.challenge(name, factor=multiplier, min=min, max=max))
            break
        except ValueError:
            print("\n>> Please enter a valid name <<")
        except KeyError:
            print("\n>> Donor not found <<")


# Helper methods:
# Asks user for the name of donor to send thank you email
def name_prompt():
    while True:
        try:
            name = input("\nPlease enter the Donor's full name:\n").strip()
            if re.match("^[A-Za-z ,]*$", name) and name:
                return name
                break
            else:
                print("\n>> Please enter a valid name <<")
        except ValueError:
            print("\n>> Please enter a valid name <<")


# Asks user for the donation amount
def donation_prompt():
    while True:
        try:
            amount = re.sub("[, ]", "", input("\nDonation amount:\n$"))
            return round(float(amount), 2)
            break
        except ValueError:
            print("\n>> Please enter a valid donation amount <<")


# Asks user for the donation multiplier number
def multiplier_prompt():
    while True:
        try:
            multiplier = re.sub("[, ]", "", input("\nMultiply donations by: "))
            return int(multiplier)
            break
        except ValueError:
            print("\n>> Please enter a valid multiplier <<")


# Asks user for a minimum donation
def min_prompt():
    while True:
        try:
            min = re.sub("[, ]", "", input("\nMin donation (Press enter for default value): "))
            return round(float(0), 2) if not min else round(float(min), 2)
            break
        except ValueError:
            print("\n>> Please enter a valid minimum value <<")


# Asks user for a maximum donation
def max_prompt():
    while True:
        try:
            max = re.sub("[, ]", "", input("\nMax donation (Press enter for default value): "))
            return round(float(9999999), 2) if not max else round(float(max), 2)
            break
        except ValueError:
            print("\n>> Please enter a valid maximum value <<")


# Sends an email to the specified donor
def send_email(new_donor):
    body = ("\nDear {donor_name},\n\n"
            "I would like to personally thank you for your generours donation "
            "of ${amount} to our charity organization.\nYour support allows us"
            " to continue supporting more individuals in need of our services."
            "\n\nSincerely,\nCharity Inc.\n").format(**new_donor)
    return body


# Thank you letter template
def create_letter(donations):
    body = ("\nDear {donor_name},\n\n"
            "I would like to personally thank you for your recent "
            "donation of ${last_donation} to our charity organization. "
            "You have donated a total of ${total} as of today. "
            "Your support allows us to continue supporting more individuals "
            "in need of our services."
            "\n\nSincerely,\nCharity Inc.\n").format(**donations)
    return body


if __name__ == "__main__":
    main()
