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
        self.last = self.donation[-1]

        
donor_data = {
              "Galileo Galilei": [348, 8377, 123],
              "Giovanni Cassini": [209],
              "Christiaan Huygens": [9135, 39],
              "Edmond Halley": [399, 1100, 357],
              "Edwin Hubble": [1899],
              "Jill": [50, 200, 100, 250]
              }

# stores and updates donar data, makes reports 
class Donor_ops:

    # 'append' function
    def donor_append(name, don):
        try:
            donor_data[name].append(don)
        except KeyError:
            donor_data.setdefault((name), []).append(don)
            
    # 'thank you' function'
    def thank_you(query):
        if query != 'list' and query != 'menu':
            donation_info = Donor(donor_data[query])
            thank_you_text = str(f"""\n---------------- Thank You ----------------\n
Dear {query},\n
You rock. Your fat contribution of ${donation_info.last:,.2f}
will go a long way to lining my pockets.\n
Sincerely,
Scrooge McDuck""")
            Donor_ops.print_function(thank_you_text)
                  
        elif query == 'list':
            Donor_ops.list_donors()

    # List donors
    def list_donors():
        list_text = str("\n---------------- List of Donors ----------------\n\n")
        for donor in donor_data:
            list_text += (donor + '\n')
        Donor_ops.print_function(list_text)
            
    def report():
        columns = ["DONOR", "TOTAL", "AVERAGE", "NUMBER"]
        report_text = str("\n--------------- Report -------------\n\n")
        report_text += str('{:<30}{:<15}{:<15}{:<15}\n'.format(*columns))
        
        for name in donor_data:
            donation_info = Donor(donor_data[name])
            report_text += str('{:<30}{:<15}{:<15,.2f}{:<15}\n'.format(name, donation_info.total, donation_info.ave, donation_info.num_donations))
        Donor_ops.print_function(report_text)
            
    def letters():
        print("\n--------- Exporting Letters to Everyone ---------\n")
        print("Thank you letters have been exported to {}".format(os.getcwd()))

        for name in donor_data:
            donation_info = Donor(donor_data[name])
            letter = f"""Dear {name},

Your most recent contribution of ${donation_info.last:,.2f} to my money vault
is very appreciated. I will spend it freely but wisely.

Sincerely,
Scrooge McDuck"""
            with open(str(name) + "_" + str(datetime.date.today()) + '.txt', 'w') as out_file:
                out_file.write(letter)
        
    def print_function(text):
        print(text)
    

class user_input:
    # user input for menu selection
    def menu_render(text, key):
        print("\n---------------Main Menu-------------\n")
        print("Enter the number coresponding to your choice\n")
        for line in text:
            print(line)
        choice = input("-> ")
        if key[choice] == Donor_ops.thank_you:
            key[choice](user_input.donation_query())
        else:
            try:
                key[choice]()
            except (KeyError):
                print("\nPlease enter one of the following options...")
                for item in key:
                    print(f'"{item}",', end=" ")
                print("\n")
                
    # user input for new donations
    def donation_query():
        query = input("\nEnter the name of the donor\nor 'list' or 'menu'\n->")
        if query == 'list':
            return 'list'
        elif query == 'menu':
            return 'menu'
        try:
            donation_amount = float(input("Enter the donation amount\n->"))
        except(ValueError):
            print('entry not valid')
            user_input.menu_render(main_menu_text, main_menu_key)
        Donor_ops.donor_append(query,donation_amount)
        return query


def Simple_print():
    for name in donor_data:
        metrics = Donor(donor_data[name])
        print(name, metrics.donation)                

        
def Ex():
    sys.exit("quitting")

    
def main():
    while True:
        user_input.menu_render(main_menu_text, main_menu_key)
        
        
main_menu_text = ["1. Donor Thank You", "2. Report", "3. Letters", "4. Quit"]
main_menu_key = {'1': Donor_ops.thank_you, '2': Donor_ops.report, '3': Donor_ops.letters, '4': Ex}

  
if __name__ == '__main__':
    main()