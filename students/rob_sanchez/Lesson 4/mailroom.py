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
    prompt = "\nChoose an action:\n"
    menu_sel = "\n1. Send a Thank You\n2. Create a Report\n3. Quit\n"

    # User selection
    while True:
        try:
            user_selection = input(prompt + menu_sel)
            options.get(int(user_selection))()
            # user_selection = input()
        except ValueError:
            pass
        except NameError:
            pass
        except TypeError:
            pass


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

        donor_dict[donor_name] = [float(amt_input)]
        send_email(history)
    # Append their last contribution to their history
    else:
        amt_input = input("\nDonation amount:\n")

        donor_dict[donor_name].append(float(amt_input))

        history["donor_name"] = donor_name
        history["Amount"] = donor_dict[donor_name][-1]

        send_email(history)
    return False


# Creates a summary report of the donations
def create_report():
    headers = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    str_format = "{:<30} ${:>17} {:>16} ${:>14}"
    print(("\n{:<30} | {:^15} | {:^15} | {:^15}").format(*headers))
    print("-"*82)

    donor_avg = {}
    num_gifts = {}
    avg_gift = {}

    donor_avg = {key: sum(donor_dict[key]) for key in donor_dict}
    num_gifts = {key: len(donor_dict[key]) for key in donor_dict}
    avg_gift = {key: sum(donor_dict[key])/len(donor_dict[key]) for key in donor_dict}

    for key, value in donor_dict.items():
        print(str_format.format(key, donor_avg[key], num_gifts[key], avg_gift[key]))

    return False


# Helper methods

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


if __name__ == "__main__":
    main()
