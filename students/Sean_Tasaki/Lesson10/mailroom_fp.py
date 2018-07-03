#!/usr/bin/env python3
"""
Sean Tasaki
7/2/2018
Lesson10.mailroom_fp
"""
from collections import defaultdict
from collections import OrderedDict
from operator import itemgetter
import sys
import functools

donor_dict = defaultdict(list, {'Bob Dylan': [2000.00, 500.00, 3.00], 'Italo Calvino': [1001.00, 333.00], 'Feist Scotia': [1500.00, 30.00]})

# Input functions
def main_menu():
    main_menu_dict = {'1': DonorCollection(donor_dict).thank_you, '2': DonorCollection(donor_dict).create_report, '3': DonorCollection(donor_dict).create_thank_you_letters, '4': DonorCollection(donor_dict).match_contributions, '5': quit}
    main_prompt = "Enter 1-4 from the following options: (1) Send a Thank You to a Donor, (2) Create a Report, (3) Write a Thank You Letter to All Donors, (4) Match Contributions, (5) Quit\n >> "  
    main_menu_response(main_prompt, main_menu_dict)

def main_menu_response(prompt, main_menu_dict):
    while True:
        response = input(prompt)
        try:
            if main_menu_dict[response]() == "exit menu":
                sys.exit(0)
        except KeyError:
            print("Enter a number between 1-5.")    

def quit():
    return 'exit menu'

def donor_name_prompt():
    return input('Enter the first and last name of the donor or enter ''list'' to see a list of previous donor names or enter Q to exit to main menu\n> ')          

def donation_prompt():
     return float(input("Please enter the donation amount:\n"))

def projection_prompt():
    return int(input('Enter 0 for an estimate or 1 to match contributions:\n>'))
def factor_prompt():
    return int(input('Enter the factor to match contributions:\n>'))

def min_amount_prompt():
    return float(input('Enter minimum donation amount to match:\n>'))

def max_amount_prompt():
    return float(input('Enter maximum donation amount to match:\n>'))

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
        try:
            self.name = donor_name_prompt()            
            if self.name.lower() == 'list':
                print(self.get_all_donors())
            elif self.name.upper() == 'Q':
                main_menu()
            first, last = self.name.split(' ')
        except ValueError:
            print("Invalid input.")
            self.thank_you()               
        else: 
            success = False
            while not success:   
                try:
                    self.donation = donation_prompt()
                    success = True

                except ValueError:
                    print('Please enter a valid number.')
                    success = False

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
    
    def match_contributions(self, projection = -1):
        while projection not in [0, 1]:
            try:
                projection = projection_prompt()
            except ValueError:
                print('invalid input')
        
        success = False
        while not success or min_amount > max_amount:   
            try:
                factor = factor_prompt()
                min_amount = min_amount_prompt()
                max_amount = max_amount_prompt()
                if min_amount > max_amount:
                    print('The minimum donation amount must be less than the maximum donation amount')   
                else:               
                    success = True

            except ValueError:
                print('Please enter a valid number.')
                success = False
       
        self.challenge(projection, min_amount, max_amount, factor)
        
        main_menu()

    def challenge(self, projection = 0, min = 0, max = 99999999, factor = 1):
        #Multiplies  total donation amount of each donor by factor.
        total = 0
        for donor in self.donor_dict:
            filtered_list1 = list(filter(lambda x: x >= min and x <= max, self.donor_dict[donor]))
            filtered_list2 = list(filter(lambda x: x < min and x > max, self.donor_dict[donor]))
            challenge_list = list(map(lambda x: x * factor, filtered_list1))
            if projection == 1:
                self.donor_dict[donor] = challenge_list + filtered_list2
            else:
                if challenge_list:                      
                    total = total + functools.reduce(lambda x, y: x + y, challenge_list)
                
        if projection == 1:
            print(f"All donations have been multiplied by a factor of {factor}")
            return self.donor_dict  
        else:
            if total == 0:             
                print('There were no donation amounts that fit into the range of minimum and maximum donations. Please re-adjust minimum and maximum donations.')
            else:
                print(f'Total estimated donation: ${total:.2f}')

    
    def create_report(self):     

        print("Donor Name           |   Total Given   |   Num Gifts  |    Average Gift")
        print("-----------------------------------------------------------------------")
        
        for donor in self.sort_donors_by_total_amount():
            print(f"{donor:20} ${sum(self.donor_dict.get(donor)):>17.2f}    {len(self.donor_dict.get(donor)):>6}     ${sum(self.donor_dict.get(donor))/ len(self.donor_dict.get(donor)):>16.2f}")  
        
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


