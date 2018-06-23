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
    options.get(choice, menu)()


def thankyou():

    print("""\n------------------ THANK YOU ------------------\n
type 'list' to to see a complete list of donors -
type 'menu' at any time to return to the menu""")

    # asks for a name from the user, or for the 'list' prompt
    name_check = input("Enter first and last name of a donor\n\n-> ").lower()

    try:
        options.get(name_check)()
    except TypeError:
        try:
            donation = float(input("What is the donation amount? -> "))
        except ValueError:
            print("\nYou need to enter a number")
            thankyou()
        else:
            name_check = name_check.title()
            try:
                donors[name_check].append(donation)
            except KeyError:
                donors.setdefault((name_check), []).append(donation)
            finally:
                letter_dict = {"name": name_check, "don": donation}
                print("""\n------------------ Letter ------------------\n
Dear {name},

Thank you for your contribution of ${don:,.2f}
It will be put to very good use.

Sincerely,
Vinodh""".format(**letter_dict))

                menu()


def letters():
    print("""\n--------- Exporting Letters to Everyone ---------\n
Thank you letters have been exported to {}""".format(os.getcwd()))

    for name in donors:
        letter_dict = {"donor": name, "donation": donors[name][-1]}
        letter = """Dear {donor},

Your most recent contribution of ${donation:,.2f} to my money vault
is very appreciated. I will spend it freely but wisely.

Sincerely,
Vinodh""".format(**letter_dict)
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
    donors_report = [[name, sum(donors[name]), len(donors[name]),
                     (sum(donors[name])/len(donors[name]))]
                     for name in donors]

    # and reverses the order from largest to smallest
    donors_report = sorted(donors_report, key=itemgetter(1), reverse=True)

    print("{:<15}{:>17}{:>15}{:>10}".format(*column))
    print("---------------------------------------------------------------")

    for name in donors_report:
        print('{:<20} ${:>13.2f}{:>12}  ${:>10.2f}'.format(*name))

    menu()


def quit_program():
    print("exiting the program")


donors = {
        'William Gates, III': [653784.49, 2, 326892.24],
        'Mark Zuckerberg': [16396.10, 3, 5465.37],
        'Jeff Bezos': [877.33, 1, 877.33],
        'Paul Allen': [708.42, 3, 236.14],
        }


options = {
            '1':thankyou,
            '2':letters,
            '3':report,
            '4':quit_program,
            'list': donor_list,
            'menu': menu
          }

if __name__ == '__main__':
    menu()
