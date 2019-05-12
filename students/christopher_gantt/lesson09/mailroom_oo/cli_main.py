#!/usr/bin/env python3

""" Command Line Interface for Mailroom """

from donor_models import Donor, DonorCollection

WK = Donor("Wassily Kandinsky")
JJ = Donor("Jasper Johns")
MR = Donor("Mark Rothko")
RS = Donor("Richard Serra")
YT = Donor("Yves Tanguy")

WK.add_donation(43928.13)
WK.add_donation(131.34)
WK.add_donation(1928.0)
JJ.add_donation(3134.43)
JJ.add_donation(153.34)
MR.add_donation(135353.33)
RS.add_donation(153757.87)
RS.add_donation(28457.12)
RS.add_donation(1293451.0)
YT.add_donation(1534.23)
YT.add_donation(2542.19)

DONOR_DB = DonorCollection(WK, JJ, MR, RS, YT)

PROMPT = "\n".join(("\nMain Menu",
                    "Type a number from the options below",
                    "1 - Send a Thank You to a single donor",
                    "2 - Create a Report",
                    "3 - Quit\n"))

SUB_PROMPT = "\n".join(("\nThank You",
                        "Type a number from the options below",
                        "1 - View all donor names",
                        "2 - Add donation for current donor",
                        "3 - Add donation for new donor",
                        "4 - Back to main menu\n"))


def menu_selection(prompt, switch_dict):
    while True:
        response = input(prompt)
        try:
            func = switch_dict[response]()
        except KeyError:
            print("Not a valid option")
        else:
            if func == "exit menu":
                break


def exit_menu():
    return "exit menu"


def print_donors():
    print("\n".join(DONOR_DB.generate_name_list()))


def ask_for_name():
    name = input("Type donor name: ").title()
    return name


def ask_for_donation(name):
    try:
        donation = float(input(f"Add a donation amount for {name}: $"))
    except ValueError:
        donation = float(input(f"Please enter a number. Donation Amount: $"))
    return donation  


def donation_and_thank_you(name):
    donation = ask_for_donation(name)
    DONOR_DB.get_donor(name).add_donation(donation)
    print(DONOR_DB.get_donor(name).thank_you_letter())


def current_donor():
    name = ask_for_name()
    if name in DONOR_DB.generate_name_list():
        donation_and_thank_you(name)
    else:
        print("Donor is not in the system.")


def new_donor():
    name = ask_for_name()
    DONOR_DB.add_donor(Donor(name))
    donation_and_thank_you(name)


SWITCH_SUB_PROMPT_DICT = {"1": print_donors,
                          "2": current_donor,
                          "3": new_donor,
                          "4": exit_menu}


def thank_you():
    menu_selection(SUB_PROMPT, SWITCH_SUB_PROMPT_DICT)


def display_report():
    print(DONOR_DB.generate_report())


SWITCH_FUNC_DICT = {"1": thank_you, "2": display_report, "3": exit_menu}


def main():
    print("\nWelcome to The Mailroom")
    menu_selection(PROMPT, SWITCH_FUNC_DICT)


if __name__ == '__main__':
    main()
