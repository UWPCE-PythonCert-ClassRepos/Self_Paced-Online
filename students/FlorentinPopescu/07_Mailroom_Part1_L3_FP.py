# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:01:43 2019
@author: Florentin Popescu
"""

#===================LESSON_03====================
# Mailroom, Part 1-------------------------------
#================================================

#================================================
# Sending a Thank You note
#================================================
import re

#donors on file
donors = [['Name1', 1, 10, 100], 
          ['Name2', 5.50, 15.50, 25.50],
          ['Name3', 1000000],
          ['Name5', 10.50, 20.75, 4.25],
          ['Name6', 999.99, 99.99, 9.99],
          ['Name7', 0.75,  0.25]]


choices = ["Send a Thank You", "Create a Report", "Quit"]

#-----------------------------------------------
def donor_list(table):
    return [item[0] for item in table]

#-----------------------------------------------
def add_donor(table, item):
    return table.append([item])

#-----------------------------------------------
def check_name(string):
    '''
    Test if donor's name contains special characters
    '''
    regex = re.compile("[-+=@_!#$%^&*()<>?/\|}{~:]")
    if(regex.search(string) == None): 
        return True 
    else: 
        return False

#-----------------------------------------------
def statistics(table):
    '''
    Compute base statisting on donations (sum, average).
    '''
    #gardians - avoid division by 0
    tbl = [[item[0], sum(item[1:]), len(item[1:]), 
           sum(item[1:])/len(item[1:])] for item in table if item[1] > 0]
    tbl.sort(key=lambda x: x[1], reverse = True)
    return tbl

#-----------------------------------------------
def letter(name, amount):
    '''
    Print a costumized thank-you note.
    '''
    print(f"""\nDear {name.lstrip().rstrip():s}, 
              \nThank you for you donation of ${amount:,.2f} to our charity.""")

#-----------------------------------------------
def add_donation(table, name, amount):
    return table[donor_list(table).index(name)].append(amount)
    
#-----------------------------------------------
def addDonation_sendLetter(table, x, amount):
    '''
    Add donation to list and generate a thank-you note.
    '''
    add_donation(table, x, amount)
    letter(x, amount)
    return None

#-----------------------------------------------
def name_donation_letter(table):
    while True:
        x = input("\nEnter: donor's name; list; quit:>>\n")
        if x == 'quit':
            return (table)
        elif x == 'list':
            print ('\nExisting donors:\n', donor_list(table))
        elif x not in donor_list(table) and x not in ['list','quit']:
            # gardian - reject names containing special characters, pure numbers, or NaNs. 
            if not check_name(x) or x.isdigit() or x == " ":
                print("We are sorry, but '{}' does not seem to be a not a valid name. Please re-enter;".format(x))
            else:
                print ("\nAdd new donor: {}".format(x))
                try:
                    amount = input("Welcome! Please enter your generous donation:\n")
                    amount = float(amount)
                    #gardian - when donation is positive, add the donor to the list along with donation and print a thank-you note. 
                    if amount > 0:
                        add_donor(table, x)
                        addDonation_sendLetter(table, x, amount)
                    else: print ("We accept only positive donations. Please enter a donation to become one of our donors.")
                except:
                    print('\nWrong amount. Try again','\n')
        elif x in donor_list(table) and x not in ['list','quit']:
            try:
                amount = input("Welcome back {}! Please enter your new donation:\n".format(x))
                amount = float(amount)
                if amount > 0:
                    addDonation_sendLetter(table, x, amount)
                #gardian - when an old donor tries to withdraw money inform him his money was spent.
                elif amount < 0:
                    print ('Money you donated to charity in the past was spent for noble causes, we cannot return.\n')   
                else: 
                    print ("We accept only non-zero donations.")
            except:
                print("\nWrong amount. PLease re-enter:\n")

#-----------------------------------------------
def report(table):
    print("\n")
    print("-"*77)
    print ("".join([f"{'Donor Name':<20}", "|", f"{'Total Given |':>19}", f"{'Num Gifts |':>18}", f"{'Average Gift':>18}"]))
    print("-"*77)
    for item in table:
        print(f"{item[0]:<19} | ${round(item[1],2):>15,.2f} | {item[2]:>15d} | ${round(item[3],2):>15,.2f}")
    print("-"*77)
    print("\n")

#-----------------------------------------------
def main(table, select):
    while True:
        for idx, choice in enumerate(select):
             print(idx + 1, choice + '\n')
        x = input('\nSelect one of the above: 1, 2, or 3:>>\n')
        try:
            x = int(x)
            if x == 1: name_donation_letter(table)
            elif x == 2: report(statistics(table))
            elif x == 3: 
                print ("\nThank you for your interest in our charity. We hope to see you again.\n")
                return
            else:
                print ("\nWrong selection. Please re-select:\n")
        except:
            print("\nWrong selection. Please re-select:\n")

#===============================================
if __name__=='__main__':
    main(donors, choices)

#===============================================
#---------------- END --------------------------
#===============================================     

#-----------------------------------------------------------------------------
#Donor Name          |      Total Given |       Num Gifts |      Average Gift
#-----------------------------------------------------------------------------
#Name3               | $   1,000,000.00 |               1 | $   1,000,000.00
#Name6               | $       1,109.97 |               3 | $         369.99
#Name1               | $         111.00 |               3 | $          37.00
#Name2               | $          46.50 |               3 | $          15.50
#Name5               | $          35.50 |               3 | $          11.83
#Florentin           | $          20.00 |               1 | $          20.00
#Name7               | $           1.00 |               2 | $           0.50
#-----------------------------------------------------------------------------
    

