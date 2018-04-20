#!/usr/bin/env python3
# #############################################################################
# Written by: Lily Mayc4t
# Date: 4/14/2018
# FileID: mailroom3.py
#
# Purpose: use comprehension and excepttion
#
# #############################################################################


import collections
from collections import *

names = ["Lily Maycat", "Lulu Lemon", "Marc Jacobs", "Bobbi Brown", "Kate Spade"]
amt   = [i*[5000] for i in range(1,6)]
donors = {name:amout for name, amout in zip(names, amt)}

def quit():
    """Quit the top menu."""
    print ("Quitting this menu now")
    return "quit"


def list_all_donor():
    """List all the current donors in the system """
    print ("\t\tList all donor:")
    for each_dn in donors:
        print ("\t\t", each_dn)


def add_donation(dn_name):
    """Add donor, donation information to the system."""
    print ("\t\tAdd Donation:")
    try: 
        dn_amt = float(input("\t\tEnter Donation Amount for {}: ".format(dn_name)))
    except ValueError:
        print("\t\tWRONG INPUT\n\t\tAmount of Money should be a valid number:")
        return

    if dn_name in donors:
        donors[dn_name].append(dn_amt)
    else:

        donors[dn_name] = [dn_amt]
    print("\n\n\t\tDear{},\n\t\tThanks a lot for your generous donation of ${}. \n\t\tThanks".format(dn_name, dn_amt))


def send_thank():
    """Print out the thank you note for the recent donation."""
    print ("\tSend Thank You")
    ans = input("\n\tEnter Full Name(CaSeSeNsItIvE), List, or quit(to quit) : ")
    while(ans.lower() != 'quit'):
        if ans.lower() == "list":
            list_all_donor()
        else:
            add_donation(ans)
        ans = input(
            "\n\tEnter Full Name(CaSeSeNsItIvE), List, or quit(to quit) : ")


def create_report():
    """Creat the report and print out to terminal. """

    print ("\tCreate Report")
    report = list()
    for dn, dnt in donors.items():
        report.append([dn, sum(dnt), len(dnt), sum(dnt)/len(dnt)])

    sorted_report = sorted(report, key=lambda x: -x[1])

    print("\t{:<40}|{:>14} | {:>12} | {:>14}".format(
        "Donor Name", "Total Give", "Num Gifts", "Average Gift"))
    print("\t" + "_"*40 + " " + "_"*14 + "   " + "_"*12 + "   " + "_"*14)

    for each_dn in sorted_report:
        print("\t{:<37}   ${:>16} {:>12}   ${:>14}".format(
            each_dn[0], each_dn[1], each_dn[2], each_dn[3]))


def send_letters():
    """Creat and sent out thank letter to everyone on the list for their current donation. """
    print("\n\n\tSend Letters")
    for k, v in donors.items():
        fname = k.replace(' ', "_") + ".txt"
        try: 
            with open(fname, 'w') as outfile:
                outfile.write(
                    "Dear {},\n\nThank you for your current generous donations: ${}.\nThis will be put to good use. \n\nThanks".format(k, v[-1]))
                outfile.close()
        except PermissionError:
            print ("Permission denied, can't open file {}".format(fname))


if __name__ == "__main__":
    main_prompt = ("\nSelect Options!!!\n"
                   "1. Send a Thank You \n"
                   "2. Create The ReportType\n"
                   "3. Send letters to everyone\n"
                   "4. Quit >> "
                   )
    
    main_dispatch = {"1": send_thank,
                     "2": create_report,
                     "3": send_letters,
                     "4": quit,
                     }
    print("Dispatch :", main_dispatch)

    while True:
        try: 
            ans = input(main_prompt)
            if main_dispatch[ans]() == "quit":
                break

        except KeyError:
            print ( "Wrong Choice, Retry")

