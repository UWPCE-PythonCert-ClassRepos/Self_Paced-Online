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


def user_input(something = ""):
    """
    Display exit reminder and prompt user for input.
    """
    while not something:
        print(exit_reminder)
        something = input(">")
    return check_not_exit(something) * something


def check_not_exit(check_str):
    """
    Check whether or not given string is "exit"
    """
    return not check_str.lower() == "exit"


def thank_u_str(thank_name, thank_gift):
    """
    Return personalized thank you message.
    """
    return (divider + f"Dearest {thank_name},\n"
            f"\tThank you for donation(s) of ${thank_gift:.2f}!\n"
            "We will use your donation(s) to create real living Pokemon.\n"
            "You now have our eternal loyalty. Use it wisely.\n"
            "Sincerely,\n"
            f"We're a Pyramid Scheme & so is {thank_name}"
            + divider)


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
            print(fstr_keylist())

    while True:
        print("\nEnter Donation Amount:")
        donation_amt_str = user_input()
        if not donation_amt_str:
            return
        donation_amt_float = conv_str_money(donation_amt_str)
        if donation_amt_str != donation_amt_float:
            break

    add_new_donation(donor_name, donation_amt)
    
    print(thank_u_str(donor_name, donation_amt))


def add_new_donation(add_name, add_donation):
    donor_dict[add_name].append(add_donation)


def fstr_keylist(list_dict = donor_dict):
    """
    Format dict_keys into a readable string.
    """
    return ("{}\n"*len(list_dict)).format(*list_dict)


def conv_str_money(conv_str):
    """
    Convert string to a float rounded to the Hundredth.
    If it's unable to convert, return original string.
    """
    try:
        conv_float = round(float(conv_str), 2)
        return conv_float
    except:
        return conv_str


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


def sum_2tuple_by2(idx_set):
    """
    Return sum of 2nd element of 2-element tuple.
    i.e. (a, b) assuming b is a list of numbers should return sum(b)
    """
    return sum(idx_set[1])


def create_letters(write_dir = ""):
    """
    Write a full set of letters to each donor to individual files on disk.
    Go through all donors in donor_dict, generate a thank you letter,
    write to disk as a text file.
    """
    while not os.path.isdir(write_dir):
        print("Enter an existing directory to place the letters.")
        print("Input 'cwd' to use Current Working Directory")
        write_dir = user_input()
        if not write_dir:
            return
        if write_dir.lower() == "cwd":
            write_dir = os.getcwd()
    for donor, donations in donor_dict.items():
        print(write_letter_to_dir(donor, donations, write_dir))
    print("Finished writing the letters")


def write_letter_to_dir(name, gifts, letter_dir=os.getcwd()):
    """
    Write a personalized thank you letter for all the donors.
    Letters will be written to letter_dir.
    """
    curdate = (datetime.datetime.now()).strftime("%Y_%m_%d")
    file_name = name.replace(' ', '_') + "_" + curdate + ".txt"
    file_path = os.path.join(letter_dir, file_name)
    with open(file_path, 'w+') as letter:
        letter.write(thank_u_str(name, sum(gifts)))
    return "Wrote to " + file_path
