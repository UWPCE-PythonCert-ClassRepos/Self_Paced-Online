#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import os

"""
Created on Wed Dec 26 19:30:19 2018

@author: dennis
"""

"""You work in the mail room at a local charity. Part of your job is to write incredibly boring, 
repetitive emails thanking your donors for their generous gifts. 
You are tired of doing this over and over again, so you’ve decided to let Python help 
you out of a jam and do your work for you."""

"""Update to mail room program to add functional programming"""

# Donor class - contains properties and methods for accessing and updating donor's data
class Donor:
    
    def __init__(self, name, donations=None):
        self.name = name
        if donations == None:
            self._donations = []
        else:
            self._donations = list(donations)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
 
    @property
    def donations(self):
        return self._donations
 
    def add_donation(self, amount):
        try:
            self.donations.append(float(amount))
        # Handle error if user doesn't input a valid numerical donation
        except ValueError:
            print('Not a valid donation.')
            prompt_donation(self.name)
    
    # Create email to donor thanking them for their generous donation
    def create_email(self, amount):
        return '\nDear {},\n\nThank you so much for generous donation of ${}.\n\n\t\t\tSincerely,\n\t\t\tPython Donation Team'.format(self.name, amount)

    def sum_donations(self):
        return sum(self.donations)
    
    def number_donations(self):
        return len(self.donations)
        
    def avg_donations(self):
        return self.sum_donations() / self.number_donations()
    
    def multiply_donations(self, factor):
        self._donations = list(map(lambda x: x*factor, self.donations))
        return self._donations
#        d = list(map(lambda x: x*factor, self.donations))
#        return d

    def filter_donations(self, min_donation = 0, max_donation = 99999999999999999):
        self._donations = list(filter(lambda x: int(min_donation) <= x <= int(max_donation), self.donations))
        return self._donations

    
# DonorCollection class - properties and methods for managing collection of donors
class DonorCollection:
        
    def __init__(self, donors=None):
        if donors == None:
            donors = []
        else:
            self._donors = donors

    @property
    def donors(self):
        return self._donors
 
    # Display list of donors by name
    def donor_list(self):
        list_donors = ''
        for donor in self.donors:
            list_donors += donor.name + '\n'
        return list_donors

    # Set donor
    def set_donor(self, full_name):
        exists = False
        # Check if existing donor
        for donor in self.donors:
            if donor.name == full_name:
                exists = True
                break
        # Not existing donor, so create new donor
        if not exists:
            donor = Donor(full_name)
            donors.add_donor(donor)
        return donor

    # Add new donor to donor collection
    def add_donor(self, donor):
        self.donors.append(donor)
        
     
    def sort_on_total_donation(self):
        return(sorted(self.donors, key=total_donation_key, reverse=True))


    # Create report
    def create_report(self):
        #Create list of summarized donations so that total can be sorted
        sorted_donors = donors.sort_on_total_donation()
        
        # Print summarized data
        report = '\nDonor Name                | Total Given | Num Gifts | Average Gift\n'
        report += '-'*66 + '\n'
        for donor in sorted_donors:
            if donor.donations != []:
                report +=  f'{donor.name: <27}${donor.sum_donations(): >12.2f}{donor.number_donations(): >12}  ${round(donor.avg_donations(),2): >11.2f}\n'
        print(report)
        return report

    # Send letters to everyone
    def send_letters(self):
        now = datetime.datetime.now()
        now = str(now.year) + '-' + str(now.month) + "-" + str(now.day)
        path = os.getcwd() + '/letters'
    
        # Change directory to letters directory, if it doesn't exist, create it
        try:
            os.chdir(path)
        except FileNotFoundError:
            os.makedirs(path)  
            os.chdir(path)
            
        # Loop through each donor and send thank you email
        try:
            for donor in self.donors:
                with open(donor.name + '_' + str(now) + '.txt', 'w') as outfile:
                    print(donor.name)
                    outfile.write(donor.create_email(donor.donations[-1]))
                
            print('\nThe thank you emails were sent!')
        except:
            print('\nThere was an error sending the thank you emails.')
            
    # Apply multiplication factor to each donor list
    def challenge(self, factor=3, min_donation=0, max_donation=99999999999999):
#        mult_donors = DonorCollection()
        for donor in self.donors:
            donor.filter_donations(min_donation, max_donation)
            donor.multiply_donations(factor)
#            d = donor.multiply_donations(factor)
#            mult_donors.add_donor(d)
        return donors
#        return mult_donors
       

# Create dictionary of donors
donor1 = Donor('Dennis Coffey', [2500.00,400.00,1400.00,4000.00,75.00])
donor2 = Donor('Bill Gates', [120.00,650.00,40.00,75.00])
donor3 = Donor('Ethan Coffey', [800.00,150.00,1100.00,2000.00,60.00])
donor4 = Donor('Paul Allen', [400.00,45000.00,9000.00])
donor5 = Donor('Jeff Bezos', [3.00,8.00])

donors = DonorCollection([donor1,donor2,donor3,donor4,donor5])

# Total donation for sorting
def total_donation_key(donor):
    return sum(donor.donations)


# Sending a Thank You
def send_thankyou():
    # Loop if user selects list
    full_name = 'list'
    while full_name.lower() == 'list':
        # Create prompt menu
        full_name = input('Please input your Full Name\n'
                          '\t or list if you would like to see a list of donors >> ')
            
        # Check user input and perform appropriate action    
        if full_name.lower() == 'list':
            # Create list of donors
            print(donors.donor_list())
        else:
            prompt_donation(full_name)
            break

# Prompt for donation scenarios
def run_donation_scenarios():
    print("Let's run donation scenarios by modifying multiplication factor,")
    print("minimum donation amount and maximum donation amount")
    # Input multiplication factor
    mult_factor = input('Please input a donation multiplication factor >> ')
    # Input minimum donation
    min_donation = input('Please input a minimum donation amount >> ')
    # Input maximum donation
    max_donation = input('Please input a maximum donation amount >> ')
    donors.challenge(int(mult_factor), int(min_donation), int(max_donation))
    donors.create_report()

# Prompt for donation amount and append donation to user    
def prompt_donation(full_name, donation_amount = None):
    current_donor = donors.set_donor(full_name)
    # Promt for donation amount
    if donation_amount == None:
        donation_amount = input('Please enter a donation amount $')
    try:
        current_donor.add_donation(donation_amount)
        print(current_donor.create_email(donation_amount))
        
    # Handle error if user doesn't input a valid numerical donation
    except ValueError:
        print('Not a valid donation.')
        prompt_donation(full_name) 
   
# Quit program
def user_quit():
    print("\nThank you, have a nice day.")


if __name__ == '__main__':

    # Loop until user selects Quit
    prompt = None
    switch_action_dict = {'a':send_thankyou, 'b':donors.create_report, 'c':donors.send_letters, 'd':run_donation_scenarios, 'e':user_quit}
    while prompt != 'e':
        # Create prompt menu
        prompt = input('Actions to choose from:\n'
                         '\ta) Send a Thank You\n'
                         '\tb) Create a Report\n'
                         '\tc) Send letters to everyone\n'
                         '\td) Run donation scenarios\n'
                         '\te) Quit\n'
                         'Please choose an action: ')
        try:
            switch_action_dict.get(prompt)()
        # Handle error for when user does not choose a valid option in the list
        except TypeError:
            print('\nNot a valid option.  Please choose a value from the list (a, b, c, d, or e)')
