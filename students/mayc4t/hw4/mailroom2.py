#!/usr/bin/env python3
# #############################################################################
# Written by: Lily Mayc4t
# Date: 4/1/2018
# FileID: mailroom2.py
#
# #############################################################################


import collections
from collections import *


donors = defaultdict(list, {"Lily Maycat": [20],
                            "Lulu Lemon": [15, 15, 15],
                            "Marc Jacobs": [30, 30],
                            "Kate Spade": [60, 60, 60],
                            "Bobbi Brown": [44]
                            })


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
    dn_amt = int(input("\t\tEnter Donation Amount for {}: ".format(dn_name)))
    if dn_name in donors:
        donors[dn_name].append(dn_amt)
    else:
        donors[dn_name] = [dn_amt]
    print("\n\n\t\tDear{},\n\t\tThanks a lot for your generous donation of ${}. \n\t\tThanks".format(
        dn_name, dn_amt))


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
        with open(fname, 'w') as outfile:
            outfile.write(
                "Dear {},\n\nThank you for your current generous donations: ${}.\nThis will be put to good use. \n\nThanks".format(k, v[-1]))
            outfile.close()


def menu_selection(prompt, dispatch_dict):
    print("Dispatch :", dispatch_dict)
    while True:
        ans = input(prompt)
        if dispatch_dict[ans]() == "quit":
            break


# note to myself:
# can I do the sub menu ... with the input will be a name ?
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


if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)
