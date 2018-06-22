#!/usr/bin/env python3
# Ian Letourneau
# 6/18/2018
# A script that stores values for donors and their donations.
# The script can process requests from the user on various functions
# to utilize these values
import datetime
from functools import reduce

# Build a dictionary of existing donors
donors = {
    "Bill Gates": [150.00, 20.50, 350.75],
    "Jimmy Kimmel": [456.37, 25.67, 1001.00, 2134.78, 3.14],
    "LeBron James": [87.00, 3.50, 45.00, 749.01]
}


def send_thank_you(name, amount):
    """A function that takes in no parameters, This function allows the user
    to lookup a list of existing donors as well as add a new donor to the
    list. Once a name is chosen, the function prompts the user for an amount
    donated and will add the donation to that donor's donations in the
    dictionary. Finally, the script prints a thank you letter to that donor.
    To quit to the main menu, 'q' can be typed at any user prompt."""

    # Once amount is input, add the donation to the donor key if existing
    # or add both the donor and the donation to the dictionary if new
    if name in donors.keys():
        donors[name].append(amount)
    else:
        donors.setdefault(name, [])
        donors[name].append(amount)

    out_string = ('Dear {}, we wanted to say thank you for your generous'
                  ' donation of ${:.2f}!'.format(name, amount))
    display_thank_you(out_string)
    return out_string


def display_thank_you(string):
    print("")
    print(string)


def create_report():
    """A function that takes no paramters. This function creates a report
    from existing donors and their donations to output donor name,
    total amount donated, number of donations, and average donation amount
    to a compiled list and returns it."""

    # Find longest name to adjust size of table
    name_length = 0
    running_total = 0
    total_dict = {}
    sorted_dict = {}
    sorted_list = []
    out_list = []

    # Loop through donors and track longest name and total donations.
    # Sort donors by total donations
    for name in donors:
        total = 0
        donations = donors[name]
        for value in donations:
            total += value
            total_dict[name] = total
    sorted_list = sorted(total_dict.values(), reverse=True)
    sorted_dict = {key: value for sorted_key in sorted_list for key,
                   value in total_dict.items() if value == sorted_key}

    # Loop through each donor and print their entry based on data in dictionary
    for name in sorted_dict:
        donations = donors[name]
        don_length = (len(donations))
        average = (sorted_dict[name]/don_length)

        out_list.append("{},{:.2f},{},{:.2f}".format(name, sorted_dict[name],
                                                     don_length, average))
    display_report(out_list)
    return out_list


def display_report(sorted_list):
    """A function that displays the compiled list returned from
    create_report()."""
    names = []
    totals = []
    donations = []
    averages = []

    for donor in sorted_list:
        donor_split = donor.split(",")
        names.append(donor_split[0])
        totals.append(float(donor_split[1]))
        donations.append(int(donor_split[2]))
        averages.append(float(donor_split[3]))

    # Find longest name for formatting
    name_length = len(max(names, key=len))

    # Print header line of table adjusting column length by length of name
    print("")
    print("{:{align}{width}} | {:<10} | {:<10} | {:<10}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift",
        align='<', width=str(name_length+1)))
    print("-"*(name_length+43))

    for row in range(len(names)):
        print("{:{align}{width}} $ {:>11.2f}   {:>10d} $ {:>10.2f}".format(
            names[row], totals[row], donations[row], averages[row], align='<',
            width=str(name_length+2)))


def send_all():
    """A function that sends a Thank You letter to every donor in the form of
    creating and writing to a .txt file titled with their name and the current
    date. The .txt includes their name and their total donations within the
    thank you memo."""
    now = datetime.datetime.now()
    letters = []
    # Loop through each donor in the list and calculate total donations.
    for donor in list(donors.keys()):
        total = 0
        donations = donors[donor]
        for value in donations:
            total += value
        donorFile = donor.replace(" ", "")
        # Format .txt filename using the donors name and the current date. Then
        # create file and write thank you letter within open .txt file.
        filename = "{}_{}_{}_{}.txt".format(
            donorFile, now.year, now.month, now.day)
        f = open(filename, "w+")
        f.write('Dear {}, we wanted to say thank you for your generous total'
                ' donations of ${:.2f}! We hope to continue seeing you in'
                ' the future!'.format(
                    donor, float(total)))
        f.close()
        letters.append(filename)
    display_letters_created(letters)
    return letters


def display_letters_created(letters):
    """A function that displays which .txt files were created to the user."""
    letter_string = ("{} "*len(letters)).format(*letters)
    print("The following letters have been created: {}".format(letter_string))


