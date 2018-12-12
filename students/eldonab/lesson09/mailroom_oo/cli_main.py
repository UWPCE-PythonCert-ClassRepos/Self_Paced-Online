#!/usr/bin/python
from donor_models import *
import os
import os.path


Bill = Donor("Bill Gates", [500, 6000])
Jeff = Donor("Jeff Bezos", [10000, 400])
Hannah = Donor("Hannah Smith", [40000, 60000])
John = Donor("John Clark", [3000, 4000])
Andrew = Donor("Andrew Jones", [8000, 9000, 100])


donors = DonorCollection(Bill, Jeff, Hannah, John, Andrew)


def thank_you_note():
    """Send a thank you note and update the list of donors"""
    name = input("Please, type the full name of a sponsor: ")
    while name == "list":
        donors.list()
        name = input("Please, type the full name of a sponsor: ")
    while name.isnumeric():
        name = input("Please, type the full name of a sponsor. Your input should be a string: ")
    amount = int(input("How much would you like to donate? "))
    if donors.is__in_list(name):
        donors.add_donation_to_list(name, amount)
    else:
        donors.add_new_donor(name, amount)


def letter_to_all():
    """Write a thank you note to each donor and save it to a disk"""
    for donor in donors.collection:
        # print(donor)
        directory = str(input("Please specify the directory name for this file: "))
        filepath = os.path.join(os.sep, directory)
        total_don = donor.total_donations
        with open(f"{filepath}\\{donor.name}.txt", "w") as f:
            f.write("Dear {0},\n\n\tThank you for your very kind donation of ${1}.\n\n\t\t It will be put to very good use.\n\n\t\t\t Sincerely,\n\t\t\t -The Team".format(donor.name, total_don)) 
     

def quit():
    """exit the running program"""
    exit()

    
dict_select = {
1: thank_you_note,
2: donors.create_report,
3: letter_to_all,
4: quit
}


if __name__ == '__main__':
    while True:
        action = int(input(("Please tell us what you would like to do: 'send a thank you: type 1', 'create a report: type 2', 'send a letter to all donors: type 3', 'quit: type 4' ")))
        dict_select[action]()
    

       

    

    




