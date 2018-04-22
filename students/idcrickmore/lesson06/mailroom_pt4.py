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
    # try exception handling here
    #options.get(choice, menu)()
    try:
        options(choice)
    except KeyError:
        menu()


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
            print("\nMUST ENTER A NUMBER")
            thankyou()
        else:
            name_check = name_check.title()
            # check to see if 'name_check' is in the donor dict...
            # if it is, append it
            try:
                donors[name_check].append(donation)
            except KeyError:
                # if 'name_check' isn't in the donor dict...
                # set  the default format value as a list ([]) and append it
                donors.setdefault((name_check), []).append(donation)
            finally:
                letter_dict = {"name": name_check, "don": donation}
                print("""\n------------------ Letter ------------------\n
Dear {name},

You rock. Your fat contribution of ${don:,.2f}
will go a long way to lining my pockets.

Sincerely,
Scrooge McDuck""".format(**letter_dict))

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
Scrooge McDuck""".format(**letter_dict)
        with open(str(name) + "_" + str(datetime.date.today()) +
                  '.txt', 'w') as out_file:
            out_file.write(letter)

    menu()


def donor_list():
    # lists all the donors
    # calls the 'thankyou' function at the end to ask for user input
    donor_list_string ="\n------------------ DONOR LIST ------------------\n\n"

    for name in donors:
        donor_list_string += (str(name) + "\n")

    return donor_list_string


def report():
    report_string = "\n-------------------- REPORT --------------------\n\n"
    
    column = ["Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"]
    donors_report = [[name, sum(donors[name]), len(donors[name]),
                     (sum(donors[name])/len(donors[name]))]
                     for name in donors]

    # and reverses the order from largest to smallest
    donors_report = sorted(donors_report, key=itemgetter(1), reverse=True)
       
    report_string += "{:<15}{:>17}{:>15}{:>10}\n".format(*column)
    report_string += "---------------------------------------------------------------\n"

    # loops through 'donors_report' and
    # dumps all values for 'name' into .format
    for name in donors_report:
        report_string += ('{:<20} ${:>13.2f}{:>12}  ${:>10.2f}\n'.format(*name))
    
    return report_string

    

def ex():
    print("quiting...")
    
    
#code here 'print_func' takes one arguemnt
#uses argument to call the right function
def print_func(func):
    print(func())
    menu()


donors = {
          "Galileo Galilei": [348, 8377, 123],
          "Giovanni Cassini": [209],
          "Christiaan Huygens": [9135, 39],
          "Edmond Halley": [399, 1100, 357],
          "Edwin Hubble": [1899]
          }


#code here options should call the 'print_func' function with
#the right argment for it to call the correct function
options = {
           '1': thankyou, 's': thankyou,
           '2': letters, 'e': letters,
           '3': print_func, 'c': print_func,
           '4': ex, 'q': ex,
           'list': donor_list,
           'menu': menu
           }

if __name__ == '__main__':
    menu()
