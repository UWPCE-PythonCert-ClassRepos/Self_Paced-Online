#!/usr/bin/env python3
from operator import itemgetter
import os
import sys
import datetime


# defines donor metrics
class Donor:
    def __init__(self, donor_name, donation=None):
        self.name = donor_name
        self.donation = donation if donation else []
        self.total = sum(self.donation)
        self.ave = self.total/len(self.donation) if donation else 0
        self.num_donations = len(self.donation)
            
 
# stores and updates donar data, makes reports 
class Donor_operations:
    def __init__(self, donors):
        self.donors_data = donors
        
    def donor_query():
        text = ["Enter the name of the donar", "Enter the donation amount"]
        donor = user_input.donor_query(text)
        # return donor
        
        for item in donor:
            print(item, type(item))
        
    # 'thank you' function here that calles 'donor query()'
    
    # 'append' function here
    
    # 'name check' function here
 
# list of donor instances  
donor_data = [
              Donor("Galileo Galilei", [348, 8377, 123]),
              Donor("Giovanni Cassini", [209]),
              Donor("Christiaan Huygens", [9135, 39]),
              Donor("Edmond Halley", [399, 1100, 357]),
              Donor("Edwin Hubble", [1899]),
              Donor("Mr. NoDonation")
              ]

# I guess this doesn't need to be a class then?
class user_input:
    # user input for menu selection
    def menu_render(text, key):
        while True:
            for line in text:
                print(line)                
            choice = input("-> ")
            try:
                key[choice]()
            except (KeyError):
                print("\nPlease enter one of the following options...")
                for item in key:
                    print(f'"{item}",', end=" ")
                print("\n")
                    
    # user input for new donations
    def donor_query(text):
        new_donor = input("Enter the name of the donar\n-> ")
        try:
            donation_amount = int(input("Enter an integer donation amount -> "))
        except(ValueError):
            print('entry not valid')
            user_input.menu_render(main_menu_text, main_menu_key)
        return [new_donor, [donation_amount]]


def Simple_print():
    for name in donor_data:
        print(name.name, name.donation)                

        
def Ex():
    sys.exit("quitting")  
        
        
main_menu_text = ["1. Simple Print", "2. Donor Query", "3. Quit"]
main_menu_key = {'1': Simple_print, '2': Donor_operations.donor_query, '3': Ex}

  
if __name__ == '__main__':
    user_input.menu_render(main_menu_text, main_menu_key)