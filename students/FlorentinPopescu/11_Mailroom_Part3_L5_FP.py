# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 12:30:49 2019
@author: Florentin Popescu
"""

#===================LESSON_05====================
# Mailroom, Part 3-------------------------------
#================================================

#================================================
# Exceptions
#================================================
import re, os, sys

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
    try:
        regex = re.compile("[-+=@_!#$%^&*()<>?/\|}{~:]")
        return bool(regex.search(string))
    except re.error as r_err:
        print(f"Error <{r_err}>. Invalid regular expression.")
   
#-----------------------------------------------
def letter(name, amount):
    '''
    Print a costumized thank-you note.
    '''
    return f"\nDear {name.lstrip().rstrip():s}, \nThank you for you donation of ${amount:.2f} to our charity. \nSincerely." 

#-----------------------------------------------
def add_donation(dit, name, amount):
    #add a new donor
    if name not in dit.keys():
        #dit.update({str(name):[amount]})
        dit[name] = [amount]
    #if donor exists, add new donation
    else: 
        dit[name].append(amount)
    
#-----------------------------------------------
def add_donation_print_letter(table, name, amount):
    '''
    Add donation to list and generate a thank-you note.
    '''
    add_donation(table, name, amount)
    print(letter(name, amount))

#-----------------------------------------------
def write_letter(dit):
    for key, value in dit.items():
        file_name = key + ".txt"
        try:
            with open(file_name, 'w') as f:
                f.write(letter(key, value[0]))
                print(f"Prepared letter for '{key:s}'.")
        except IOError as io_err:
            print(f"Error: <{io_err}>. Unable to write the file on disk or directory locked for writting.")
            
#-----------------------------------------------
def switch_directories(dit, current_directory, new_directory):
    try: 
        os.chdir(new_directory)
    except: 
        print(f"Something wrong with specified directory. Exception <{sys.exc_info()}>") 
    new_directory = os.getcwd()
    write_letter(dit)
    print(f"\nThank-you letters are storred in {new_directory}.")
    os.chdir(current_directory)
    current_directory = os.getcwd() 
     
#-----------------------------------------------
def sendletter_everyone(dit):
    current_directory = os.getcwd()
    print(f"Program located in {current_directory}")
    try:
        new_directory = input("Enter directory to store generated letters:\n").lower()
        if new_directory not in os.listdir():
            try:
                os.mkdir(new_directory)
            except OSError as os_err:
                print(f"Error <{os_err}>. Storage directory not indicated. Letters will be saved in the program's directory.\n")  
            switch_directories(dit, current_directory, new_directory)
        else:
            switch_directories(dit, current_directory, new_directory)
    except FileNotFoundError as fnf_err:
        print(fnf_err, "; please re-type.")
        
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
            if check_name(entered) or entered.isdigit() or entered == " ":
                print("We are sorry, but '{}' does not seem to be a not a valid name. Please re-enter;".format(entered))
            else:
                print ("\nAdd new donor: {}".format(entered))
                try:
                    amount = input("Welcome! Please enter your generous donation:\n")
                    amount = float(amount)
                    #gardian - when donation is positive, add the donor to the list along with donation and print a thank-you note. 
                    if amount > 0:
                        add_donation_print_letter(dit, entered, amount)
                    else: 
                        print ("We accept only positive donations. Please enter a donation to become one of our donors.")
                except ValueError as v_err:
                    print(f"\nWrong amount - error: '{v_err}'. Please re-enter the amount.\n")
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
            except ValueError as v_err:
                print(f"\nWrong amount - error: '{v_err}'. Please re-enter the amount.\n")
                    
#-----------------------------------------------
def report(dit):
    #compute statistics (sum, count, average) 
    tbl = {}
    for key, values in dit.items():
        tbl[key] = [sum(values), len(values), round(sum(values)/len(values), 2)]
        #tbl.update({key:[sum(values), len(values), round(sum(values)/len(values), 2)]})
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
def quit_program(table = None):
    sys.exit()

#-----------------------------------------------    
#switch dictionary 
switch_dict = {1: name_donation_letter,
               2: report,
               3: sendletter_everyone,
               4: quit_program}
  
#-----------------------------------------------
def main(switch_dict):
        while True:
            try:
                alternative = int(input("Please select: \n1 : 'Send a Thank You', \n2 : 'Create a Report', \n3 : 'Send letters to everyone', \n4 : 'Exit'\n"))
                switch_dict[alternative](donors)
            except (ValueError, TypeError, KeyError) as vtk_err:
                print(f"Error: <{vtk_err}>. Please select one of the options above. Enter 4 if you like to exit the program.\n")
            except SystemExit:
                print("--- Program closed ---")
                break
    
#===============================================
if __name__ == '__main__':
    main(switch_dict)
#===============================================
#--------------- END ---------------------------
#===============================================
 
