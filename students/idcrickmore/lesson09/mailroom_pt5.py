#!/usr/bin/env python3
from operator import itemgetter
import os
import sys
import datetime


              
# defines donor metrics
class Donor:
    def __init__(self, donation=None):
        self.donation = donation if donation else []
        self.total = sum(self.donation)
        self.ave = self.total/len(self.donation) if donation else 0
        self.num_donations = len(self.donation)


donor_data = {
              "Galileo Galilei": [348, 8377, 123],
              "Giovanni Cassini": [209],
              "Christiaan Huygens": [9135, 39],
              "Edmond Halley": [399, 1100, 357],
              "Edwin Hubble": [1899],
              "Mr. NoDonation":[]
              }

# stores and updates donar data, makes reports 
class Donor_operations:
    def __init__(self, donors):
        self.donors_data = donors
    
    # 'append' function here
    def donor_append(name, don):
        try:
            donor_data[name].append(don)
        except KeyError:
        # if 'name_check' isn't in the donor dict...
        # set  the default format value as a list ([]) and append it
            donor_data.setdefault((name), []).append(don)
            
    # calls input class and returns donor object    
    def donation_query():
        text = ["\nEnter the name of the donar\nor 'list' for a list of donors\nor 'menu' for the main menu\n->", "Enter the donation amount\n->"]
        donor = user_input.donation_query(text)
        return donor

    # 'thank you' function here that calls 'donoration_query()'
    def thank_you():
        donor = Donor_operations.donation_query()

        if type(donor) == list:
            donor_dict = {"name": donor[0], "don": donor[1]}
            Donor_operations.donor_append(donor_dict["name"], donor_dict["don"])
            print("\n---------------- Thank You Letter ----------------\n"
                  "Dear {name},\n\n"
                  "You rock. Your fat contribution of ${don:,.2f}\n"
                  "will go a long way to lining my pockets.\n\n"
                  "Sincerely,\n"
                  "Scrooge McDuck\n".format(**donor_dict))
                  
        elif donor == 'list':
            Donor_operations.list_donors()


    # List donors
    def list_donors():
        print("\n---------------- List of Donors ----------------\n")
        for donor in donor_data:
            print(donor)
            

    
 
# list of donor instances  

class user_input:
    # user input for menu selection
    def menu_render(text, key):
        while True:
            print("\n---------------Main Menu-------------")
            print("Enter the number coresponding to your choice\n")
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
    def donation_query(text):
        new_donor = input(text[0])
        if new_donor == 'list':
            return 'list'
        elif new_donor == 'menu':
            return 'menu'
        try:
            donation_amount = float(input(text[1]))
        except(ValueError):
            print('entry not valid')
            user_input.menu_render(main_menu_text, main_menu_key)
        return [new_donor, donation_amount]


def Simple_print():
    for name in donor_data:
        metrics = Donor(donor_data[name])
        print(name, metrics.donation)                

        
def Ex():
    sys.exit("quitting")
        
        
main_menu_text = ["1. Simple Print", "2. Donor Thank You", "3. Quit"]
main_menu_key = {'1': Simple_print, '2': Donor_operations.thank_you, '3': Ex}

  
if __name__ == '__main__':
    user_input.menu_render(main_menu_text, main_menu_key)