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


donor_dict = defaultdict(list,
                         {"Sleve McDichael": [86457.89, 2346.43, 9099.09],
                          "Willie Dustice": [505.05, 43.21],
                          "Rey McScriff": [666.00],
                          "Mike Truk": [70935.30, 12546.70, 312.00],
                          "Bobson Dugnutt": [1234.56, 789.00],
                          "Todd Bonzalez": [715867.83, 10352.07]})
exit_reminder = "Return to the main menu by entering 'exit'"
divider = "\n" + "*" * 50 + "\n"

def main_menu(user_prompt = None):
    """
    Prompt user to send a Thank You, Create a report, create letters, or quit.
    """
    valid_prompts = {"1": craft_thank_u,
                     "2": create_report,
                     "3": create_letters,
                     "4": sys.exit}
    options = list(valid_prompts.keys())
    print(divider + "We're a Pyramid Scheme & So Are You! E-Mailroom"
          + divider)
    while user_prompt not in valid_prompts:
        options_str = ("{}" + (", {}") * (len(options)-1)).format(*options)
        print(f"Please choose from the following options ({options_str}):")
        print("1. Send a Thank you")
        print("2. Create Donor Report")
        print("3. Send letters to everyone")
        print("4. Quit")
        user_prompt = input(">")
        print(divider)
    return valid_prompts.get(user_prompt)


def craft_thank_u(donor_name = "list"):
    """
    Prompt for a full name.
    Prompt->"list": show a list of the donor names
    Prompt->name not in list: add name to list;
    Then prompt for donation amount, add amount to donation history
    Compose and print an email thanking the donor for their donation.
    Return to main
    """
    print(divider)
    print("Let's craft a very personal thank you note for our donor!")

    while donor_name == "list":
        print(divider)
        print("Enter Donor Name:")
        print("Pull up a list of donor names by entering 'list'")
        donor_name = user_input()
        if not donor_name:
            return
        if donor_name.lower() == "list":
            print(divider)
            print(list_of_keys())

    while True:
        print("\nEnter Donation Amount:")
        donation_amt = user_input()
        try:
            donation_amt = round(float(donation_amt), 2)
            break
        except ValueError:
            print("Invalid input")
        except TypeError:
            return

    add_new_donation(donor_name, donation_amt)
    
    print(thank_u_str(donor_name, donation_amt))


def create_report():
    """
    Print a list of donors sorted by total historical donation amount.
    Donor Name, Total Given, Num Gifts, Average Gift
    """
    sort_donors = sorted(donor_dict.items(), key=sum_2tuple_by2, reverse=True)

    col_name_list = ["Donor Name", "Total Given", "Gifts", "Avg Donation"]

    sum_col_len = max(max([len(str(round(sum(donations), 2)))
                   for _, donations in sort_donors]), len(col_name_list[1]))
    avg_col_len = max(max([len(str(round(sum(donations)/len(donations),2)))
                   for _, donations in sort_donors]), len(col_name_list[3]))
    donor_col_len = max([len(name) for name, _ in sort_donors])

    donor_col = "{:<" + f"{donor_col_len}" + "}"
    header_sum_col = "{:>" + f"{sum_col_len}" + "}"
    header_avg_col = "{:>" + f"{avg_col_len}" + "}"
    row = (donor_col + "\t" + header_sum_col + "\t{:}" + "\t" + header_avg_col)

    report = row.format(*col_name_list)

    sum_col = header_sum_col[:len(header_sum_col)-1] + ".2f}"
    avg_col = header_avg_col[:len(header_avg_col)-1] + ".2f}"
    row = (donor_col + "\t$" + sum_col + "\t{:}" + "\t$" + avg_col)

    for name, donations in sort_donors:
        hist_amt = sum(donations)
        num_gifts = len(donations)
        row_data = [name, hist_amt, num_gifts, hist_amt/num_gifts]
        report += "\n" + row.format(*row_data)
    print(report)


def create_letters(write_dir = ""):
    """
    Write a full set of letters to each donor to individual files on disk.
    Go through all donors in donor_dict, generate a thank you letter,
    write to disk as a text file.
    """
    while not os.path.isdir(write_dir):
        print("Enter an existing directory to place the letters.")
        print("Press Enter or input 'cwd' to use Current Working Directory")
        write_dir = user_input()
        if not write_dir:
            return
        if write_dir == '' or write_dir.lower() == "cwd":
            write_dir = os.getcwd()
    for donor, donations in donor_dict.items():
        print(write_letter_to_dir(donor, donations, write_dir))
    print("Finished writing the letters")


def write_letter_to_dir(name, gifts, letter_dir=os.getcwd()):
    curdate = (datetime.datetime.now()).strftime("%Y_%m_%d")
    file_name = name.replace(' ', '_') + "_" + curdate + ".txt"
    file_path = os.path.join(letter_dir, file_name)
    with open(file_path, 'w+') as letter:
        letter.write(thank_u_str(letter_name, sum(gifts)))
    return "Wrote to " + file_path


def sum_2tuple_by2(idx_set):
    """
    Returns sum of 2nd element of 2-element tuple.
    Used in create_report()
    """
    return sum(idx_set[1])


def add_new_donation(add_name, add_donation):
    donor_dict[add_name].append(add_donation)


def thank_u_str(thank_name, thank_gift):
    return (divider + f"Dearest {thank_name},\n"
            f"\tThank you for donation(s) of ${thank_gift:.2f}!\n"
            "We will use your donation(s) to create real living Pokemon.\n"
            "You now have our eternal loyalty. Use it wisely.\n"
            "Sincerely,\n"
            f"We're a Pyramid Scheme & so is {thank_name}"
            + divider)


def user_input(something = ""):
    if not something:
        print(exit_reminder)
        something = input(">")
    return check_not_exit(something) * something


def check_not_exit(check_str):
    return not check_str.lower() == "exit"


def list_of_keys(list_dict = donor_dict):
    return ("{}\n"*len(list_dict)).format(*list_dict)

"""
while True:
    main_menu()()
    print("\nReturning to main menu..........")
    input("Press enter to continue...")
"""
