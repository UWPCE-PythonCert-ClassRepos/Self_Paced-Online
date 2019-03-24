# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:25:52 2019
@author: Florentin Popescu
"""

#===================LESSON_10====================
# ------------ Functional Mailroom --------------
#================================================

#imports
import re, os, sys, numpy as np, pandas as pd
from functools import reduce

#------------------------------------------------
class Donor():
    # holds donor's name and donation's amount
    
    #--------------------------------------------
    # class initializer
    def __init__(self, name, donations = None):
        self._name = name
        if donations:
            self._donations = donations
        else:
            self._donations = []
    
    #--------------------------------------------
    # class repper
    def __repr__(self):
        return f"Donor {self._name} : donation = {self._donations}" 
    
    #--------------------------------------------
    # class properties and setters 
    @property
    def name(self):
        return self._name
    
    @property
    def donations(self):
        return self._donations

    @name.setter
    def name(self, name):
        self._name = name
    
    #-----------------------------------------------
    # methods for object extension
    def add_donations(self, amount):
        self.donations.append(amount)
        
    #--------------------------------------------
    # reduce and mean
    def number_donations(self):
        return reduce(lambda x, y: x + 1, self._donations, 0)
        
    def sum_donations(self):
        return reduce(lambda x, y: x + y, self._donations)
    
    def average_donations(self):
        return round(np.array(self._donations).mean(), 2)
       
    #-----------------------------------------------
    # filter, map and repeat
    def donations_bellow_treshold(self, treshold):
        return list(filter(lambda x: x <= treshold, self.donations))
    
    def donations_above_treshold(self, treshold = 0.01):
        return list(filter(lambda x: x > treshold, self.donations))
    
    def multiply_donations(self, multiplier, list_donors):
        return list(map(lambda x: x * multiplier, list_donors))
    
    def clone_donations(self, multiplier, list_donors):
        return list(np.array(list_donors).repeat(multiplier))
    
    #-----------------------------------------------
    def __str__(self):
        return f"{self.name}: ${self.donations}: {self.number_donations}: {self.average_donations}"
    
    #-----------------------------------------------
    # static methods
    @staticmethod
    def check_name(name):
        #Test if donor's name contains special characters
        try:
            regex = re.compile("[-+=@_!#$%^&*()<>?/\|}{~:]")
            return bool(regex.search(name))
        except re.error as r_err:
            print(f"Error <{r_err}>. Invalid regular expression.")

    @staticmethod
    def letter(name, donation):
        """
        Print a costumized thank-you note.
        """
        return f"\nDear {name.lstrip().rstrip():s}, \nThank you for you donation of ${donation:.2f} to our charity. \nSincerely." 

#================================================
class DonorsDataSet():
    # holds donor dataset, methods to add new donors and statistics 
    
    #--------------------------------------------
    # class initializer    
    def __init__(self, donors = None):
        if donors:
            self._donors = donors
        else:
            self.donors = []

    #--------------------------------------------
    # class repper
    def __repr__(self):
        return f"Donors database: {self._donors}"
    
    #--------------------------------------------
    # class properties
    @property
    def donors(self):
        return self._donors
    
     #--------------------------------------------
    # methods for class object extension and listing
    def add_new_donor(self, donor):
        self.donors.append(donor)
        
    def list_donors(self):
        return [donor.name for donor in self.donors]

    def list_donations(self):
        return [donor.donations for donor in self.donors]
                         
    #-----------------------------------------------
    # methods for statistics reporting
    def stat_report(self):
        stat_table = ""
        for donor in self.donors:
            stat_table += "".join([f"{donor.name:<20}", "|", f"{donor.sum_donations():>19}", "|", f"{donor.number_donations():>18}", "|", f"{donor.average_donations():>18}\n"])
        return stat_table
    
    #----------------------------------------------
    def __iter__(self):
        return self
    
#================================================
# User interface
#================================================
#donors on file
donors_set = DonorsDataSet([Donor("Name1", [1, 10, 100]),
                          Donor("Name2", [5.50, 15.50, 25.50]),
                          Donor("Name3", [1000000]),
                          Donor("Name4", [10.50, 20.75, 4.25]),
                          Donor("Name5", [999.99, 99.99, 9.99]),
                          Donor("Name6", [0.75,  0.25])])

#-----------------------------------------------
def write_letter():
    for name, donation in zip(donors_set.list_donors(), donors_set.list_donations()):
        file_name = name + ".txt"
        try:
            with open(file_name, 'w') as f:
                f.write(Donor.letter(name, donation[0]))
                print(f"Prepared letter for '{name:s}'.")
        except (IOError, OSError, PermissionError, IsADirectoryError) as iosdp_err:
            print(f"Error: <{iosdp_err}>. Unable to write the file on disk or directory locked for writting.")

#-----------------------------------------------
def report():
    print("\n")
    print("-"*77)
    print ("".join([f"{'Donor Name':<20}", "|", f"{'Total Given':>19}", "|", f"{'Num Gifts ':>18}", "|", f"{'Average Gift':>18}"]))
    print("-"*77)
    print(donors_set.stat_report())
    print("-"*77)
    print("\n")
            
#-----------------------------------------------
def switch_directories(current_directory, new_directory):
    try: 
        os.chdir(new_directory)
    except (FileNotFoundError, WindowsError) as fnfw_err: 
        print(f"Something wrong with specified directory. Exception {fnfw_err} \n<{sys.exc_info()}>") 
    new_directory = os.getcwd()
    write_letter()
    print(f"\nThank-you letters are storred in {new_directory}.")
    os.chdir(current_directory)
    current_directory = os.getcwd() 
     
#-----------------------------------------------
def sendletter_everyone():
    current_directory = os.getcwd()
    print(f"Program located in {current_directory}")
    try:
        new_directory = input("Enter directory to store generated letters:\n").lower()
        if new_directory not in os.listdir():
            try:
                os.mkdir(new_directory)
            except OSError as os_err:
                print(f"Error <{os_err}>. Storage directory not indicated. Letters will be saved in the program's directory.\n")  
            switch_directories(current_directory, new_directory)
        else:
            switch_directories(current_directory, new_directory)
    except FileNotFoundError as fnf_err:
        print(fnf_err, "; please re-type.")
        
#----------------------------------------------
def challenge():
    vi = int(input("For a cloned view of the donation list please enter '1'; any other integer entered produces a compact view with all equal donations summed up in the list:\n"))
    multiplier = int(input("Please enter the cloning factor for your donations:\n"))
    min_donation = float(input("What's the minimal amount below which you want the donations cloned? \n"))
    try: 
        min_donation > 0.01
    except ValueError:
        min_donation = 0.01
        print("Challenge: \n")
    new_donors_set = []
    if vi == 1:
        for donor in donors_set.donors:
            new_donors_set.append(Donor(donor.name, sorted(donor.clone_donations(multiplier, donor.donations_bellow_treshold(min_donation)) + donor.donations_above_treshold(min_donation))))
            print(f"Prior donations of donor {donor.name}:")
            print(f"{sorted(donor.donations)}")
            print(f"Current donations of donor {donor.name} after clonning by a factor of {multiplier}:")
            print(f"{sorted(donor.clone_donations(multiplier, donor.donations_bellow_treshold(min_donation)) + donor.donations_above_treshold(min_donation))}\n")          
    else:
        for donor in donors_set.donors:
            new_donors_set.append(Donor(donor.name, sorted(donor.multiply_donations(multiplier, donor.donations_bellow_treshold(min_donation)) + donor.donations_above_treshold(min_donation))))
            print("Prior donations of donor {donor.name}:")
            print(f"{sorted(donor.donations)}")
            print(f"Current donations of donor {donor.name} after multiplication by {multiplier}:")
            print(f"{sorted(donor.multiply_donations(multiplier, donor.donations_bellow_treshold(min_donation))+ donor.donations_above_treshold(min_donation))}\n")
#----------------------------------------------

def forecast():
    lower_treshold = float(input("Please enter the treshold below which donations will double:\n"))
    upper_treshold = float(input("Please enter the treshold above which donations will triple: \n"))
    print("\033[91m" + "Scenario:")
    for donor in donors_set.donors:
        print(f"Total {donor.name}'s current donations: ${round(reduce(lambda x, y: x + y, donor.donations, 0), 2):0,.2f}")
        donations_after_doubling = donor.donations_bellow_treshold(lower_treshold)*2 + donor.donations_above_treshold(lower_treshold) 
        print(f" Total {donor.name}'s donations if donations < ${lower_treshold} double: ${round(reduce(lambda x, y: x + y, donations_after_doubling, 0), 2):0,.2f}")
        donations_after_tripling = donor.donations_above_treshold(upper_treshold)*3 + donor.donations_bellow_treshold(upper_treshold)
        print(f" Total {donor.name}'s donations if donations > ${upper_treshold} triple: ${round(reduce(lambda x, y: x + y, donations_after_tripling, 0), 2):0,.2f}")
        stats = pd.DataFrame({"Initial": pd.Series(donor.donations), "Doubling": pd.Series(donations_after_doubling), "Tripling": pd.Series(donations_after_tripling)}).round(2)
        print(f"Statistics for '{donor.name}':\n {stats.describe().fillna(0).round(2)}\n")
        
#-----------------------------------------------
def name_donation_letter():
    while True:
        entered = input("\nEnter: donor's name; list; quit:>>\n")
        if entered == 'quit':
            return None
        elif entered == 'list':
            print("\nExisting donors:") 
            print("".join("\n{}\t{}".format(name, donation) for name, donation in zip(donors_set.list_donors(), donors_set.list_donations())))
        elif entered not in donors_set.list_donors():
            # gardian - reject names containing special characters, pure numbers, or NaNs. 
            if Donor.check_name(entered) or entered.isdigit() or entered == " ":
                print("We are sorry, but '{}' does not seem to be a not a valid name. Please re-enter;".format(entered))
            else:
                print ("\nAdd new donor: {}".format(entered))
                amount = input("Welcome! Please enter your generous donation:\n")
                try:
                    amount = float(amount)
                except ValueError as v_err:
                    print(f"\nWrong amount - error: '{v_err}'. Please re-enter the amount.\n")
                #gardian - when donation is positive, add the donor to the list along with donation and print a thank-you note. 
                if amount > 0:
                    donors_set.add_new_donor(Donor(entered, [amount]))
                else: 
                    print ("We accept only positive donations. Please enter a donation to become one of our donors.")
        else:
            amount = input("Welcome back {}! Please enter your new donation:\n".format(entered))
            try:
                amount = float(amount)
            except ValueError as v_err:
                print(f"\nWrong amount - error: '{v_err}'. Please re-enter the amount.\n")
            if amount > 0:
                for donor in donors_set.donors:
                    if donor.name == entered:
                       donor.add_donations(amount)
            #gardian - when an old donor tries to withdraw money inform him his money was spent.
            elif amount < 0:
                print ('Money you donated to charity in the past was spent for noble causes, we cannot return.\n')   
            else: 
                print ("We accept only non-zero donations.")
           
#-----------------------------------------------
def quit_program(table = None):
    sys.exit()

#-----------------------------------------------    
#switch dictionary 
switch_dict = {1: name_donation_letter,
               2: report,
               3: sendletter_everyone,
               4: challenge,
               5: forecast,
               6: quit_program}
  
#-----------------------------------------------
def main(switch_dict):
    while True:
        try:
            alternative = int(input("Please select: \n1 : 'Send a Thank You', \n2 : 'Create a Report', \n3 : 'Send letters to everyone', \n4 : 'Challenge', \n5 : 'Forecast', \n6 : 'Exit'\n"))
            switch_dict[alternative]()
        except (ValueError, TypeError, KeyError) as vtk_err:
            print(f"Error: <{vtk_err}>. Please select one of the options above. Enter 6 if you like to exit the program.\n")
        except SystemExit:
            print("--- Program closed ---")
            break

    
#===============================================
if __name__ == '__main__':
    main(switch_dict)
    
#===============================================
#--------------- END ---------------------------
#===============================================
