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
from donor import Donor
from donor_dict import Donor_Dict


d = Donor_Dict(Donor("Sleve McDichael", [86457.89, 2346.43, 9099.09]),
               Donor("Willie Dustice", [505.05, 43.21]),
               Donor("Rey McScriff", [666.00]),
               Donor("Mike Truk", [70935.30, 12546.70, 312.00]),
               Donor("Bobson Dugnutt", [1234.56, 789.00]),
               Donor("Todd Bonzalez", [715867.83, 10352.07]))
divider = "\n" + "*" * 50 + "\n"

def main_menu(user_prompt = None):
    """
    Prompt user to send a Thank You, Create a report, create letters, or quit.
    """
    valid_prompts = {"1": create_thank_u,
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


def user_input(some_str = ""):
    """
    Display exit reminder and prompt user for input.
    """
    exit_reminder = "Return to the main menu by entering 'exit'"
    while not some_str:
        print(exit_reminder)
        some_str = input(">")
    return check_not_exit(some_str) * some_str


def check_not_exit(check_str):
    """
    Check whether or not given string is "exit"
    """
    return check_str.lower() != "exit"


def input_dir(write_dir=""):
    while not os.path.isdir(write_dir) or write_dir != "":
        print("Enter an existing directory to place the letters.")
        print("Input 'cwd' to use Current Working Directory")
        write_dir = user_input()
        if write_dir.lower() == "cwd":
            write_dir = os.getcwd()


def write_txt_to_dir(f_name, content, wrt_dir=os.getcwd()):
    """
    Write a personalized thank you letter for all the donors.
    Letters will be written to letter_dir.
    """
    curdate = (datetime.datetime.now()).strftime("%Y_%m_%d")
    file_name = f_name.replace(' ', '_') + "_" + curdate + ".txt"
    file_path = os.path.join(wrt_dir, file_name)
    with open(file_path, 'w+') as letter:
        letter.write(content)
    return "Wrote to " + file_path


def conv_str(conv_str, conv_type=int):
    """
    Convert string to an int.
    If it's unable to convert, return original string.
    """
    try:
        conv_yes = conv_type(conv_str)
        return conv_yes
    except:
        return None


def create_thank_u(donor_name = "list"):
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
            print(d.names_str)

    while True:
        print("\nEnter Donation Amount:")
        gift_amt_str = user_input()
        if not gift_amt_str:
            return
        gift_amt_str = conv_str(gift_amt_str, float)
        if gift_amt_str:
            break
        else:
            print("Enter a valid amount")

    d.add_donor(donor_name, donation_amt_float)
    
    print(d.thank_u_str(donor_name))

    while save_to_dir not in ['y', 'n']:
        print("Would you like to save this in a file [y/n]?")
        save_to_dir = input(">")
    if save_to_dir == 'y':
        write_dir = input_dir()
        write_txt_to_dir(donor_name, d.thank_u_str(donor_name))


def sort_report_by(report_sort=None):
    while report_sort not in [0, 1, 2, 3, 4]:
        print("How would you like to sort the report?")
        print("[1] Name Asc.\n[2] # of Gifts Desc.")
        print("[3] Avg Gift Amount Desc.\n[4] Total Gift Amount Desc.")
        print("[0] Unsorted")
        option = user_input()
        if not option:
            return
        report_sort = conv_str(option, int)
        if not report_sort:
            print("Please input 0, 1, 2, 3, or 4")
    return report_sort


def create_report():
    """
    Print a list of donors sorted by total historical donation amount.
    Donor Name, Total Given, Num Gifts, Average Gift
    """
    sort_by = sort_report_by()
    if sort_by == None:
        return
    if sort_by == 0:
        donor_list = d.all_donor_info()
    else
        donor_list = d.sort_all_donor_info(sort_by-1)

    col_name_list = ["Donor Name", "Gifts", "Avg Gift", "Total Given"]

    donor_col = "{:<" + f"{d.col_len[0]}" + "}"
    header_avg_col = "{:>" + f"{d.col_len[2]}" + "}"
    header_sum_col = "{:>" + f"{d.col_len[3]}" + "}"
    row = (donor_col + "\t{:}" + "\t" +header_avg_col + "\t" + header_sum_col)

    report = row.format(*col_name_list)

    sum_col = header_sum_col[:len(header_sum_col)-1] + ".2f}"
    avg_col = header_avg_col[:len(header_avg_col)-1] + ".2f}"
    row = (donor_col + "\t{:}" + "\t" +avg_col + "\t" + sum_col)

    for name, hist, avg_gift, sum_gift in donor_list:
        row_data = [name, len(hist), avg_gift, sum_gift]
        report += "\n" + row.format(*row_data)
    print(report)


def create_letters(write_dir = ""):
    """
    Write a full set of letters to each donor to individual files on disk.
    Go through all donors in donor_dict, generate a thank you letter,
    write to disk as a text file.
    """
    for donor in d:
        print(write_txt_to_dir(d[donor].name, d.thank_u_str(donor), write_dir))
    print("Finished writing the letters")



