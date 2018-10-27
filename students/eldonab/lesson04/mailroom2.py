#!/usr/bin/env python3
from pathlib import Path

#create a list of at least 5 donors.
#updated donors_list from part one using a dictionary
donors_list = {
"Bill Gates": [50000, 600000],
"Jeff Bezos": [100000, 400, 7000],
"Hannah Smith": [400000, 600000], 
"John Clark": [30000, 40000],
"Andrew Jones": [80000,90000, 1000]
}

#updated all functions using dictionary methods:

def add_donation_to_list(res_name):
    """Add a new donation amount to an existing donor's name."""
    amount = float(input("How much is the new donation amount? "))
    for donor in donors_list:
        if res_name in donor:
            donors_list[donor].append(amount)
            letter(res_name, amount)


def show_list():
    """Show existing list of donor names"""
    for donor in donors_list:
        print(donor)




def add_new_donor(new_donor):
    """Add a new donor name and donation amount."""
    amount = float(input("How much is the new donation amount? "))
    donors_list.update({new_donor: [amount]})
    letter(new_donor, amount)
   


def is_in_list(donor_name):
    """Check whether donor already exists in the list of donors."""
    for donor in donors_list:
        if donor_name in donor:
            return True


def letter(donor_name, donor_amount):
    """Print a thank you letter"""
    print("Dear {0}, thank you for your generous donation in the amount of ${1}!".format(donor_name, donor_amount))




def thank_you_note():
    """Send a thank you note and update the list of donors"""
    name = input("Please, type the full name of a sponsor: ")
    while name == "list":
        show_list()
        name = input("Please, type the full name of a sponsor: ")
    else:
        if is_in_list(name):
            add_donation_to_list(name)
        else:
            add_new_donor(name)
  
        



def stat_donors():
    """Print donation statistics for each donor"""
    for donor in donors_list:
        a_donor = donor
        total_don = sum(donors_list[donor])
        number_of_don = len(donors_list[donor])
        average_don = total_don//number_of_don
        print("{:<20} ${:>12,.2f}{:^12} ${:>12,.2f}".format(a_donor, total_don, number_of_don, average_don))



          
def create_report():
    """Print a list of donors sorted by name, total donated amount, number of donation, and average donation amount"""
    print("{0:<20}{1:>12}{2:>12}{3:>15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("--------------------------------------------------------------------------------------------")
    stat_donors()


def quit():
    """exit the running program"""
    exit()



def letter_to_all():
    """Write a thank you note to each donor and save it to a disk"""
    for donor, donation in donors_list.items():
        directory = str(input("Please specify the directory name for this file: "))
        filepath = Path("c:/",directory)
        total_don = sum(donation)
        with open(f"{filepath}\\{donor}.txt", "w") as f:
            f.write("Dear {0},\n\n\tThank you for your very kind donation of ${1}.\n\n\t\t It will be put to very good use.\n\n\t\t\t Sincerely,\n\t\t\t -The Team".format(donor, total_don)) 



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
        action = int(input(("Please tell us what you would like to do: 'send a thank you: type 0', 'create a report: type 1', 'send a letter to all donors: type 2' 'quit: type 3' ")))
        dict_select[action]()

    
