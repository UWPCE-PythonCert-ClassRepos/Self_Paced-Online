#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import os
"""
Created on Thu Nov  8 19:30:19 2018

@author: dennis
"""

"""You work in the mail room at a local charity. Part of your job is to write incredibly boring, 
repetitive emails thanking your donors for their generous gifts. 
You are tired of doing this over and over again, so you’ve decided to let Python help 
you out of a jam and do your work for you."""

#Mailroom Part 2
#Update your mailroom program to:
#Use dicts where appropriate
#See if you can use a dict to switch between the users selections. See Using a Dictionary to switch for what this means.
#Try to use a dict and the .format() method to do the letter as one big template rather than building up a big string in parts.

#The Program
#Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:
#It should have a data structure that holds a list of your donors and a history of the amounts they have donated. 
#This structure should be populated at first with at least five donors, 
#with between 1 and 3 donations each.
#You can store that data structure in the global namespace.
#The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)

#Create dictionary of donors
donors = {'Dennis Coffey': [2500.00,400.00,1400.00], 
          'Bill Gates': [120.00,650.00], 
          'Ethan Coffey': [800.00,150.00,1100.00], 
          'Paul Allen': [45000.00,9000.00], 
          'Jeff Bezos': [3.00]}


#Sending a Thank You
#If the user (you) selects ‘Send a Thank You’, prompt for a Full Name. 
#If the user types ‘list’, show them a list of the donor names and re-prompt
#If the user types a name not in the list, add that name to the data structure and use it.
#If the user types a name in the list, use it.
#Once a name has been selected, prompt for a donation amount.
#Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
#Once an amount has been given, add that amount to the donation history of the selected user.
#Finally, use string formatting to compose an email thanking the donor for their generous donation. 
#Print the email to the terminal and return to the original prompt.
def send_thankyou():
    #Loop if user selects list
    full_name = 'list'
    while full_name.lower() == 'list':
        #Create prompt menu
        full_name = input('Please input your Full Name\n'
                          '\t or list if you would like to see a list of donors >> ')
            
        #Check user input and perform appropriate action    
        if full_name.lower() == 'list':
            [print(donor) for donor in donors.keys()]
        else:
            add_donation(full_name) 
            break

#Prompt for donation amount and append donation to user    
def add_donation(full_name):
    if full_name not in donors:
        donors[full_name] = []
    donation_amount = input('Please enter a donation amount $')
    donors[full_name].append(int(donation_amount))
    print(create_email(full_name, donation_amount))
    
#Create email to donor thanking them for their generous donation
def create_email(full_name, donation_amount):
    return '\nDear {},\n\nThank you so much for generous donation of ${}.\n\n\t\t\tSincerely,\n\t\t\tPython Donation Team'.format(full_name, donation_amount)

#Send letters to everyone
def send_letters():
    now = datetime.datetime.now()
    now = str(now.year) + '-' + str(now.month) + "-" + str(now.day)
    for k, v in donors.items():
        with open(k + '_' + str(now) + '.txt', 'w') as outfile:
            outfile.write(create_email(k,v[-1]))
    
#Quit program
def user_quit():
    print("\nThank you, have a nice day.")

#Creating a Report
#If the user (you) selected “Create a Report”, print a list of your donors, sorted by total historical donation amount. 
#Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
#Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
#After printing this report, return to the original prompt.
#At any point, the user should be able to quit their current task and return to the original prompt.
#From the original prompt, the user should be able to quit the script cleanly.
#Your report should look something like this:
# Donor Name                | Total Given | Num Gifts | Average Gift
# ------------------------------------------------------------------
# William Gates, III         $  653784.49           2  $   326892.24
# Mark Zuckerberg            $   16396.10           3  $     5465.37
# Jeff Bezos                 $     877.33           1  $      877.33
# Paul Allen                 $     708.42           3  $      236.14
def create_report():
    #Create list of summarized donations so that total can be sorted
    sum_donors = []
    for k, v in donors.items():
        sum_donors.append([k,sum(v),len(v),sum(v)/len(v)])
    sum_donors.sort(key=lambda tup: tup[1], reverse=True)
    
    #Print summarized data
    print('\nDonor Name                | Total Given | Num Gifts | Average Gift')
    print('-'*66)
    for donor in sum_donors:
        print(f'{donor[0]: <27}${donor[1]: >12.2f}{donor[2]: >12}  ${round(donor[3],2): >11.2f}')


if __name__ == '__main__':

    #Loop until user selects Quit
    prompt = None
    switch_action_dict = {'a':send_thankyou, 'b':create_report, 'c': send_letters, 'd': user_quit}
    while prompt != 'd':
        #Create prompt menu
        prompt = input('Actions to choose from:\n'
                         '\ta) Send a Thank You\n'
                         '\tb) Create a Report\n'
                         '\tc) Send letters to everyone\n'
                         '\td) Quit\n'
                         'Please choose an action: ')
        switch_action_dict.get(prompt)()
