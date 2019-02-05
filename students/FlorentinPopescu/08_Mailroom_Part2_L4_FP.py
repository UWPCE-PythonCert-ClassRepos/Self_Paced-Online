# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 12:30:49 2019
@author: Florentin Popescu
"""

#===================LESSON_04====================
# Mailroom, Part 2-------------------------------
#================================================

#================================================
# Update mailroom with file writting
#================================================
import re

#donors on file
donors = {"Name1": [1, 10, 100], 
          "Name2": [5.50, 15.50, 25.50],
          "Name3": [ 1000000],
          "Name5": [10.50, 20.75, 4.25],
          "Name6": [999.99, 99.99, 9.99],
          "Name7": [0.75,  0.25]}

#-----------------------------------------------
def check_name(string):
    '''
    Test if donor's name contains special characters
    '''
    regex = re.compile("[-+=@_!#$%^&*()<>?/\|}{~:]")
    return (not bool(regex.search(string)))
    
#-----------------------------------------------
def letter(name, amount, prt = True):
    '''
    Print a costumized thank-you note.
    '''
    message = f"\nDear {name.lstrip().rstrip():s}, \nThank you for you donation of ${amount:.2f} to our charity. \nSincerely." 
    if prt: 
        print(message)
    return message

#-----------------------------------------------
def add_donation(dit, name, amount):
    #add a new donor
    if name not in dit.keys():
        dit.update({str(name):[amount]})
    #if donor exists, add new donation
    else: 
        dit[name].append(amount)
    
#-----------------------------------------------
def add_donation_print_letter(table, name, amount):
    '''
    Add donation to list and generate a thank-you note.
    '''
    add_donation(table, name, amount)
    letter(name, amount)

#-----------------------------------------------
def sendletter_everyone(dit):
    for key, value in dit.items():
        file_name = key + ".txt"
        with open(file_name, 'w') as f:
            f.write(letter(key, value[0], False))
            print("Prepared letter for {:s}.".format(key))

#-----------------------------------------------
def name_donation_letter(dit):
    while True:
        entered = input("\nEnter: donor's name; list; quit:>>\n")
        if entered == 'quit':
            return None
        elif entered == 'list':
            print("\nExisting donors:") 
            print("".join("\n{}\t{}".format(key, value) for key, value in dit.items()))
        elif entered not in dit.keys():
            # gardian - reject names containing special characters, pure numbers, or NaNs. 
            if not check_name(entered) or entered.isdigit() or entered == " ":
                print("We are sorry, but '{}' does not seem to be a not a valid name. Please re-enter;".format(entered))
            else:
                print ("\nAdd new donor: {}".format(entered))
                try:
                    amount = input("Welcome! Please enter your generous donation:\n")
                    amount = float(amount)
                    #gardian - when donation is positive, add the donor to the list along with donation and print a thank-you note. 
                    if amount > 0:
                        add_donation_print_letter(dit, entered, amount)
                    else: print ("We accept only positive donations. Please enter a donation to become one of our donors.")
                except:
                    print('\nWrong amount. Try again','\n')
        else: 
            try:
                amount = input("Welcome back {}! Please enter your new donation:\n".format(entered))
                amount = float(amount)
                if amount > 0:
                    add_donation_print_letter(dit, entered, amount)
                #gardian - when an old donor tries to withdraw money inform him his money was spent.
                elif amount < 0:
                    print ('Money you donated to charity in the past was spent for noble causes, we cannot return.\n')   
                else: 
                    print ("We accept only non-zero donations.")
            except:
                print("\nWrong amount. PLease re-enter:\n")

#-----------------------------------------------
def report(dit):
    #compute statistics (sum, count, average) 
    tbl = {}
    for key, values in dit.items():
        tbl.update({key:[sum(values), len(values), round(sum(values)/len(values), 2)]})
    dst = dict(sorted(tbl.items(), key = lambda x: x[1], reverse = True))
    
    #print statistics
    print("\n")
    print("-"*77)
    print ("".join([f"{'Donor Name':<20}", "|", f"{'Total Given |':>19}", f"{'Num Gifts |':>18}", f"{'Average Gift':>18}"]))
    print("-"*77)
    for key, value in dst.items():
        print(f"{key:<19} | ${round(value[0],2):>15,.2f} | {value[1]:>15d} | {round(value[2],2):>15,.2f}")
    print("-"*77)
    print("\n")

#-----------------------------------------------
#switch dictionary 
switch_dict = {1: name_donation_letter,
               2: report,
               3: sendletter_everyone,
               4: exit}
  
alternative = None
#-----------------------------------------------
def main(table, switch_dict, alternative):
    while alternative != list(switch_dict.keys())[3]:  
        try:
            alternative = int(input("Please enter:, \n1 : 'Send a Thank You', \n2 : 'Create a Report', \n3 : 'Send letters to everyone', \n4 : 'Exit'\n"))
            switch_dict.get(alternative)(table)
        except:
            print("\nPlease select one of the options above. Enter 4 if you like to exit the program.\n")
            
#===============================================
if __name__=='__main__':
    main(donors, switch_dict, alternative)

