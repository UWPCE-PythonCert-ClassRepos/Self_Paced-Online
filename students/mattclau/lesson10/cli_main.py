from sys import exit
import os
from donor_models import *


class CLIMain:

    match = 1.0

    def __init__(self, donors):
        """set initial list of donors from those passed in"""
        self.donors = donors

    def thank_you(self, passed_name=None):
        """Send thank you to the user passed in or get name for letter."""
        name = CLIMain.check_passed_name(self,passed_name)

        #check only if donor exists, ask to add if not
        CLIMain.check_donor_exists(self, name, 'send_letter')

        donor = self.donors.get_donor_from_name(name)

        print(donor.create_letter())

        CLIMain.show_menu(self)

    def add_donor(self, passed_name=None):
        """gets name and optional donation amount for new donor, if already on list, gets only donation if requested"""
        name = CLIMain.check_passed_name(self,passed_name)

        #check only if donor exists, ask to add if not
        CLIMain.check_donor_exists(self, name, 'add_donor')

        #get initial donation for new donor if there is one
        init_donation = [CLIMain.initial_donation()]

        #add new donor
        new_donor = Donor(name, donations = init_donation)

        #add new donor to collection
        self.donors.add_donor(new_donor)

        #ask if user wants to send letter for new donor
        if init_donation != [None]:
            CLIMain.send_letter_after_donation(self, name)

        #print current list of donors
        CLIMain.print_donors(self)

        CLIMain.show_menu(self)

    def add_donation(self, passed_name=None):
        """Adds donation for existing user"""
        name = CLIMain.check_passed_name(self,passed_name)

        #check if donor exists, if it does, add donation
        CLIMain.check_donor_exists(self, name, 'add_donation')

        #get donor object
        donor = self.donors.get_donor_from_name(name)

        #get donation amount
        amount = CLIMain.get_donation()

        #add donation amount for donor
        donor.add_donation(amount)

        #ask if user wants to send letter for new donation
        CLIMain.send_letter_after_donation(self, name)

        #print current list of donors
        CLIMain.print_donors(self)

        CLIMain.show_menu(self)

    def report(self):
        """Prints aggregated, ordered report for all donors"""
        print('Would you like to sort descending? Enter Yes for descending or No for Ascending.')
        choice = CLIMain.get_choice()

        desc = False

        if choice.upper() == 'Y':
            desc = True

        sort_type = CLIMain.get_sort_type()

        sorted_donations = self.donors.aggregate_donations(desc, sort_type)

        print(CLIMain.report_formatter(sorted_donations))

        CLIMain.show_menu(self)

    def send_all(self):
        """Print letters for all donors, gets path where to save files from user"""
        path = CLIMain.get_file_path()

        for donor in self.donors.return_donors():
            CLIMain.export_letter(self, donor, path)

        CLIMain.show_menu(self)

    def match_factor(self):
        """sef global match factor for all new donations"""
        try:
            match = float(input('\nEnter global match factor: '))
        except ValueError:
            print('\n***Error! Use only numbers for the match factor.***')
            return CLIMain.match_factor()
        else:
            CLIMain.match = match
            print('\nGloba match factor now set to', CLIMain.match, 'for all new donations.\n')

    def match_all(self):
        """update all past donations to new amount based on match factor"""
        #print current list of donors
        CLIMain.print_donors(self)

        match, new_donors = CLIMain.pass_match_values(self)

        print('\nMatch factor of', match, 'applied to all current donations.\n')
        #print new list of donors
        [print(donor.name,donor.donations) for donor in new_donors.return_donors()]


    def projection(self):
        """update all past donations to new amount based on match factor"""
        #print current list of donors
        CLIMain.print_donors(self)

        match, new_donors, projected_total = CLIMain.pass_match_values(self, True)

        print('\nWith a match factor of', match, 'applied to donations in your current range,\n')
        print(f'Your projected total matching contribution would be ${projected_total:,.2f}\n')
        print('The matched donations with their new values are as follows:')
        [print(donor.name,donor.donations) for donor in new_donors.return_donors()]

    def quit(self):
        """Function that exits the program when called"""
        exit()

    #dictionary for switch that calls functions based on key values
    menu = {'1':add_donor, '2':add_donation, '3':thank_you, '4':report, '5':send_all, '6':match_factor, '7':match_all, '8':projection, '9':quit}

    def show_menu(self):
        while True:
            print("\n1. Add a new donor","\n2. Add donation for existing donor","\n3. Send a Thank You letter to a single donor"
                    ,"\n4. Create a Donor Report", "\n5. Send letters to all donors", "\n6. Set Global Match Factor", "\n7. Multiply all donations by match factor"
                    , "\n8. Project Donations Based on Matching", "\n9. Quit")
            selection = input("Enter the number for the action you require: ")
            try:
                CLIMain.menu[selection](self)

            except KeyError:
                print('\n***Error! Please enter only numbers from the menu.***')


    def get_donation():
        """Asks for and returns donation amount"""
        try:
            donation = float(input('\nEnter donation amount: '))
        except ValueError:
            print('\n***Error! Use only numbers for the donation amount.***')
            return CLIMain.get_donation()
        else:
            #multiply by match, default is 1, so only changes donation if factor set
            return donation * CLIMain.match

    def set_min_max():
        """Asks for and returns minimum or maximum donation amount"""
        try:
            min_max = float(input('\nEnter a value: '))
        except ValueError:
            print('\n***Error! Use only numbers for the donation amount.***')
            return CLIMain.get_donation()
        else:
            return min_max

    def pass_match_values(self, projection = False):
        """Asks for and returns minimum or maximum donation amount"""
        print('Would you like to add a minimum donation amount for the match?')
        choice = CLIMain.get_choice()

        if choice == 'Y':
            min_donation = CLIMain.set_min_max()

        print('Would you like to add a maximum donation amount for the match?')
        choice = CLIMain.get_choice()

        if choice == 'Y':
            max_donation = CLIMain.set_min_max()

        try:
            match = float(input('\nEnter match factor for all current donations: '))
        except ValueError:
            print('\n***Error! Use only numbers for the match factor.***')
            return CLIMain.match_factor()

        try:
            new_donors, projected_total = self.donors.match_donations(match, min_don=min_donation, max_don=max_donation, projection=projection)
        except:
            try:
                new_donors, projected_total = self.donors.match_donations(match, min_don=min_donation, projection=projection)
            except:
                try:
                    new_donors, projected_total = self.donors.match_donations(match, max_don=max_donation, projection=projection)
                except:
                    new_donors, projected_total = self.donors.match_donations(match, projection=projection)
        if projection:
            return match, new_donors, projected_total
        else:
            return match, new_donors

    def get_name(self):
        """Gets and returns user input for donor name, displays list of names if needed"""
        name = ''
        name = input('\nEnter a donor name or type list to see all current donors: ').title()

        #display list of names if requested
        if name.upper() == 'LIST':
            name = ''
            #changed to comprehension
            [print(donor.name) for donor in self.donors.return_donors()]
            return CLIMain.get_name(self)

        return name

    def check_passed_name(self,passed_name):
        if passed_name:
            name = passed_name
        else:
            name = CLIMain.get_name(self)
        return name

    def get_choice():
        """gets and returns user choice for Y/N questions"""
        choice = input('Please enter Yes (Y) or No (N): ')
        if choice.upper() not in ('Y','N','YES','NO'):
            print('\n***Error! Please enter Yes or No.***')
            return CLIMain.get_choice()
        else:
            return choice[0].upper()

    def get_sort_type():
        """requests and returns sort order type from user"""
        sort_types = {'1':'sum', '2':'avg', '3':'len'}
        print("\nHow would you like the report sorted?")
        print("1. Sort by Sum of donations per donor","\n2. Sort by average of donations per donor","\n3. Sort by number of donations per donor")

        selection = input("Enter the number for the sort type you require: ")

        try:
            return sort_types[selection]
        except KeyError:
            print('\n***Error! Please enter only numbers from the menu.***')
            CLIMain.get_sort_type()


    def print_donors(self):
        """prints current list of donors and their donations"""
        print('\nCurrent List of Donors:\n')
        [print(donor.name,donor.donations) for donor in self.donors.return_donors()]
        print('\n')


    def initial_donation():
        """Asks for and returns initial donation"""
        print('Would you like to enter an initial donation for this donor?')
        choice = CLIMain.get_choice()

        if choice.upper() == 'Y':
            return CLIMain.get_donation()

    def check_donor_exists(self, name, action_type):
        if self.donors.check_for_donor(name) and action_type == 'add_donor':
            print('***Error! Donor has already been added.  Would you like to add a donation for this donor instead?***')
            choice = CLIMain.get_choice()

            if choice == 'Y':
                self.add_donation(name)
            else:
                CLIMain.show_menu(self)
        elif not self.donors.check_for_donor(name) and action_type != 'add_donor':
            print('***Error! Donor does not yet exist.  Would you like to them as a new donor instead?***')
            choice = CLIMain.get_choice()

            if choice == 'Y':
                self.add_donor(name)
            else:
                CLIMain.show_menu(self)

    def send_letter_after_donation(self,passed_name):
        print('Would you like to send a thank you letter for this latest donation?')
        choice = CLIMain.get_choice()

        if choice.upper() == 'Y':
            return CLIMain.thank_you(self,passed_name)

    def get_file_path():
        """Requests and returns file path from user"""
        userpath = input('\nEnter the directory path where the files should be created.  Hit enter to create in directory of program: ')

        if userpath == '':
            return userpath
        elif not os.path.isdir(userpath):
            print('\n***Error! Please create directory before creating letters.***')
            return CLIMain.get_file_path()
        elif not os.access(userpath, os.W_OK):
            print('\n***Error! User does not have permission to write to this directory.***')
            return CLIMain.get_file_path()
        else:
            return userpath

    def export_letter(self, donor, passedpath):
        """Writes letter to file with given path"""
        try:
            os.path.isdir(passedpath)

            #add path if given
            filename = os.path.join(passedpath,donor.name.replace(' ','_') + '.txt')

            #updated to use with
            with open(filename, 'w') as outfile:
                outfile.write(donor.create_letter(donor))
            outfile.close()
        except PermissionError:
            print('\n***Error! User does not have permission to write to this directory.***')

            return send_all()
        except FileNotFoundError:
            print('\n***Error! Please create directory before creating letters.***')
            return send_all()

    def report_formatter(donations):
        """Formats the passed in aggregate donations into a report"""
        #print header
        header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
        formatted_report = f'\n{header[0]:<20}|{header[1]:^15}|{header[2]:^11}|{header[3]:^16}'
        formatted_report += '\n'
        formatted_report += '-'*(20+15+13+16+2)
        formatted_report += '\n'

        #print donor rows
        #changed to comprehension
        formatted_report += '\n'.join(f'{row[0]:<20}  ${row[1]:<15,.2f}{row[2]:<11} ${row[3]:<16,.2f}' for row in donations)
        formatted_report += '\n'
        return formatted_report

