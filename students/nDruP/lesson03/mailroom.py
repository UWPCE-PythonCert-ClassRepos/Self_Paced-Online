#!/usr/bin/env python3
"""
1. Create Data structure that holds Donor, Donation Amount.
2. Prompt user to Send a Thank You, Create a Report, or quit.
3. At any point, the user should be able to quit their current task and return
to the original prompt
4. From the original prompt, the user should be able to quit the scipt cleanly
"""


import sys

donor_list = [["Sleve McDichael", [86457.89, 2346.43, 9099.09]],
              ["Willie Dustice", [505.05, 43.21]],
              ["Rey McScriff", [666.00]],
              ["Mike Truk", [70935.30, 12546.70, 312.00]],
              ["Bobson Dugnutt", [1234.56, 789.00]],
              ["Todd Bonzalez", [715867.83, 10352.07]]]

name_list = []
for x in range(len(donor_list)):
    name_list.append(donor_list[x][0])
    

def send_thanks():
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
    print_divider()
    print("Let's craft a very personal thank you note for our donor!")
    print("You can return to the main menu at any time by entering 'exit'")
    while donor_name == "list":
        donor_name = input("Enter Donor Name >")
        if donor_name.lower() == "list":
            print(donor_list)
        elif donor_name.lower() == "exit":
            return
    while !donation_amt:
        donation_amt = input("Enter their Donation Amount >")
        if donation_amt.lower() == "exit":
            return
    donation_amt = float(donation_amt)
    if donor_name not in name_list:
        donor_list.append([donor_name, [donation_amt]])
    else:
        donor_list[donor_name.index(donor_name)][1].append(donation_amt)
    return


def create_report():
    """
    Print a list of donors sorted by total historical donation amount.
    Donor Name, Total Given, Num Gifts, Average Gift
    """
    return


def print_divider():
    print("\n"+"*"*50+"\n")


def main_menu():
    user_prompt = None
    valid_prompts = ["1", "2", "3"]
    print_divider()
    print("Welcome to the e-mailroom of We're a Pyramid Scheme.")
    print_divider()
    while user_prompt not in valid_prompts:
        print("Please choose from the following options (1,2,3): ")
        print("1. Send a Thank you")
        print("2. Create Donor Report")
        print("3. Quit")
        user_prompt = input(">")
        if user_prompt == "1":
            send_thanks()
        elif user_prompt == "2":
            create_report()
        elif user_prompt == "3":
            break
    sys.exit()
            
        
        
