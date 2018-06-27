#!/usr/bin/env python3
import sys
import collections


# List of donors and donation amounts
donor_dict = {"Tom Cruise": [100, 200, 300],
              "Michael Jordan": [1300],
              "Katy Perry": [4500, 1500],
              "Adam Sandler": [500, 2400]}


def main():

    welcome()


# Displays the initial welcome prompt
def welcome():
    # Menu options
    options = {1: send_thank_you,
               2: create_report,
               3: sys.exit}

    welcome_options(options)

    while True:
        # User selection
        user_selection = input()
        options.get(int(user_selection), welcome_options(options))()


# Sends a thank you email to the selected donor
def send_thank_you():
    # Name of donor to send thank you email
    donor_name = input("\nPlease enter the Donor's full name:\n")
    history = {}

    # Create list of names
    name_set = set()
    for donor, value in donor_dict.items():
        name_set.add(donor)

    while donor_name.lower() == "list":
        print ("\nList of Donors: " + print_list(list(name_set)))
        donor_name = input("\nPlease enter the Donor's full name:\n")

    # Add donor if it doesn't exist in current dictionary
    if donor_name not in list(name_set):
        amt_input = input("\nDonation amount:\n")

        history["donor_name"] = donor_name
        history["Amount"] = amt_input

        donor_dict[donor_name] = [amt_input]
        send_email(history)
    # Append their last contribution to their history
    else:
        amt_input = input("\nDonation amount:\n")

        donor_dict[donor_name].append(amt_input)

        history["donor_name"] = donor_name
        history["Amount"] = donor_dict[donor_name][-1]

        send_email(history)
    return False


# Creates a summary report of the donations
def create_report():
    headers = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(("{:<30} | {:^15} | {:^15} | {:^15}").format(*headers))
    print("-"*82)

    donor_report = get_summary()

    for item in donor_report:
        print(("{:<30} ${:>17} {:>16} ${:>14}").format(*item))

    return False


# Helper methods
def welcome_options(menu_options):
    print("\nSelect an option below:\n")
    for key in sorted(menu_options):
        print(key, "-", menu_options[key].__name__)


# Returns a list of formatted values
def print_list(in_val):
    form_string = ", ".join(["{:s}"] * len(in_val))
    return form_string.format(*in_val)


# Sends an email to the specified donor
def send_email(new_donor):
    body = ("\nDear {donor_name},\n\n"
            "I would like to personally thank you for your generours donation "
            "of ${Amount} to our charity organization.\nYour support allows us"
            " to continue supporting more individuals in need of our services."
            "\n\nSincerely,\nCharity Inc.\n").format(**new_donor)
    print(body)
    welcome()


# Returns donation summary of each donor
def get_summary():
    donor_names = []
    total_given = []
    num_gifts = []
    i = 0

    for donor, value in donor_dict.items():
        history = donor_dict[donor]["donations"]
        donor_names.append([])
        donor_names[i].append(donor)
        for item in history:
            total_given.append(float(item.get('amount')))
            num_gifts.append(item.get('donation-number'))
        donor_names[i].append("{:.2f}".format(sum_values(total_given)))
        donor_names[i].append(len(num_gifts))
        donor_names[i].append("{:.2f}".format(sum_values(total_given)/len(num_gifts)))
        total_given = []
        num_gifts = []
        i += 1
    return donor_names


# Adds all the values of a list
def sum_values(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + sum_values(num_list[1:])


if __name__ == "__main__":
    main()
