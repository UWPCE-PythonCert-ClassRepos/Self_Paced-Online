#!/usr/bin/env python3
"""
1. Create Data structure that holds Donor, Donation Amount.
2. Prompt user to Send a Thank You, Create a Report, or quit.
3. At any point, the user should be able to quit their current task and return
to the original prompt
4. From the original prompt, the user should be able to quit the scipt cleanly
"""


import sys


donor_list = {"Sleve McDichael": [86457.89, 2346.43, 9099.09],
              "Willie Dustice": [505.05, 43.21],
              "Rey McScriff": [666.00],
              "Mike Truk": [70935.30, 12546.70, 312.00],
              "Bobson Dugnutt": [1234.56, 789.00],
              "Todd Bonzalez": [715867.83, 10352.07]}
name_list = [x for x in donor_list]


def main_menu():
    user_prompt = None
    valid_prompts = {"1":send_thanks,
                     "2":create_report,
                     "3":send_all,
                     "4":sys.exit}
    while True:
        print("We're a Pyramid Scheme & So Are You! E-Mailroom")
        print_divider()
        while user_prompt not in valid_prompts:
            print("Please choose from the following options (1,2,3,4): ")
            print("1. Send a Thank you")
            print("2. Create Donor Report")
            print("3. Send letters to everyone")
            print("4. Quit")
            user_prompt = input(">")
        valid_prompts.get(user_prompt)()
        user_prompt = None


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
    while True:
        print("Let's craft a very personal thank you note for our donor!")
        print("Return to the main menu at any time by entering 'exit'")
        print("Pull up a list of donor names by entering 'list'")
        while donor_name == "list":
            donor_name = input("Enter Donor Name >")
            if donor_name.lower() == "list":
                print(("{}\n"*len(name_list)).format(*name_list))
        if donor_name.lower() == "exit":
            break
        donation_amt = input("Enter their Donation Amount >")
        if donation_amt.lower() == "exit":
            break
        donation_amt = float(donation_amt)
        if donor_name not in name_list:
            donor_list[donor_name] = [donation_amt]
        else:
            donor_list[donor_name].append(donation_amt)
        print_divider()
        message = f"Dearest {donor_name},\n"
        message += f"Thank you so much for donation of ${donation_amt:.2f}!\n"
        message += "We will use for something wonderful. Something...\n"
        message += "Fantastic.\n We're going to create a real living Pokemon."
        message += f"\nSincerely,\n We're a Pyramid Scheme & so is {donor_name}"
        print(message)
        print_divider()
        break
    return


def create_report():
    """
    Print a list of donors sorted by total historical donation amount.
    Donor Name, Total Given, Num Gifts, Average Gift
    """
    '''donation_list = sorted(donor_list, key=sum_donations, reverse=True)
    name_col_len = max([len(x) for x in name_list])
    money_col_len = 12
    headers = ["Donor Name", "Total Given", "# of Gifts", "Avg Donation"]
    cols = "{:<" + f"{name_col_len}" + "}\t|{:^" + f"{money_col_len+5}"
    cols += "}|{:^10}|{:^" + f"{money_col_len+5}" + "}"
    cols = cols.format(*headers)
    print(cols)
    print("-"*len(cols))
    for index, donation in donation_list:
        name = name_list[index]
        total = sum(donation)
        num_gift = len(donation)
        average = total/num_gift
        row = f"{name:<{name_col_len}}\t| ${total:>{money_col_len+3}.2f}|"
        row += f"{num_gift:^10d}| ${average:>{money_col_len+3}.2f}"
        print(row)
    '''
    
    return


def send_all():
    return





def print_divider():
    """
    Prints a divider so user has better idea of when they enter a new screen.
    """
    print("\n"+"*"*50+"\n")

main_menu()
