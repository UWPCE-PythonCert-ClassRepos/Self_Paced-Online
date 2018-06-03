#!/usr/bin/env python3

"""Updated Mailroom Script
$ chmod +x mailroom_fp.py
"""

import datetime
import os

class Donor:

    def __init__(self, firstname, lastname, donations=None):
        self._firstname = firstname
        self._lastname = lastname
        self._donations = donations if donations else []

    @property
    def fullname(self):
        """returns string with fullname of donor"""
        return f"{self._firstname} {self._lastname}"

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def donations(self):
        return self._donations

    def donations_total(self):
        """returns the total donations"""
        try:
            return sum(self._donations)
        except TypeError:
            return self._donations

    def last_donation(self):
        return self._donations[-1]

    def add_donation(self, donation):
        """adds the new donation amount to donations"""
        return self.donations.append(donation)

    def donation_count(self):
        """returns number of donations"""
        return len(self._donations)

    def average_donation(self):
        try:
            return self.donations_total() / self.donation_count()
        except TypeError:
            return self._donations


class DonorFunctions:

    def __init__(self, donors=None):
        self._donorslist = donors if donors else []

    def donorslist(self):
        return self._donorslist

    def add_donor(self, donor):
        self._donorslist.append(donor)

    def get_all_donors(self):
        return [d.fullname for d in self._donorslist]

    def list_all_donors(self):
        return "\n".join(self.get_all_donors())

    def send_single_thank_you(self):
        """function for sending thank you message-gets/ adds single donation and prints thank you"""
        donor_name = get_name_input(self.get_all_donors())
        if donor_name == "quit":
            print("No donor name entered, exiting to menu")
        else:
            donor_amount = check_number_input()

            if donor_name not in self.get_all_donors():
                firstname, lastname = donor_name.split(" ")
                self.add_donor(Donor(firstname, lastname, [donor_amount]))
            else:
                for donor in self._donorslist:
                    if donor.fullname == donor_name:
                        donor.add_donation(donor_amount)
            print('\nDear {},'.format(donor_name))
            print('''\tThank you for your generous donation of ${:,.2f}\n
                Sincerely, \nThe ChickTech Donations Department\n'''.format(
                donor_amount))

    def print_report(self):
        """Print report to match example from assignment for donor list """
        print()
        title = ['Donor Name', '|  Total Given ', '|   Num Gifts',
                 '  | Average Gift']
        print('{:<20}{:>14}{:^14}{:>14}'.format(title[0], title[1],
                                                title[2], title[3]))
        print('-'*65)
        print()
        # # Creating list to hold donors info for printing
        for donor in self._donorslist:
            print('{:<22}{}{:>12.2f}{:>10}{:>8}{:>12.2f}'.format(donor.fullname, '$',
                                                                 donor.donations_total(), donor.donation_count(),
                                                                 '$', donor.average_donation()))
        print()

    def send_letters_everyone(self):
        """Creates a letter for everyone in the database, and writes them to file."""
        letters_count = 0
        date = datetime.datetime.now()
        new_folder = date.strftime("%Y-%m-%d_%H-%M")
        try:
            os.mkdir(new_folder)
        except OSError:
            print("\nError with directory creation.Something must have gone wrong!\n")
            return
        for donor in self._donorslist:
            # create file in date folder titled with donor name
            filename = "./{}/{}_{}.txt".format(new_folder,
                                               donor.firstname, donor.lastname)
            with open(filename, 'w') as donor_thanks:
                letter_output = print_thank_you_total(donor)
                donor_thanks.write(letter_output)
            letters_count += 1
        print("Created {} Thank You letters in this folder: {}".format(
            letters_count, new_folder))

    def print_letters_to_everyone(self):
        '''test print all function'''
        print()
        for donor in self._donorslist:
            print(print_thank_you_total(donor))

    def print_donors(self):
        print(self.print_report())

    def print_donors_names(self):
        """ prints list of donors"""
        print("\nDonors")
        print("-"*20)
        print(self.list_all_donors())

    def print_donors_and_donations(self):
        """Prints all letters to screen - for view and testing"""
        print("\nDonors and donations")
        print("-"*30, "\n")
        [print(donor.fullname, "=>", donor.donations, '\n')
         for donor in self._donorslist]


    def print_donors_and_donation_totals(self):
        """Prints all letters to screen - for view and testing"""
        print("\nDonors and donations")
        print("-"*30, "\n")
        [print(donor.fullname, "=>", donor.donations_total(), '\n')
         for donor in self._donorslist]


    def new_donors_list(self, factor, min_don=None, max_don=None):
        """Calls the challenge function and returns new database.
        **Attempted to do this in challenge - but kept encountering an error.**"""
        updated_donor_list = self.challenge(factor, min_don, max_don)
        return DonorFunctions(updated_donor_list)

    def challenge(self, factor, min_don=None, max_don=None):
        """Returns a new db of donors multiplied by the factor provided. 
        Creates new db calling the filter_factor_map"""
        new_d_list = []
        for donor in self._donorslist:
            new_d_list.append(Donor(donor.firstname, donor.lastname,
                                    self.filter_factor_map(factor, donor.donations, min_don, max_don)))
        #return list of donors
        return new_d_list

    def projection(self, factor, min_donation=None, max_donation=None):
        """Return projection value for donations. a feature that could show them, 
        based on past contributions, what their total contribution would become under different scenarios
        """
        projected_contribution = 0
        for donor in self._donorslist:
            projected_contribution += sum(self.filter_factor_map(factor,
                                                                 donor.donations,
                                                                 min_donation,
                                                                 max_donation))
        # returns the projection
        return projected_contribution

    def filter_factor_map(self, factor, donations, min_donation=None, max_donation=None):
        """Uses filter, map and the factor to provide the new list of filtered donations"""
        if min_donation and max_donation:
            if min_donation > max_donation:
                raise ValueError(
                    'Minimum Donation listed is larger than Maximum Donation. Try Again!')
            else:
                # for donation in donations:
                return list(map(lambda x: x * factor,
                                filter(lambda y: min_donation <= y <= max_donation, donations)))
        elif min_donation:
            # for donation in donations:
            return list(map(lambda x: x * factor,
                            filter(lambda y: y >= min_donation, donations)))
        elif max_donation:
            # for donation in donations:
            return list(map(lambda x: x * factor,
                            filter(lambda y: y <= max_donation, donations)))
        else:
            # for donation in donations:
            return list(map(lambda x: x * factor, donations))


