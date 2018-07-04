#!/usr/bin/env python3

# -------------------------------------#
# Desc: Mailroom Part 3
# Dev: Will White
# Date: 6/11/2018
# ChangeLog: (When,Who,What)
# -------------------------------------#
import math

dict_donations = {
    "bill gates": [25000.00, 3], "monet holt": [50000.00, 2], "jeff bezos": [123500.09, 3],
    "john wick": [120000.00, 2], "john snow": [10.56, 1]
}  # List of donors


def prompt_for_number_in_range(prompt_text, min_limit, max_limit):

    min_limit = float(min_limit)
    max_limit = float(max_limit)

    while True:
        try:
            return_number = input(prompt_text)
            return_number = float(return_number)

            if min_limit <= return_number <= max_limit:
                break
            else:
                print("Number out of range.")
        except ValueError:
            print("Input could not be converted to a float")

    return return_number


def menu_options():  # Function to run the menu options
    user_input = prompt_for_number_in_range(
        'Please enter a number from the following options:\n\n' +
        '[1] Send a Thank You\n' +
        '[2] Create a Report\n' +
        '[3] Send Letters to Everyone\n' +
        '[4] Quit the Program\n', 1, 4)
    return user_input  # Function returns user_input


def prompt_for_name():  # Function to prompt the user for a name
    donor_name = input("Please input the donor's name, or type 'list' to see a list of donor names: \n")
    while donor_name == 'list':  # If user inputs "list", program will print a list of current donors
        for key in dict_donations:
            print(key.title())
        donor_name = input("\nPlease input the donor's name: \n").lower()
    return donor_name  # Function returns the donor's name


def add_donation_amount(donor_name, donation_amount):
    if donor_name in dict_donations:
        dict_donations[donor_name][0] += donation_amount
        dict_donations[donor_name][1] += 1
    else:
        dict_donations[donor_name] = [donation_amount, 1]


def add_donation():  # Function for the user to add a donation
    donor_name = prompt_for_name()
    donation_amount = prompt_for_number_in_range("Please input the donation amount: ", 0, math.inf)

    add_donation_amount(donor_name, donation_amount)
    print(print_letter(donor_name, donation_amount))


def print_letter(donor_name, donation_amount):
    dict_donor_info = {'name': donor_name.title(), 'donation': donation_amount}
    str_letter = '''
Dear {name},

Thank you for your donation of {donation:.2f}, it is very much appreciated.

Kind Regards,
Your Favorite Local Charity
'''.format(**dict_donor_info) # Thank you email with formatting to include donor name and amount
    return str_letter


def sort_list():
    dict_to_list = []
    for donor in dict_donations:
        dict_to_list.append([donor, dict_donations[donor][0]])
    sorted_list = sorted(dict_to_list, key=lambda x: x[1], reverse=True)
    return sorted_list


def create_a_report():  # Function to create a report of all the current donor info
    sorted_list = sort_list()
    title_header = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print('{:<10}{:>20}{:>20}{:>20}'.format(*title_header))
    print('----------------------------------------------------------------------')

    for i in sorted_list:
        donor_name = i[0]
        donor_count = dict_donations[donor_name][1]
        print('{:<10}{:>20.2f}{:>20}{:>20.2f}'.format(donor_name.title(), i[1], donor_count, (i[1] / donor_count)))


def send_letters():
    for donor_name in dict_donations:
        with open("{}.txt".format(donor_name), 'w') as txt_file:
            txt_file.write(print_letter(donor_name, dict_donations[donor_name][0]))


switch_func_dict = {
    1: add_donation,
    2: create_a_report,
    3: send_letters
}

if __name__ == "__main__":  # If this is the main file, run the below

    while True:
        option_selected = menu_options()  # Run the menu options function and save the input
        option_selected = int(option_selected)
        if option_selected < 4:  # If user entered 1, get the name and run the add_donation function
            try:
                switch_func_dict.get(option_selected)()
            except KeyError:
                print("Option doesn't exist.")
        else:  # If the user enters anything else, quit the program
            break

    print("Thank you, the program will now exit")
    raise SystemExit  # Exit the program
