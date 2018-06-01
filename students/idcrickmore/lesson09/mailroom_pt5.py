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
            

donor_data = [
              Donor("Galileo Galilei", [348, 8377, 123]),
              Donor("Giovanni Cassini", [209]),
              Donor("Christiaan Huygens", [9135, 39]),
              Donor("Edmond Halley", [399, 1100, 357]),
              Donor("Edwin Hubble", [1899]),
              Donor("Mr. NoDonation")
              ]
              
# stores and updates donar data, makes reports 
class Donor_operations:
    def __init__(self, donors):
        self.donors_data = donors
    
    # calls input class and returns donor object    
    def donation_query():
        text = ["\nEnter the name of the donar\nor 'list' for a list of donors\nor 'menu' for the main menu\n->", "Enter the donation amount\n->"]
        donor = user_input.donation_query(text)
        return donor
        
    # 'thank you' function here that calls 'donoration_query()'
    def thank_you():
        item = Donor_operations.donation_query()
        
        if type(item) == list:
            letter_dict = {"name": item[0], "don": item[1]}
            print("\n---------------- Thank You Letter ----------------\n"
                  "Dear {name},\n\n"
                  "You rock. Your fat contribution of ${don:,.2f}\n"
                  "will go a long way to lining my pockets.\n\n"
                  "Sincerely,\n"
                  "Scrooge McDuck\n".format(**letter_dict))
                  
        elif item == 'list':
            Donor_operations.list_donors()


    # List donors
    def list_donors():
        print("\n---------------- List of Donors ----------------\n")
        for item in donor_data:
            print(item.name)
            
    # 'append' function here
    
    # 'name check' function here
 
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
        print(name.name, name.donation)                

        
def Ex():
    sys.exit("quitting")  
        
        
main_menu_text = ["1. Simple Print", "2. Donor Thank You", "3. Quit"]
main_menu_key = {'1': Simple_print, '2': Donor_operations.thank_you, '3': Ex}

  
if __name__ == '__main__':
    user_input.menu_render(main_menu_text, main_menu_key)