def challenge(factor, mini=None, maxi=None, total=None):
    """A function that takes a factor parameter and maps across the donor
    tables to multiply all donations by that value. The function also takes in
    optional minimum and maximum parameters to filter the donations on what to map
    through as well as an optional total parameter to sum all the remaining values.

    params factor: value to multiply donation table by
    params mini: minimum bound to filter through
    params maxi: maximum bound to filter through
    params total: boolean for totalling final dataset"""

    ret_db = {}
    for name, donations in donors.items():
        if mini != None and maxi != None:
            donations = list(
                filter(lambda x: x >= mini and x <= maxi, donations))
        elif mini != None and maxi == None:
            donations = list(filter(lambda x: x >= mini, donations))
        elif mini == None and maxi != None:
            donations = list(filter(lambda x: x <= maxi, donations))

        new_dons = list(map(lambda x: x*factor, donations))
        if total == True:
            if new_dons:
                new_dons = reduce(lambda x, y: x+y, new_dons)
        ret_db[name] = new_dons

    return ret_db


def name_amount_veri():
    """A function that goes through various input validation loops to ensure
    user input will run through the funcion. 'q' will quit back to the main
    menu."""
    print("")
    name_prompt = ("Please enter a full name to send to or enter"
                   " 'list' for a full list of donors('q' to quit"
                   " to menu): ")
    name = input(name_prompt)
    if name == 'q':
        return 0, 0
    # If list is chosen, print a list of donors and reprompt for a
    #  name, 'q' # to quit to main menu
    while name == 'list':
        for donor in donors:
            print(donor)
        name = input(name_prompt)
    if name == 'q':
        return 0, 0
    # Once name is input, prompt for a donation amount, 'q' to quit
    amount = input(
        "Please enter the amount that was donated('q' to quit"
        " to menu): ")
    if amount == 'q':
        return 0, 0
    while True:
        try:
            amount = float(amount)
        except ValueError:
            amount = input(
                "Invalid. Please enter the amount that was donated: ")
            continue
        break
    return name, amount


def get_factor():
    """A function to prompt user for factor value."""
    factor_prompt = ("Please enter a factor to multiply by: ")
    num = input(factor_prompt)
    while num.isnumeric() == False:
        num = input("Invalid. " + factor_prompt)
    return int(num)


def get_bounds():
    """A function to prompt user for minimum and maximum bounds."""
    mini = input("Would you like a minimum(y/n): ")
    while mini.lower() != 'y' and mini.lower() != 'n':
        mini = input("Invalid. Would you like a minimum(y/n): ")
    if mini.lower() == 'y':
        mini_val = input("Please enter a minimum: ")
        while mini_val.isnumeric == False:
            mini_val = input("Invalid. Please enter a minimum: ")
        mini_val = float(mini_val)
    else:
        mini_val = None

    maxi = input("Would you like a maximum(y/n): ")
    while maxi.lower() != 'y' and maxi.lower() != 'n':
        maxi = input("Invalid. Would you like a maximum(y/n): ")
    if maxi.lower() == 'y':
        maxi_val = input("Please enter a maximum: ")
        while maxi_val.isnumeric == False:
            maxi_val = input("Invalid. Please enter a maximum: ")
        maxi_val = float(maxi_val)
    else:
        maxi_val = None

    return mini_val, maxi_val


def menu():
    """A function to store the menu prompt. Called first in __main__"""
    print("""\nHello User! What would you like to do?
1) Send a Thank You card
2) Create a report of donors
3) Send a Thank You to everyone
4) Multiply the Donor Database
5) Project the Donor Database
6) Quit \n""")


def menu_exit():
    """A function to return an exit prompt to the dictionary switch
    in __main__."""
    return "exit menu"


if __name__ == '__main__':
    """This area is always exectued by the script. It contains the main menu
    prompt as well as the calls to the previous two functions depending on which
    option was chosen. The third option allows the user to quit the script."""
    response = ''
    function_dict = {'1': send_thank_you,
                     '2': create_report,
                     '3': send_all,
                     '4': challenge,
                     '5': challenge,
                     '6': menu_exit}
    # Prompt menu and repeat until the "Quit" option has been chosen
    while True:
        menu()
        prompt = ("Please input a numerical value for"
                  " what you would like to do: ")
        response = input(prompt)
        while response not in ('1', '2', '3', '4', '5', '6'):
            response = input("Invalid input. " + prompt)

        # Once response has been verified and is not 3 to quit, call the
        # appropriate function
        if response == '1':
            name, amount = name_amount_veri()
            if name == 0:
                continue
            # Call the send Thank You latter function passing user input
            function_dict[response](name, amount)
        elif response == '4':
            factor = get_factor()
            mini, maxi = get_bounds()
            new_donors = function_dict[response](factor, mini, maxi)
            print(new_donors)
        elif response == '5':
            factor = get_factor()
            mini, maxi = get_bounds()
            new_donors = function_dict[response](
                factor, mini, maxi, total=True)
            print(new_donors)
        elif function_dict[response]() == 'exit menu':
            break
