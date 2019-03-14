# -*- coding: utf-8 -*-
"""
Created on Sat Mar 2 14:31:07 2019
@author: Florentin Popescu
"""

#===================LESSON_09====================
# Object Oriented Mailroom-----------------------
#================================================
#imports
import re, os, sys

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
    # properties and setters 
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
    # methods for statistics
    def number_donations(self):
        return len(self._donations)
    
    def sum_donations(self):
        return sum(self._donations)
    
    def average_donations(self):
        return round(self.sum_donations()/self.number_donations(), 2)
        
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
    def letter(name, amount):
        """
        Print a costumized thank-you note.
        """
        return f"\nDear {name.lstrip().rstrip():s}, \nThank you for you donation of ${amount:.2f} to our charity. \nSincerely." 
   
   
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
    
    #@donors.setter
    #def donors(self, donors):
    #    self._donors = donors
        
    #--------------------------------------------
    # methods for class objects extension and listing
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


#================================================
# User interface
#================================================
#donors on file
donors_set = DonorsDataSet([Donor("Name1", [1, 10, 100]),
                          Donor("Name2", [5.50, 15.50, 25.50]),
                          Donor("Name3", [1000000]),
                          Donor("Name4", [10.50, 20.75, 4.25]),
                          Donor("Name5", [999.99, 99.99, 9.99]),
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
               4: quit_program}
  
#-----------------------------------------------
def main(switch_dict):
    while True:
        try:
            alternative = int(input("Please select: \n1 : 'Send a Thank You', \n2 : 'Create a Report', \n3 : 'Send letters to everyone', \n4 : 'Exit'\n"))
            switch_dict[alternative]()
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
