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

choices = {1: "Send a Thank You", 
           2: "Create a Report", 
           3: "Send letters to everyone",
           4: "Quit"}

#-----------------------------------------------
def donors_dict(table):
    dit = {}
    for key, values in table.items():
        dit.update({key:values})
    return dit

#-------------------------------------------
def add_donor(dit, item, donation = None):
    return dit.update({str(item):[donation]})

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
    """
    if not regex.search(string):
        bool(regex.search(string))
    """
#-----------------------------------------------
def statistics(table):
    '''
    Compute base statisting on donations (sum, average).
    '''
    tbl = {} 
    for key, values in table.items():
        tbl.update({key:[sum(values), len(values), round(sum(values)/len(values), 2)]})
    return tbl

#-----------------------------------------------
def letter(name, amount, prt = True):
    '''
    Print a costumized thank-you note.
    '''
    message = f"\nDear {name.lstrip().rstrip():s}, \nThank you for you donation of ${amount:.2f} to our charity. \nSincerely,1" 
    if prt: 
        print(message)
    return message

#-----------------------------------------------
def add_donation(table, name, amount):
    table.update({name:[amount]})
    
#-----------------------------------------------
def add_donation_print_letter(table, x, amount):
    '''
    Add donation to list and generate a thank-you note.
    '''
    add_donation(table, x, amount)
    letter(x, amount)

#-----------------------------------------------
def sendletter_everyone(table):
    for key, value in table.items():
        file_name = key + ".txt"
        with open(file_name, 'w') as f:
            f.write(letter(key, value[0], False))
            print("Prepared letter for {:s}.".format(key))

#-----------------------------------------------
def name_donation_letter(table):
    while True:
        entered = input("\nEnter: donor's name; list; quit:>>\n")
        if entered == 'quit':
            return (table)
        elif entered == 'list':
            print("\nExisting donors:") 
            print("".join("\n{}\t{}".format(key, value) for key, value in donors_dict(table).items()))
        elif entered not in donors_dict(table).keys() and entered not in ['list','quit']:
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
                        add_donor(table, entered, amount)
                        add_donation_print_letter(table, entered, amount)
                    else: print ("We accept only positive donations. Please enter a donation to become one of our donors.")
                except:
                    print('\nWrong amount. Try again','\n')
        elif entered in donors_dict(table).keys() and entered not in ['list','quit']:
            try:
                amount = input("Welcome back {}! Please enter your new donation:\n".format(entered))
                amount = float(amount)
                if amount > 0:
                    add_donation_print_letter(table, entered, amount)
                #gardian - when an old donor tries to withdraw money inform him his money was spent.
                elif amount < 0:
                    print ('Money you donated to charity in the past was spent for noble causes, we cannot return.\n')   
                else: 
                    print ("We accept only non-zero donations.")
            except:
                print("\nWrong amount. PLease re-enter:\n")

#-----------------------------------------------
def report(table):
    dst = dict(sorted(table.items(), key = lambda x: x[1], reverse = True))
    print("\n")
    print("-"*77)
    print ("".join([f"{'Donor Name':<20}", "|", f"{'Total Given |':>19}", f"{'Num Gifts |':>18}", f"{'Average Gift':>18}"]))
    print("-"*77)
    for key, value in dst.items():
        print(f"{key:<19} | ${round(value[0],2):>15,.2f} | {value[1]:>15d} | {round(value[2],2):>15,.2f}")
    print("-"*77)
    print("\n")

#-----------------------------------------------
def main(table, select):
    while True:
        for key, value in choices.items():
            print(key, value + '\n')
        alternative = input('\nSelect one of the above: 1, 2, 3 or 4:>>\n')
        try:
            alternative = int(alternative)
            if alternative == 1: name_donation_letter(table)
            elif alternative == 2: report(statistics(donors))
            elif alternative == 3: sendletter_everyone(table)
            elif alternative == 4: 
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
#NOTE: Nathasha's recommendations from Mailroom-Part 1 were implemented here.
 