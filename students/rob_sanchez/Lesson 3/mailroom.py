#!/usr/bin/env python3
import sys

# List of donors and donation amounts
donor_dict = {"John": {
                "donations": [
                  {"donation-number": '1', "amount": '100'},
                  {"donation-number": '2', "amount": '200'},
                  {"donation-number": '3', "amount": '300'}
                ]},
              "Michael": {
                "donations": [
                    {"donation-number": '1', "amount": '1300'}
                ]},
              "Sarah": {
                "donations": [
                    {"donation-number": '1', "amount": '4500'},
                    {"donation-number": '2', "amount": '1500'}
                ]}
              }


def main():
    print("\nWelcome!\n")
    welcome()


# Displays the initial welcome prompt
def welcome():

    # Prompt for the option to be executed
    print("\nSelect an option below:\n")

    selection = welcome_options()

    if selection == '1':
        send_thank_you()
    elif selection == '2':
        create_report()
    elif selection == '3':
        sys.exit()


# Sends a thank you email to the selected donor
def send_thank_you():
    # Name of donor to send thank you email
    donor_name = input("\nPlease enter the Donor's full name:\n")

    # Create list of names
    name_set = set()
    for donor, value in donor_dict.items():
        name_set.add(donor)

    while donor_name.lower() == "list":
        print ("\nList of Donors: " + print_list(list(name_set)))
        donor_name = input("\nPlease enter the Donor's full name:\n")

    if donor_name not in list(name_set):
        amt_input = input("\nDonation amount:\n")

        donor_dict[donor_name] = {"donations": [{"donation-number": '1', "amount": '0'}]}
        donor_dict[donor_name]["donations"][0]["amount"] = float(amt_input)
        send_email(donor_name, amt_input)
    else:
        amt_input = input("\nDonation amount:\n")
        history = donor_dict[donor_name]["donations"]
        num_of_donations = []

        for item in history:
            num_of_donations.append(item.get('amount'))

        new_index = len(num_of_donations)

        donor_dict[donor_name]["donations"].append(
                            {"donation-number": '', "amount": ''})
        donor_dict[donor_name]["donations"][new_index]["donation-number"] = new_index + 1
        donor_dict[donor_name]["donations"][new_index]["amount"] = float(amt_input)

        send_email(donor_name, amt_input)


# Creates a summary report of the donations
def create_report():
    headers = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(("{:<30} | {:^15} | {:^15} | {:^15}").format(*headers))
    print("-"*82)

    donor_report = get_summary()

    for item in donor_report:
        print(("{:<30} ${:>17} {:>16} ${:>14}").format(*item))

    welcome()

# Helper methods
def welcome_options():
    # Menu options
    options = "1. Send a Thank You\n2. Create a Report\n3. Quit\n"
    selection_options = ('1', '2', '3')

    # Selection value
    selection_no = input(options)

    # Keep prompting user until a matching value is found
    while selection_no not in selection_options:
        print("\nInvalid Input! Try again.\n")
        selection_no = input(options)
    return selection_no


# Returns a list of formatted values
def print_list(in_val):
    form_string = ", ".join(["{:s}"] * len(in_val))
    return form_string.format(*in_val)


# Sends an email to the specified donor
def send_email(donor, amount):
    greeting = "\nDear {},\n\n".format(donor)
    body = ("I would like to personally thank you for your generours donation"
            " of ${:.2f} to our charity organization.\nYour support allows us "
            "to continue supporting more individuals in need of our services."
            "\n\nSincerely,\nCharity Inc.\n").format(float(amount))
    print(greeting, body)
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
        donor_names[i].append(sum_values(total_given))
        donor_names[i].append(len(num_gifts))
        donor_names[i].append(sum_values(total_given)/len(num_gifts))
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
