# lesson 04 mailroom pt 2
# !/usr/bin/env python3

import os
import datetime
from statistics import mean

# starting list of 5+ donors and 1-3 donations each
donors = {"John Travolta": [5000, 7500],
          "Jane Fonda": [10000, 8000, 6500],
          "Judy Blume": [3000, 3000],
          "Joey Tribbiani": [9000],
          "Jenny Gump": [10300, 13750, 12500]}


def menu():
    ask = input("Please choose an action:\n"
                "1) Send a new thank you\n"
                "2) Create a report\n"
                "3) Send letters to all donors\n"
                "4) Quit\n"
                ">>")
    options = {"1": donor_name, "2": report, "3": letters, "4": quit}
    try:  
        options[ask]()
    except KeyError:
        print("\nThere was an error. Please try again.\n")


def email(name, donation):
    """Print short email to screen"""
    if donation >= (10 ** 6):
        print("\nThe amount entered is too large.")
        donors.pop(name)
    else:
        donors[name].append(donation)
        ty_temp = {"first_last": name, "value": donation}
        print("\nThank you, {first_last}, for supporting The Brave Heart Foundation.\n"
              "Your generous donation of ${value} will make a positive,\n"
              "life-changing impact for teens nationwide.".format(**ty_temp))


def donation_amount(donor):
    """Ask for donor amount"""
    donation = input("\nWhat is the donation amount?\n>>")
    if donation.lower() == "exit":
        print("\nExiting.")
        donors.pop(donor)
    else:
        try:
            donation = int(donation)
        except ValueError:
            print("\nInvalid entry.")
            donors.pop(donor)
        else:
            email(donor, donation)


def donor_name():
    """Ask for donor name and add to list if needed"""
    while True:
        addressee = input("\nTo whom would you like to send a thank you?\n"
                          "'List' will display current donors.\n"
                          "'Exit' will return to main menu.\n"
                          ">>")
        if addressee.lower() == "exit":
            print("\nExiting.\n")
            break
        elif addressee.lower() == "list":
            print(list(donors.keys()))
        elif addressee not in donors:
            donors[addressee] = []
            donation_amount(addressee)
        else:
            donation_amount(addressee)


def report():
    """Print report of donors and donation details"""
    donor_sums = {}
    for d in donors:
        total = sum(donors[d])
        count = len(donors[d])
        average = total/count
        donor_sums[d] = [total, count, average]
    sorted_donor_sums = sorted(donor_sums.items(), key=lambda x: x[1], reverse=True)
    print("\n{:<20} {:<15} {:^12} {:<15}".format("Donor", "Total Given", "Number", "Average Given"))
    for i in range(len(sorted_donor_sums)):
        info = {"donor_name": sorted_donor_sums[i][0],
                "donor_total": sorted_donor_sums[i][1][0],
                "donor_count": sorted_donor_sums[i][1][1],
                "donor_avg": sorted_donor_sums[i][1][2]}
        print("{donor_name:<20} ${donor_total:^15.2f} {donor_count:^12} ${donor_avg:^15.2f}".format(**info))
    print()


def letters():
    """Create txt file in CWD for each donor"""
    current = datetime.datetime.now()
    date = str(current.month) + "_" + str(current.day) + "_" + str(current.year)
    for d in donors:
        letter_temp = {"letter_name": d, "letter_amount": sum(donors[d])}
        letter = ("Dear {letter_name},\n\n"
                  "Thank you for supporting The Brave Heart Foundation.\n"
                  "Your donations totaling ${letter_amount} have made a positive,\n"
                  "life-changing impact for teens nationwide.\n\n"
                  "Blessings,\n"
                  "BHF".format(**letter_temp))
        file_name = d + " " + date + ".txt"
        with open(file_name, "w") as donor_letter:
            donor_letter.write(letter)
    print("\nFiles completed.\n")


def quit():
    print("\nGoodbye.")
    exit()


if __name__ == '__main__':
    while True:
        menu()
