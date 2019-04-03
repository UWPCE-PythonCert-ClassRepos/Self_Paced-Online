
import sys, os
from mailroom9 import *

def view_donors():
    print("\n".join(donor_db))

def quit_program():
    print ("Thank you. Bye!")
    sys.exit(0)  # exit the interactive script

#function to make sure input name is letters only and longer than 2 characters
def validate_name():
    while (True):
        try:
            input_Name = str(input("Please enter a name > "))
            if ((len(input_Name) > 2 and len(input_Name.split()) > 1)  or input_Name.isalpha()):
            #if (len(input_Name >2)):
                break
            else:
                raise TypeError
        except TypeError:
            print("Letters only or longer name, please.")
    
    return input_Name

#function to make sure input amount is numeric
def validate_amount(input_Name):
    while (True):
        try:
            input_Amount = input(f"{input_Name} please input amount > ")
            value = float(input_Amount)
            if value <= 0:
                raise ValueError
            break
        except ValueError:
            print('Valid amount, please')
    return value

def send_thank_you():

    input_name = validate_name()
    while("list" in input_name):
        for d in sorted(donor_db.keys()):
            print(d)

        input_name = validate_name()

    value = validate_amount(input_name)

    new_donor = Donor(input_name, value)

    if not donor_db.is_donor_exist(new_donor):
        response = input("Donor doesn't exist in database.  Do you want to add to database? >").upper()
        if "Y" in response or "Yes" in response:
            print(new_donor.create_thank_you_note())
            donor_db.add_donor(new_donor)
    else:
            print(new_donor.create_thank_you_note())
            donor_db.add_donor(new_donor)

def get_report():
    return donor_db.prepare_report()

def display_report():
    for r in get_report():
        print(r)

def create_report():
    space=''
    print(f'Donor Name {space:<15}| Total Given {space:<10}| Num Gifts {space:<9}| Average Gift {space:<19}')
    print("-"*85)
    #sort_Donor = sorted(donor_db.items(), key=lambda x: x[1], reverse = True)
    display_report()

def send_letters():
    path = os.getcwd()
    donor_db.send_letters(path)
    print("Done!")

if __name__ == "__main__":
    
    D1 = Donor("William Gates, III", 100.2)
    D2 = Donor("Mark Zuckerberg", 3000.2)
    D3 = Donor("Jeff Bezos", 100000.2)
    D4 = Donor("Paul Allen", 5000.24)
    D5 = Donor("Donald Trump", 50000.24)
    D6 = Donor("Donald Trump", 10000.24)

    #create donor_db from DonorCollection
    donor_db = DonorCollection()
    donor_db.add_donor(D1)
    donor_db.add_donor(D2)
    donor_db.add_donor(D3)
    donor_db.add_donor(D4)
    donor_db.add_donor(D5)
    donor_db.add_donor(D6)

    arg_dict = {'S':send_thank_you, 'C':create_report, 'L':send_letters}

    while True:
        response = input("Please select S for \"Send a Thank You\" C for \"Create a Report\" L for \"Send Letters\" or Q to quit >").upper()
        arg_dict.get(response, quit_program)()