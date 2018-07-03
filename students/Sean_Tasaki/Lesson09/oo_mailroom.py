#!/usr/bin/env python3
"""
Sean Tasaki
6/29/2018
Lesson09.oo_mailroom
"""
from collections import defaultdict
from collections import OrderedDict
from operator import itemgetter
import sys


donor_dict = defaultdict(list, {'Bob Dylan': [2000.00, 500.00, 3.00], 'Italo Calvino': [1001.00, 333.00], 'Feist Scotia': [1500.00, 30.00]})

# Input functions
def main_menu():
    main_menu_dict = {'1': DonorCollection(donor_dict).thank_you, '2': DonorCollection(donor_dict).create_report, '3': DonorCollection(donor_dict).create_thank_you_letters, '4': quit}
    main_prompt = "Enter 1-4 from the following options: (1) Send a Thank You to a Donor, (2) Create a Report, (3) Write a Thank You Letter to All Donors (4) Quit\n >> "  
    main_menu_response(main_prompt, main_menu_dict)

def main_menu_response(prompt, main_menu_dict):
    while True:
        response = input(prompt)
        try:
            if main_menu_dict[response]() == "exit menu":
                sys.exit(0)
        except KeyError:
            print("Enter a number between 1-4.")    

def quit():
    return 'exit menu'

def donor_name_prompt():
    return input('Enter the first and last name of the donor or enter ''list'' to see a list of previous donor names or enter Q to exit to main menu\n> ')          

def donation_prompt():
     return float(input("Please enter the donation amount:\n"))


class Donor:
    def __init__(self, first_name, last_name, donation_lis = []):
        self.first_name = first_name
        self.last_name = last_name
        if donation_lis != []:
            self.donation_lis = donation_lis
        else:
            self.donation_lis = []

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def add_donation(self, amount):
        return self.donation_lis.append(amount)

    @property
    def num_of_donations(self):
        return len(self.donation_lis)

    @property
    def total_donation(self):
        return sum(self.donation_lis)

    @property
    def avg_donation(self):
        return sum(self.donation_lis/ len(self.donation_lis))

    @property
    def d_lis(self):
        return self.donation_lis  

class DonorCollection:
    def __init__(self, donor_dict):
        self.donor_dict = donor_dict
    
    def add_donor(self, donor):
        return self.donor_dict.update({donor.full_name: donor.d_lis})

    #Returns sorted list of all donors
    def get_all_donors(self):
       donor_lis = list(donor_dict.keys())
       return sorted(donor_lis)

    def sort_donors_by_total_amount(self):
        donor_total_amount = {key:sum(value) for key, value in self.donor_dict.items()}
        return OrderedDict(sorted(donor_total_amount.items(), key = itemgetter(1), reverse = True))
    
    def thank_you(self):
        self.name = donor_name_prompt()
        if self.name.lower() == 'list':
            print(self.get_all_donors())
        elif self.name.upper() == 'Q':
            main_menu()
           
        else:
            self.donation = donation_prompt()
            first, last = self.name.split(' ')
            self.donor = Donor(first.title(), last.title(), [self.donation])
            
            if self.donor.full_name not in donor_dict:
                print(f"{self.name.title()} is a new donor.")
                print(self.thank_you_message(self.name, self.donation, 0))
                self.add_donor(self.donor)
            else:
                print(f"{self.name.title()} is a previous donor.\n>> ")          
                print(self.thank_you_message(self.name, self.donation, 1))
                self.donor_dict[f"{first.title()} {last.title()}"].append(self.donation)
        
        main_menu()

    def thank_you_message(self, name, donation, type):
        #New donor message
        if type == 0:
            return f"Thank you {name.title()} for becoming a new donor to our charity! Your genereous donation of ${float(donation):.2f} is much appreciated."
        # previous donor message   
        elif type == 1:
            return f"Thank you {name.title()} for your loyal support to our charity! Your genereous donation of ${float(donation):.2f} is much appreciated."  
    
    def create_report(self):     

        print("Donor Name           |   Total Given   |   Num Gifts  |    Average Gift")
        print("-----------------------------------------------------------------------")
        
        for donor in self.sort_donors_by_total_amount():
            print(f"{donor:20} ${sum(donor_dict.get(donor)):>17.2f}    {len(donor_dict.get(donor)):>6}     ${sum(donor_dict.get(donor))/ len(donor_dict.get(donor)):>16.2f}")  
        
        main_menu()

    def create_thank_you_letters(self):
        # Creates a letter for each donor that gets a file in the working dir based on donor's name.
        try:
            # Separate donors based on whether they gave multiple donations or a single donation
            file_donor_names=  [(donor + '.txt') for donor in donor_dict]
            file_object_for_donations = [open(file, 'w') for file in file_donor_names]
            for count, donor in enumerate(donor_dict):
                file_object_for_donations[count].write(self.thank_you_letter_template(donor)) 
        except IOError:
            print("There was an error with creating the letter files")
        else:
            print("Thank you letters created. Look in the directory for the new files.")
            main_menu()
        finally: 
            for file in file_object_for_donations:
                file.close()

    def thank_you_letter_template(self, dk):
        if len(self.donor_dict.get(dk)) > 1:
            return "Dear {},\nThank you for your {} generous donations of ${:.2f}. Your support helps our charity stay in business.\n\nSincerely,\n-The Team".format(dk, len(self.donor_dict.get(dk)), sum(self.donor_dict.get(dk)))
        else:
            return "Dear {},\nThank you for your generous donation of ${:.2f}. Your support helps our charity stay in business.\n\nSincerely,\n-The Team".format(dk, sum(self.donor_dict.get(dk)))

if __name__ == '__main__':
    main_menu()