# Mailroom menu functions
def menu_selection(menu_input, user_entry):
    """menu function"""
    try:
        menu_input[user_entry]['menu_dispatch']()
    except KeyError:
        print("{} is not a valid choice. ".format(user_entry))
        return False
    else:
        return True


def main_menu():
    '''Create Main Menu'''
    main_menu_title = "\nWelcome to the Mailroom App\nWhat would you like to do?\n"
    print_menu_options(MAIN_MENU, main_menu_title)


def print_menu_options(menu_input, menu_title):
    ''' Prints  Menu'''
    while True:
        print(menu_title)
        for key, value in menu_input.items():
            # prints each option and then prompts for user input
            print(key, value['menu_prompt'])
        response = input("\nEnter a number or q to exit menu>>>  ")
        menu_selection(menu_input, response)
        if response == 'q':
            return


def single_print_menu():
    '''Create single print sub Menu'''
    single_print_menu_title = "\nWelcome to the Send A Thank You Menu:\nHow would you like to find a donor: \n"
    print_menu_options(SINGLE_PRINT_SUB_MENU, single_print_menu_title)


def quit_menu():
    '''Quit menu function and method'''
    print("Quitting this menu now")
    return "exit menu"


def get_name_input(donors_list):
    ''' Function to select user input to return to print function 
        USER INTERACTION'''
    name_input = input(
        "Please enter the name of the donor:  ")

    for donor in donors_list:
        if name_input.lower() in donor.lower():
            donor_check = input(
                "Is this the donor you are looking for: {}?\nPlease type yes or no >> ".format(
                    donor))
            if donor_check == 'yes':
                return donor

    print("{} is not in our records. Let's add {} to our list!".format(
        name_input, name_input))
    while True:
        new_donor_name = input(
            "Please enter the full name of the donor or type 'exit' to quit>> ")
        if new_donor_name == 'exit':
            return "quit"
        name_check = input(
            "Is this the donor name you would like to add: {} ?\nPlease type yes, no, or exit' to quit>> ".format(new_donor_name))
        if name_check == 'yes':
            print("Adding {} to donor list".format(new_donor_name))
            return new_donor_name
        elif name_check == 'exit':
            return "quit"
        else:  # anything other then yes
            print(
                "Let's try entering the donor name again. Or type 'exit' to quit to menu.")


