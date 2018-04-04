#!/usr/bin/env python3
from operator import itemgetter
import os
import datetime


def menu():

    print("""\n------------------ MENU ------------------\n
PLEASE CHOOSE FROM THE FOLLOWING THREE OPTIONS
1. Send Thank You
2. Export Letters to Everyone
3. Create a Report
4. Quit\n""")

    choice = input("-> ").lower()[0]

    # use .get() on the 'options' dict to call functions
    # keep calling the 'menu' function if user input not in dict
    options.get(choice, menu)()


def thankyou():

    print("""\n------------------ THANK YOU ------------------\n
type 'list' to to see a complete list of donors -
type 'menu' at any time to return to the menu""")

    # asks for a name from the user, or for the 'list' prompt
    name_check = input("Enter first and last name of a donor\n\n-> ").lower()

    if name_check not in options:

        donation = float(input("What is the donation amount? -> "))

        name_check = name_check.title()

        # check to see if 'name_check' is in the donor dict...
        # if it is, append it
        if name_check in donors:
            donors[name_check].append(donation)

        # if 'name_check' isn't in the donor dict...
        # set  the default format value as a list ([]) and append it
        else:
            donors.setdefault((name_check), []).append(donation)

        letter_dict = {"name": name_check, "don": donation}

        print("""\n------------------ Letter ------------------\n
Dear {name},

You rock. Your fat contribution of ${don:,.2f}
will go a long way to lining my pockets.

Sincerely,
Scrooge McDuck""".format(**letter_dict))

    options.get(name_check, menu)()


def letters():
    print("""\n--------- Exporting Letters to Everyone ---------\n
Thank you letters have been exported to {}""".format(os.getcwd()))

    for name in donors:
        letter_dict = {"donor": name, "donation": donors[name][-1]}
        letter = """Dear {donor},

Your most recent contribution of ${donation:,.2f} to my money vault
is very appreciated. I will spend it freely but wisely.

Sincerely,
Scrooge McDuck""".format(**letter_dict)
        with open(str(name) + "_" + str(datetime.date.today()) +
                  '.txt', 'w') as out_file:
            out_file.write(letter)

    menu()


def donor_list():
    # lists all the donors
    # calls the 'thankyou' function at the end to ask for user input
    print("\n------------------ DONOR LIST ------------------\n")

    for name in donors:
        print(name)

    thankyou()


def report():
    print("\n-------------------- REPORT --------------------\n")

    column = ["Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"]
    donors_report = []

    for name in donors:
        sum_don = sum(donors[name])
        num_don = len(donors[name])
        ave_don = sum_don / num_don
        donors_report.append([name, sum_don, num_don, ave_don])

    # and reverses the order from largest to smallest
    donors_report = sorted(donors_report, key=itemgetter(1), reverse=True)

    print("{:<15}{:>17}{:>15}{:>10}".format(*column))
    print("---------------------------------------------------------------")

    # loops through 'donors_report' and
    # dumps all values for 'name' into .format
    for name in donors_report:
        print('{:<20} ${:>13.2f}{:>12}  ${:>10.2f}'.format(*name))

    menu()


def ex():
    print("quiting...")


donors = {
          "Galileo Galilei": [348, 8377, 123],
          "Giovanni Cassini": [209],
          "Christiaan Huygens": [9135, 39],
          "Edmond Halley": [399, 1100, 357],
          "Edwin Hubble": [1899]
          }


options = {
           '1': thankyou, 's': thankyou,
           '2': letters, 'e': letters,
           '3': report, 'c': report,
           '4': ex, 'q': ex,
           'list': donor_list,
           'menu': menu
           }

if __name__ == '__main__':
    menu()
