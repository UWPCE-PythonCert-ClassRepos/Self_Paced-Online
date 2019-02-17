"""import required modules"""

import numpy as np
import os
import sys

"""

Notes for mail room class testing:

1. Class for individual donor
    a. contains, first name, last name, donation amount
    b. method to append to donations
    c. method to send a thank you
"""

class Donor(object):
    """takes full name and creates donor record
    need a donor and a donation to create a donor record"""
    def __init__(self, fullname, donation):
        if len(fullname.split(" ")) == 1:
            first = "Mr/Ms"
            last = fullname.split(" ")[0]
        elif len(fullname.split(" ")) == 2:
            first, last = fullname.split(" ")
        else:
            first = fullname.split(" ")[0]
            last = fullname.split(" ")[len(fullname.split(" "))-1]
        self.first = first
        self.last = last
        self.fullname = fullname
        self.donation = [donation]

    @property
    def add_donation(self):
        return self.donation
    
    @add_donation.setter
    def add_donation(self, new_donation):
        self.donation.append(new_donation)
    
    @property    
    def thank_you(self):
        """sends thank you for latest donation"""
        newest_donation = self.donation[len(self.donation)-1]        
        thankyou =  f"""\nDear {self.first}, \n\nThank you for your generous donation of ${newest_donation:,.2f}. Thanks to you, we will finally be able to begin construction on the {self.last} Memorial Children's wing at The Dark Place Hospital\n\nYours Truly,\nGarth Marenghi\n"""
        print(thankyou)    
    
    def __repr__(self):
        return "Donor Record: {}, {}".format(self.last, self.first)


"""
2. Class for collection of donors
    a. has list of donors and donotion amounts
    b. method to add donors
    c. method to create report
    d. method to create letters
"""

class DonorGroup(object):
    """Donor group initialized with first Donor class
    Donors are kept in a dictionary created in DonorGroup"""
    def __init__(self, donor=None, file_path=None):
        self.donor_list = [donor.fullname]
        self.donor_dict = {donor.fullname: donor.donation}
        self.file_path = file_path
        
    @property
    def add_donor(self):
        return self.donor_list
    
    @add_donor.setter
    def add_donor(self, new_donor):
        self.donor_list.append(new_donor.fullname)
        self.donor_dict[new_donor.fullname] = new_donor.donation    

    @property
    def create_report(self):
        rows = [(donor, sum(self.donor_dict[donor]),len(self.donor_dict[donor]),np.mean(self.donor_dict[donor])) for donor in self.donor_dict]

        #rows.sort(key = takeSecond, reverse = True)

        print('{:<20s} |{:>15s}|{:>12s} |{:>15s}'.format('Donor Name','Total Given','Num Gifts','Average Gift'))
        for i in ['{:<20s} ${:15,.2f} {:12d} ${:15,.2f}'.format(*row) for row in rows]:
            print(i)

        return "report created"

    @property
    def send_letters(self):
        return self.file_path

    @send_letters.setter
    def send_letters(self, letter_dir):

        self.file_path = letter_dir
        
        try:
            os.chdir(self.file_path)
        except FileNotFoundError:
            print("\nNOT A VALID FILE PATH")

        for donor in self.donor_dict:
            
            letter_text = f"""Dear {donor}, \n\nThank you for your generous donation of ${sum(self.donor_dict[donor]):,.2f}. Thanks to you we will finally be able to begin construction on the children's wing at Dark Place Hospital\n\nYours Truly,\nGarth Marenghi"""

            with open(donor.replace(" ","_").lower() + '_donations.txt', 'w') as donation_letter:
                donation_letter.write(letter_text)   

    def __repr__(self):
        return "Donor Group: {}".format(self.donor_list)

    
"""
SENDING A THANKYOU
If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
    -If the user types ‘list’, show them a list of the donor names and re-prompt--
    -If the user types a name not in the list, add that name to the data structure and use it.--
    -If the user types a name in the list, use it.--
    -Once a name has been selected, prompt for a donation amount.--
    -Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.--
    -Once an amount has been given, add that amount to the donation history of the selected user. -- 
    -Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
    -It is fine (for now) to forget new donors once the script quits running.--
"""
def send_thankyou():
    name = input("Please Enter First and Last Name: ")

    while name == "list":
        print("\n".join([donor for donor in dg.donor_list]))
        name = input("\nPlease Enter First and Last Name: ")

    if name not in dg.donor_list:
        #create new Donor instance        
        new_donation = input("Enter a Donation Amount: ")
        new_donation = float(new_donation)
        #create new Donor object 
        globals()[name.split(" ")[0].lower()] = Donor(name, new_donation) 

        #add new Donor object to DonorGroup
        dg.add_donor = vars()[name.split(" ")[0].lower()]

    else:
        new_donation = input("Enter a Donation Amount: ")
        new_donation = int(new_donation)

        #append new donation of existing object
        globals()[name.split(" ")[0].lower()].add_donation = new_donation

    globals()[name.split(" ")[0].lower()].thank_you

"""
CREATE A REPORT
If the user (you) selected “Create a Report”, print a list of your donors, sorted by total historical donation amount.
Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
After printing this report, return to the original prompt.
At any point, the user should be able to quit their current task and return to the original prompt.
From the original prompt, the user should be able to quit the script cleanly.
"""
def takeSecond(elem):
    return elem[1]

def create_report():
    print(dg.create_report)

"""
Send Letters Function

In this version, add a function (and a menu item to invoke it), that goes through all 
the donors in your donor data structure, generates a thank you letter, and writes it to disk as a text file.
"""
file_path = 'C:\\Users\\Jared\\Documents\\IntroToPython\\Self_Paced-Online\\students\\jared_mulholland\\lesson_4\\donation_letters'

def send_letters():
    file_path = input("\nPlease Enter File Path: ")
    try:
        os.chdir(file_path)
    except FileNotFoundError:
        print("\nNOT A VALID FILE PATH")

    dg.send_letters = file_path   
    
"""
QUIT PROGRAM
"""

def quit_mailroom():
    sys.exit(0)

"""
PROGRAM OVERVIEW
Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:\
-It should have a data structure that holds a list of your donors and a history of the amounts they have donated. 
    This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
-You can store that data structure in the global namespace.
-The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)

"""

jared = Donor("Jared Mulholland", 10000)
chris = Donor("Chris Cornell", 50000)
ben = Donor("Ben Shepard", 4000)
kim = Donor("Kim Thayil", 3400)

dg = DonorGroup(jared)
dg.add_donor = chris
dg.add_donor = ben
dg.add_donor = kim


main_dict = {
            "1": send_thankyou,
            "2": create_report,
            "3": send_letters, 
            "4": quit_mailroom
           }
    
main_prompt = ("\nMain Menu  \n 1. Send a Thank You \n 2. Create a Report \n 3. Send Letters \n 4. Quit \n Please Choose an Option: ")

def mail_room_fun(main_prompt, main_dict):
    while True:        
        response = input(main_prompt)
        print("\n")
        try:
            main_dict.get(response)()
        except TypeError:
            print("PLEASE ENTER NUMBER 1-4")

if __name__ == "__main__":
    mail_room_fun(main_prompt, main_dict)

   


             
    
   



    