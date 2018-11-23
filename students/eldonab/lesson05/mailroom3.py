#!/usr/bin/env python3
from pathlib import Path
import os
import os.path

#create a list of at least 5 donors.
#updated donors_list from part one using a dictionary
donors = {
"Bill Gates": [50000, 600000],
"Jeff Bezos": [100000, 400, 7000],
"Hannah Smith": [400000, 600000], 
"John Clark": [30000, 40000],
"Andrew Jones": [80000,90000, 1000]
}


def add_or_update_donor(name):
    """Add or update donors and donation amount"""
    try:
        amount = int(input("How much is the new donation amount? "))    
        if name in donors:
            donors[name].append(amount)
        else:
            donors.update({name: [amount]})
        letter(name, amount)
    except ValueError:
        print("Please enter a number as a donation amount")


# Changed the previous version of this function using dict comprehensions:
def show_list():
    """Show existing list of donor names"""
    {print(donor) for donor in donors}

 
def letter(donor_name, donor_amount):
    """Print a thank you letter"""
    print("Dear {0}, thank you for your generous donation in the amount of ${1}!".format(donor_name, donor_amount))


def thank_you_note():
    """Send a thank you note and update the list of donors"""
    try:
        name = input("Please, type the full name of a sponsor: ")
        while name == "list":
            show_list()
            name = input("Please, type the full name of a sponsor: ")
        else:
            add_or_update_donor(name)
    except ValueError:
        print("Your answer should be a string")

        
# stat_donors() function written with dict comprehensions:
def stat_donors():
    """Print donation statistics for each donor"""
    donor_dict = {}
    donor_dict = {k:[sum(v),len(v), sum(v)/len(v)] for k,v in donors.items()}
    sorted_d = sorted(donor_dict.items(), key = lambda x: x[1], reverse = True)
    for adonor in sorted_d:
        print("{:<20} ${:>12,.2f}{:^12} ${:>12,.2f}".format(adonor[0], adonor[1][0], adonor[1][1], adonor[1][2]))

         
def create_report():
    """Print a list of donors sorted by name, total donated amount, number of donation, and average donation amount"""
    print("{0:<20}{1:>12}{2:>12}{3:>15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("--------------------------------------------------------------------------------------------")
    stat_donors()


def quit():
    """exit the running program"""
    exit()


# def letter_to_all():
#     """Write a thank you note to each donor and save it to a disk"""
#     for donor, donation in donors.items():
#         try:
#             directory = str(input("Please specify the directory name for this file: "))
#             filepath = Path("c:/",directory)
#             total_don = sum(donation)
#             with open(f"{filepath}\\{donor}.txt", "w") as f:
#                 f.write("Dear {0},\n\n\tThank you for your very kind donation of ${1}.\n\n\t\t It will be put to very good use.\n\n\t\t\t Sincerely,\n\t\t\t -The Team".format(donor, total_don)) 
#         except FileNotFoundError:
#             print("Please, enter a valid directory name for this file.")


# This is going to be a challenge running this on a Mac. Might need to have a catch here using the os module or the like.
def letter_to_all():
    """Write a thank you note to each donor and save it to a disk"""
    try:
        for donor, donation in donors.items():
            directory = str(input("Please specify the directory name for this file: "))
            filepath = os.path.join(os.sep, directory)
            total_don = sum(donation)
            with open(f"{filepath}\\{donor}.txt", "w") as f:
                f.write("Dear {0},\n\n\tThank you for your very kind donation of ${1}.\n\n\t\t It will be put to very good use.\n\n\t\t\t Sincerely,\n\t\t\t -The Team".format(donor, total_don)) 
    except FileNotFoundError:
        print("Please, enter a valid directory name for this file.")

#creating a dictionary to store user's selections:
dict_select = {
0: thank_you_note,
1: create_report,
2: letter_to_all,
3: quit
   
}


#Running the main interaction in if __name__ == '__main__':


if __name__ == '__main__':
    while True:
        try:
            action = int(input(("Please tell us what you would like to do: 'send a thank you: type 0', 'create a report: type 1', 'send a letter to all donors: type 2' 'quit: type 3' ")))
            dict_select[action]()
        except ValueError:
            print("Please type '0', '1', '2' or '3'")
        except KeyError:
            print("Please type '0', '1', '2', or '3'")
            

    
# Recommend adding an option to quit if user raises error. Otherwise, this is a never ending loop.