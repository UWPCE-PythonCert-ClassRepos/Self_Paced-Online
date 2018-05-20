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


d = Donor_Dict.from_file("dict_init.txt")
divider = "\n" + "*" * 50 + "\n"


def main_menu(user_prompt=None):
    """
    Prompt user to send a Thank You, Create a report, create letters, or quit.
    """
    valid_prompts = {"1": create_thank_u,
                     "2": create_donor_report,
                     "3": write_letters_to_all,
                     "4": simulate,
                     "5": mr_exit}
    options = list(valid_prompts.keys())
    print(divider + "We're a Pyramid Scheme & So Are You! E-Mailroom" +
          divider)
    while user_prompt not in valid_prompts:
        options_str = ("{}" + (", {}") * (len(options)-1)).format(*options)
        print(f"Please choose from the following options ({options_str}):")
        print("1. Send a Thank you")
        print("2. Create Donor Report")
        print("3. Send letters to everyone")
        print("4. Run Projections")
        print("5. Quit")
        user_prompt = input(">")
        print(divider)
    return valid_prompts.get(user_prompt)


def user_input(some_str=""):
    """
    Display exit reminder and prompt user for input.
    """
    while not some_str:
        print("Return to the main menu by entering 'exit'")
        some_str = input(">")
    return check_not_exit(some_str) * some_str


def check_not_exit(check_str):
    """
    Check whether or not given string is "exit"
    """
    return check_str.lower() != "exit"


def input_dir(write_dir=""):
    """
    Prompt user for a valid path to directory.
    """
    while True:
        print("Enter an existing directory to write to.")
        print("Input 'cwd' to use Current Working Directory")
        write_dir = user_input()
        if write_dir.lower() == "cwd":
            write_dir = os.getcwd()
        if os.path.isdir(write_dir) or not write_dir:
            break
    return write_dir


def save_to_dir(save_name, save_text):
    """
    Prompt user for choice to save previously printed text to drive.
    """
    save_txt = " "
    while save_txt not in ['y', 'n', '']:
        print("Would you like to save previously displayed text"
              " to a file [y/n]?")
        save_txt = user_input()
    if save_txt == 'y':
        write_dir = input_dir()
        if write_dir:
            return write_txt_to_dir(save_name, save_text, write_dir)
    return ""


def write_txt_to_dir(f_name, content, wrt_dir=os.getcwd()):
    """
    Write a personalized thank you letter for all the donors.
    Letters will be written to letter_dir.
    """
    curdate = (datetime.datetime.now()).strftime("%Y_%m_%d")
    file_name = f_name.replace(' ', '_') + "_" + curdate + ".txt"
    file_path = os.path.join(wrt_dir, file_name)
    with open(file_path, 'w+') as text:
        text.write(content)
    return "Wrote to " + file_path


def conv_str(conv_str, conv_type=int):
    """
    Convert string to given conv_type.
    If it's unable to convert, return original string.
    """
    try:
        conv_yes = conv_type(conv_str)
        return conv_yes
    except ValueError:
        return None


def input_donor_name(donor_name="list", *arg):
    """
    Prompt user for donor name
    Prompt->"list": show a list of the donor names
    """
    while donor_name.lower() == "list":
        print("Enter Name (Pull up the list of donors by entering 'list')")
        donor_name = user_input()
        if donor_name.lower() == "list":
            print('\n' + d.names_str('\n', *arg) + '\n')
    return donor_name


def input_challenge_name(d_dict=d):
    """
    Prompt user for existing names in dict or 'all'.
    """
    donor_list = []
    while True:
        more_donors = None
        challenge_donor = None
        while challenge_donor not in (d_dict.names + ["", "all"]):
            print("Which donor would like to alter their donations?")
            print("Enter 'all' to alter all donors' donations")
            challenge_donor = input_donor_name("list", *donor_list)
        if challenge_donor:
            if challenge_donor == "all":
                donor_list = d_dict.names
                break
            else:
                donor_list.append(challenge_donor)
                while more_donors not in ['y', 'n', '']:
                    print("Would another donor like to alter their" +
                          " donations?[y/n]")
                    more_donors = user_input().lower()
                if more_donors == 'y':
                    continue
        break
    if challenge_donor == "" or more_donors == "":
        return False
    return donor_list


def input_donor_float(d_amt=0):
    """
    Prompt user for valid float
    If input cannot be converted to float, prompt again.
    """
    while True:
        d_amt = user_input()
        if d_amt:
            d_amt = conv_str(d_amt, float)
        if d_amt is not None:
            break
        print("Enter a valid amount")
    return d_amt


def create_thank_u():
    """
    Compose and print a thank you letter to the donor for their donation.
    Return to main
    """
    print(divider)
    print("Let's craft a very personal thank you note for our donor!")
    print(divider)

    d_name = input_donor_name()
    if d_name:
        print("\nEnter a Donation Amount:")
        gift_amt = input_donor_float()
        if gift_amt != "":
            d.add_donor(d_name, gift_amt)
            thanks = d[d_name.lower()].thank_u_letter_str(1)
            print(thanks)
            print(save_to_dir(d_name, thanks))
    return


def sort_report_by():
    """
    Prompt user to determine how to display donor report.
    """
    report_sort = None
    while report_sort not in ['1', '2', '3', '4', '5']:
        print(divider)
        print("How would you like to sort the report?")
        print("[1] Name Asc.\n[2] # of Gifts Desc.")
        print("[3] Avg Gift Amount Desc.\n[4] Total Gift Amount Desc.")
        print("[5] Unsorted")
        report_sort = user_input()
        if not report_sort:
            return False
    return int(report_sort)


def create_donor_report(d_dict=d, rep_name="donor_report"):
    """
    Print a list of donors sorted by method chosen in sort_report_by.
    Donor Name, Num Gifts, Average Gift, Total Given
    """
    sort_by = sort_report_by()
    if sort_by:
        report = d_dict.donor_report(sort_by)
        print(divider + report + divider)
        print(save_to_dir(rep_name, report))
    return


def write_letters_to_all():
    """
    Write a full set of letters to each donor to individual files on disk.
    Go through all donors in donor_dict, generate a thank you letter,
    write to disk as a text file.
    """
    write_dir = input_dir()
    if write_dir:
        for donor in d.keys:
            print(write_txt_to_dir(d[donor].name,
                                   d[donor].thank_u_letter_str(),
                                   write_dir))
        print("Finished writing the letters")
    return


def simulate(d_dict=d):
    """
    Display Donor Report altered by user's specifications.
    """
    donor_list = input_challenge_name()
    if donor_list:
        print("Input a factor to multiply contributions by.")
        fctr = input_donor_float()
        if fctr != "":
            print("Input a min donation such that all donations above" +
                  " this amount will be altered.")
            print("Enter -1 for default value")
            min_g = input_donor_float()
            if min_g != "":
                print("Input a max donation such that all donations below" +
                      " this amount will be altered")
                print("Enter -1 for default value")
                max_g = input_donor_float()
                while max_g < min_g:
                    print("Please enter a valid amount")
                    max_g = input_donor_float()
                if max_g != "":
                    sim_d = d_dict.challenge(fctr, min_g, max_g, *donor_list)
                    create_donor_report(sim_d, "projected_report")
    return


def mr_exit():
    """
    Prompt user to save donor dict before exiting program.
    """
    print("Before exiting would you like to save the donor info?[y/n]")
    save_confirm = ""
    while save_confirm not in ['y', 'n']:
        save_confirm = input('>').lower()
    if save_confirm == 'y':
        print(write_txt_to_dir("dict_init", d.dict_to_txt(), os.getcwd()))
    sys.exit()
