#!/usr/bin/env python3
"""
1. Create Data structure that holds Donor, Donation Amount.
2. Prompt user to Send a Thank You, Create a Report, or quit.
3. At any point, the user should be able to quit their current task and return
to the original prompt
4. From the original prompt, the user should be able to quit the scipt cleanly
"""


import sys
import os
import datetime
from collections import defaultdict


donor_dict = defaultdict(list)
donor_list = [["Sleve McDichael", [86457.89, 2346.43, 9099.09]],
              ["Willie Dustice", [505.05, 43.21]],
              ["Rey McScriff", [666.00]],
              ["Mike Truk", [70935.30, 12546.70, 312.00]],
              ["Bobson Dugnutt", [1234.56, 789.00]],
              ["Todd Bonzalez", [715867.83, 10352.07]]]
for name, money in donor_list:
    donor_dict[name] = money
exit_reminder = "Return to the main menu at any time by entering 'exit'"


def main_menu():
    """
    Prompt user to send a Thank You, Create a report, create letters, or quit.
    """
    user_prompt = None
    valid_prompts = {"1": craft_thank_u,
                     "2": create_report,
                     "3": create_letters,
                     "4": sys.exit}
    options = list(valid_prompts.keys())
    while True:
        print_divider()
        print("We're a Pyramid Scheme & So Are You! E-Mailroom")
        print_divider()
        while user_prompt not in valid_prompts:
            options_str = ("{}" + (", {}") * (len(options)-1)).format(*options)
            print(f"Please choose from the following options ({options_str}):")
            print("1. Send a Thank you")
            print("2. Create Donor Report")
            print("3. Send letters to everyone")
            print("4. Quit")
            user_prompt = input(">")
        print_divider()
        valid_prompts.get(user_prompt)()
        input("\nPress enter to continue...")
        user_prompt = None


def craft_thank_u():
    """
    Prompt for a full name.
    Prompt->"list": show a list of the donor names
    Prompt->name not in list: add name to list;
    Then prompt for donation amount, add amount to donation history
    Compose and print an email thanking the donor for their donation.
    Return to main
    """
    donor_name = "list"
    donation_amt = None
    message = ''
    while True:
        print("Let's craft a very personal thank you note for our donor!")
        print(exit_reminder)

        print("Pull up a list of donor names by entering 'list'")
        while donor_name == "list":
            donor_name = input("Enter Donor Name >")
            if donor_name.lower() == "list":
                print(("{}\n"*len(donor_dict)).format(*donor_dict))
        check_exit(donor_name)

        while True:
            donation_amt = input("Enter their Donation Amount >")
            check_exit(donation_amt)
            try:
                donation_amt = round(float(donation_amt), 2)
                break
            except ValueError:
                print("Invalid input")

        donor_dict[donor_name].append(donation_amt)
        print_divider()
        message = (f"Dearest {donor_name},\n"
                   f"Thank you so much for donation of ${donation_amt:.2f}!\n"
                   "We will use your donation to create real living Pokemon.\n"
                   "Sincerely,\n"
                   f"We're a Pyramid Scheme & so is {donor_name}")
        print(message)
        print_divider()

        break


def create_report():
    """
    Print a list of donors sorted by total historical donation amount.
    Donor Name, Total Given, Num Gifts, Average Gift
    """
    sort_donors = sorted(donor_dict.items(), key=sum_2tuple_by2, reverse=True)
    col_name_list = ["Donor Name", "Total Given", "Gifts", "Avg Donation"]
    billi_len = 12
    donor_col_len = max([len(name) for name, _ in sort_donors])
    donor_col = "{:<" + f"{donor_col_len}" + "}"
    money_col = "{:>" + f"{billi_len}" + "}"

    header_row = donor_col + "\t" + money_col + "\t{:}" + "\t" + money_col
    print(header_row.format(*col_name_list))
    money_col = money_col[:len(money_col)-1] + ".2f}"

    for name, donations in sort_donors:
        row = donor_col.format(name)
        row += "\t$ " + money_col.format(sum(donations))
        row += f"\t {len(donations):>}"
        row += "\t$ " + money_col.format(sum(donations)/len(donations))
        print(row)


def create_letters():
    """
    Write a full set of letters to each donor to individual files on disk.
    Go through all donors in donor_dict, generate a thank you letter,
    write to disk as a text file.
    """
    while True:
        curdate = (datetime.datetime.now()).strftime("%Y_%m_%d")
        print("Enter an existing directory to place the letters.")
        print("Current working directory will be used if input is invalid")
        print(exit_reminder)
        write_dir = input(">")
        check_exit(write_dir)
        if not os.path.isdir(write_dir):
            write_dir = os.getcwd()
        for donor, donations in donor_dict.items():
            thank_you = (f"Dear {donor},\n"
                         "We are so grateful for your lifetime generosity of "
                         f"${sum(donations):.2f}!\n"
                         "You now have our eternal loyalty. Use it wisely.\n"
                         "Sincerely,\n"
                         f"We're a pyramid scheme and so is {donor}")
            file_name = donor.replace(' ', '_') + "_" + curdate + ".txt"
            with open(os.path.join(write_dir, file_name), 'w+') as letter:
                letter.write(thank_you)
        print("Finished writing the letters")
        break


def sum_2tuple_by2(idx_set):
    """
    Returns sum of 2nd element of 2-element tuple.
    Used in create_report()
    """
    return sum(idx_set[1])


def print_divider():
    """
    Prints a divider so user has better idea of when they enter a new screen.
    """
    print("\n"+"*"*50+"\n")


def check_exit(user_input):
    """
    Check if user_input is exit. If true, brings them back to main menu.
    """
    if user_input.lower() == "exit":
        main_menu()


main_menu()
