#!/usr/bin/env python3
from pathlib import Path
import os
import os.path
from functools import reduce

#create a list of at least 5 donors.
donors = {
"Bill Gates": [50, 6],
"Jeff Bezos": [1000, 40, 70],
"Hannah Smith": [40, 6000], 
"John Clark": [30, 400],
"Andrew Jones": [80,90, 10]
}


def add_or_update_donor(name):
    """Add or update donors and donation amount"""
    try:
        amount = int(input("How much is the new donation amount? "))    
        if name in donors:
            donors[name].append(amount)
        else:
            donors.update({name: [amount]})
        letter_print(name, amount)
    except ValueError:
        print("Please enter a number as a donation amount")


def show_list():
    """Show existing list of donor names"""
    {print(donor) for donor in donors}
      

def letter(donor_name, donor_amount):
    """Return a thank you letter."""
    return "Dear {0}, thank you for your generous donation in the amount of ${1}!".format(donor_name, donor_amount)


def letter_print(donor_name, donor_amount):
    """Print a thank you letter"""
    print(letter(donor_name, donor_amount))
   

def thank_you_note():
    """Send a thank you note and update the list of donors"""
    try:
        name = input("Please, type the full name of a sponsor: ")
        while name == "list":
            show_list()
            name = input("Please, type the full name of a sponsor: ")
        while name.isnumeric():
            name = input("Please, type the full name of a sponsor. Your input should be a string: ")
        else:
            add_or_update_donor(name)
    except ValueError:
        print("Your answer should be a string")

        
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
    print("--------------------------------------------------------------")
    stat_donors()


def quit():
    """exit the running program"""
    exit()


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


def challenge(factor, min_donation = 0, max_donation = 100000):
    new_donors = {}
    for k,v in donors.items():
        new_donors.update({k:(list(map(lambda x: x*factor, list(filter(lambda x: x > min_donation and x < max_donation,v)))))})
    return new_donors


def total_projected(factor, min_donation = 0, max_donation = 10000):
    """create a new donors database with projected total donation amounts and print report"""
    projected_donations = {}
    for k, v in donors.items():
        filtered = list(filter(lambda x: x > min_donation and x < max_donation, v))
        mapped = list(map(lambda x: x*factor, filtered))
        if sum(mapped) > 0:
            projected_donations.update({k:(reduce(lambda x,y: x + y, mapped))})
    print("{0:<20}{1:>12}".format("Donor Name", "Total Given"))
    for k, v in projected_donations.items():
        print("{0:<20}{1:12}".format(k, v))

 
def print_projections():
    """Print projected donation amounts"""
    print(f"a: What total contributions would come to if the donors were to double contributions under $100")
    total_projected(2, max_donation = 100)
    print("\n")
    print(f"b: What total contributions would come to if the donors were to triple contributions over $50")
    total_projected(3, min_donation = 50)


#creating a dictionary to store user's selections:

dict_select = {
0: thank_you_note,
1: create_report,
2: letter_to_all,
3: print_projections,
4: quit
   
}


#Running the main interaction in if __name__ == '__main__':
if __name__ == '__main__':
    while True:
        try:
            action = int(input(("Please tell us what you would like to do: 'send a thank you: type 0', 'create a report: type 1', 'send a letter to all donors: type 2','see our projected donations amount': type 3, 'quit: type 4' ")))
            dict_select[action]()
        except ValueError:
            print("Please type '0', '1', '2', '3' or '4'")
        except KeyError:
            print("Please type '0', '1', '2', '3' or '4'")
            

    