def print_thank_you_total(donor):
    """ prints thank you message"""
    thank_you = '''\n\nDear {}

    Thank you for your most recent generous donation of ${:,.2f}. You're support of ${:,.2f}
    over the years has helped us fund many great programs!We wanted to write you to thank you and that we 
    look forward to your continued support!

    Sincerely,

    The ChickTech Donations Department'''.format(donor.fullname, donor.last_donation(), donor.donations_total())
    return thank_you


def check_number_input():
    '''Error Handling: Checks if number was entered by converting the number to a float'''
    while True:
        try:
            number = float(input('Please enter a donation amount : '))
        except ValueError:
            print("Please enter a number for donation amount!")
        else:
            if number > 0.0:
                print("number  ", type(number))
                return number
            else:
                print('Please enter a donation amount above 0.')


def challenge():
    """Gets user input for donations muliplier challenge. Prints the list to screen for added fun!"""
    print('''Welcome to the Challenge Option. Here you can multiply all donations by any number, 
        or you can multiply donations within an optional min and max donation amount.
        ''')
    try:
        minimum_input = float(
            input('Enter a minimum donation amount (0 if none):  '))
        maximum_input = float(
            input('Enter a maximum donation amount (0 if none):  '))
        factor = float(
            input('Enter the factor you wish to multiply these donations by >>  '))
    except ValueError:
        print('Please follow instructions and enter a number only')

    new_donor_list = mailroom_donors.new_donors_list(
        factor, minimum_input, maximum_input)
    new_donor_list.print_report()
    return new_donor_list


def projected():
    """Gets user input for projection muliplier functionality. Takes min and max and prints contribution."""
    print('''Welcome to the Projection Option. Here you can run projections for contributions. 
        Help Companies structure their matching donations based on past contribution amounts.
        Simply enter the minumum and maximum donation range that will be matched and see the total contribution:''')
    try:
        minimum_input = float(
            input('Enter a minimum donation amount (0 if none):  '))
        maximum_input = float(
            input('Enter a maximum donation amount (0 if none):  '))
        factor = float(
            input('Enter the factor you wish to multiply these donations by >>  '))
    except ValueError:
        print('Please follow instructions and enter a number only')

    projection = mailroom_donors.projection(
        factor, minimum_input, maximum_input)
    print('\nProjected contribution value: ${:,.2f}'.format(projection))


donor1 = Donor("William", "Gates", [326892.24, 122, 22, 12])
donor2 = Donor("Mark",  "Zuckerberg", [30, 60, 65982.55])
donor3 = Donor("Jeff",  "Bezos", [52636.27])
donor4 = Donor("Paul", "Allen", [877.33, 22])
donor5 = Donor("Steven", "Hawking", [326892.24, 123, 123.33, 123, 123])
donor6 = Donor("Justin", "Timberlake", [999658.25, 1233, 123])

mailroom_donors = DonorFunctions(
    [donor1, donor2, donor3, donor4, donor5, donor6])

#------Menu Dictionaries of Dictionaries .Needs to be after the functions or code won't work. ------
MAIN_MENU = {
    "1": {'menu_prompt': 'Send a Single Thank You', 'menu_dispatch': single_print_menu},
    "2": {'menu_prompt': 'Create a Report', 'menu_dispatch': mailroom_donors.print_report},
    "3": {'menu_prompt': 'Send Letters to Everyone', 'menu_dispatch': mailroom_donors.send_letters_everyone},
    "4": {'menu_prompt': 'Test Print All', 'menu_dispatch': mailroom_donors.print_letters_to_everyone},
    "5": {'menu_prompt': 'Challenge', 'menu_dispatch': challenge},
    "6": {'menu_prompt': 'Create Projection', 'menu_dispatch': projected},
    "q": {'menu_prompt': 'Quit Program', 'menu_dispatch': quit_menu}
}
SINGLE_PRINT_SUB_MENU = {
    "1": {'menu_prompt': 'Lookup Donor By Name', 'menu_dispatch': mailroom_donors.send_single_thank_you},
    "2": {'menu_prompt': 'Print List of Donors', 'menu_dispatch': mailroom_donors.print_donors_names},
    "3": {'menu_prompt': 'Print Donors and All Donations', 'menu_dispatch': mailroom_donors.print_donors_and_donations},
    "4": {'menu_prompt': 'Print Donors and Donation Totals', 'menu_dispatch': mailroom_donors.print_donors_and_donation_totals},
    "q": {'menu_prompt': 'Quit to Main Menu', 'menu_dispatch': quit_menu}}


if __name__ == '__main__':
    main_menu()
