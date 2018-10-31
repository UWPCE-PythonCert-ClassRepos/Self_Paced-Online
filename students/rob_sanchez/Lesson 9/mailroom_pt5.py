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
               4: sys.exit}
    prompt = "\nChoose an action:\n"
    menu_sel = ("\n1 - Send a Thank You\n2 - Create a Report\n"
                "3 - Send letters to everyone\n4 - Quit\n")

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
