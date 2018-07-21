#!/usr/bin/env python3
import sys
import re


# List of donors and donation amounts
donor_dict = {"Tom Cruise": [100, 200, 300],
              "Michael Jordan": [1300],
              "Katy Perry": [4500, 1500],
              "Adam Sandler": [500, 2400]}


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
    # Holds a history of the donor's name and donation amount
    history = {}

    # Get name of donor
    donor_name = get_donor_name()

    # Display list of donors when user types "list"
    while donor_name.lower() == "list":
        print ("\nList of Donors: " + get_formatted_values(list(donor_dict)))
        donor_name = get_donor_name()

    # Get donation amount
    amt_input = get_donation_amount()

    add_donor(donor_name, float(amt_input))

    history["donor_name"] = donor_name
    history["amount"] = amt_input

    print(send_email(history))


# Creates a summary report of the donations
def create_report():
    headers = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    str_format = "{:<30} ${:>17} {:>16} ${:>14}"
    print(("\n{:<30} | {:^15} | {:^15} | {:^15}").format(*headers))
    print("-"*82)

    donor_total = get_donor_totals(donor_dict)
    num_gifts = get_num_gifts(donor_dict)
    avg_gift = get_averages(donor_dict)

    for key, value in donor_total.items():
        print(str_format.format(key, round(float(donor_total[key]), 2),
              num_gifts[key], round(avg_gift[key], 2)))


# Creates a thank you file for each donor
def send_letters():
    new_list = {}
    donor_total = {}

    donor_total = {key: sum(donor_dict[key]) for key in donor_dict}

    for key, value in donor_dict.items():
        # f = open(key+'.txt', 'w')
        with open(key+'.txt', 'w') as f:
            new_list["donor_name"] = key
            new_list["last_donation"] = donor_dict[key][-1]
            new_list["total"] = donor_total[key]
            f.write(create_letter(new_list))


# Helper methods:

# Returns a list of formatted values
def get_formatted_values(in_val):
    form_string = ", ".join(["{:s}"] * len(in_val))
    return form_string.format(*in_val)


# Add donor if it doesn't exist in current dictionary,
# otherwise append their last contribution
def add_donor(donor, amt):
    donor_dict.setdefault(donor, []).append(float(amt))


# Asks user for the name of donor to send thank you email
def get_donor_name():
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
def get_donation_amount():
    while True:
        try:
            amount = re.sub("[, ]", "", input("\nDonation amount:\n$"))
            return round(float(amount), 2)
            break
        except ValueError:
            print("\n>> Please enter a valid donation amount <<")


# Returns the total donation amount and returns it in ascending order
def get_donor_totals(in_list):
    donor_total = {key: sum(in_list[key]) for key in in_list}
    donor_total = dict(sorted(donor_total.items(), key=lambda t: t[1], reverse=True))
    return donor_total


# Returns the totatl number of gifts from each donor
def get_num_gifts(in_list):
    return {key: len(in_list[key]) for key in in_list}


# Returns the average donation amount for each donor
def get_averages(in_list):
    return {key: sum(in_list[key])/len(in_list[key]) for key in in_list}


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
