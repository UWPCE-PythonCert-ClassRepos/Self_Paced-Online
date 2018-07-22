# ----------------------------------------------------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: Lesson 09 -- Object Oriented mailroom.py
# PURPOSE: To delegate responsibilities of the mailroom.py program and making it more efficient by applying OOP
# principles to simplify objectives and tasks of program scope.
#
# DATE: 07/20/2018
#
# DESCRIPTION: Refactored original mailroom.py to 3 classes (UI, DonorSuite, and Donor)
# all of which have their own constructors and methods. By dividing the tasks into multiple classes it was easier
# to test for errors and debug the program along the way.
# ----------------------------------------------------------------------------------------------------------------------

import os
import datetime
import sys

# ----------------------------------------------------------------------------------------------------------------------
#  ********************************************    class Donor    *****************************************************
# ----------------------------------------------------------------------------------------------------------------------


class Donor:
    """
    Main module for donor data storage and manipulation, contains:
    __init__()
    add_donation()
    get_avg_donation()
    get_thank_you()
    get_thank_you_tofile()
    get_report_row_header()
    get_report_row_list()
    __lt__()
    """

    def __init__(self, name):
        """
        Initializing characteristics to carry through module (e.g. name, donations, avg_donation, and getter)
        :param name:
        """
        self.name = name
        self.donations = []
        self.avg_donation = 0
        self.get_avg_donation()

    def add_donation(self, donation):
        """
        Method adds the entered donation amount from add_name() to the Donor object, and calls get_avg_donation
        to create the next characteristic that will be tracked for the donors.
        :param donation: passed in from add_name()
        :return:
        """
        if type(donation) == list:
            for l in donation:
                self.donations.append(float(l))
        else:
            self.donations.append(float(donation))
        self.get_avg_donation()

    def get_avg_donation(self):
        """
        If donations present, avg will be created (sum_donations)/(num_donations -- len(self.donations) == a list
        with 0:N donations, obtaining the len(self.donations) provides the number of donations in the list which
        keeps track of the number like a counting feature.)
        :return:
        """
        if self.donations:
            self.avg_donation = sum(self.donations) / len(self.donations)

    def get_thank_you(self):
        """
        Returns the thank_you message to donor(s) using 'template' for the message with formatting utilizing
        **kwargs to allow for x number of keyword arguments.

        This format is for in-console viewing.
        :return:
        """

        donor_dict = {'name': self.name, 'donation': self.donations[-1]}

        thankyou_msg = (
                    '''
                        Dear {name},
                        Thank you for your support through your most recent contribution of ${donation:,.2f}. 
                        Your generosity over this year has been instrumental in moving us towards our
                        fundraising goal of $100,000.00 to benefit local charities. On behalf of all 
                        the members of the Foundation, we thank you for your generosity and look forward
                        to working with you in the future to build a better world!
                       
                        Best wishes,

                        Foundation Board of Directors
                       \n'''.format(**donor_dict))
        return thankyou_msg

    def get_thank_you_tofile(self):
        """
        Returns the thank_you message to donor(s) using 'template' for the message with formatting utilizing
        **kwargs to allow for x number of keyword arguments.

        This format is for to-file viewing (no additional \t or \n that would need to be cleaned up).
        :return:
        """
        donor_dict = {'name': self.name, 'donation': self.donations[-1], 'num_donations': len(self.donations)}
        thankyou_file = (
                    '''
Dear {name},

Thank you for your continued support through your most recent contribution of ${donation:,.2f}. 
Your {num_donations} donation(s) over this year have been instrumental in moving towards our
fundraising goal of $100,000.00 to benefit local charities. On behalf of all
the members of the Foundation, we thank you for your generosity and look forward
to working with you in the future to build a better world!

Best wishes,

Foundation Board of Directors
                       \n'''.format(**donor_dict))

        return thankyou_file

    def get_report_row_header(self, donor_header_width):
        """
        Obtains row for each item in donor object and formats for output in create_report()
        :param donor_header_width: (uses the max(len()) from donor_header_width()
        :return:
        """
        return '{:{}}  |  ${:^11.2f}  |  {:^10}  |  ${:^8.2f}'.\
            format(self.name, donor_header_width, sum(self.donations), len(self.donations), self.avg_donation)

    def get_report_row_list(self, donor_name_list):
        """
        Same as above, only used for the list feature in add_names() so it only includes names
        :param donor_name_list:
        :return:
        """
        # donor_name_list
        return '{:{}}  '.format(self.name, donor_name_list)

    def __lt__(self, other):
        """
        Used for comparison of donation amounts.
        :param other:
        :return:
        """
        return sum(self.donations) > sum(other.donations)


# ----------------------------------------------------------------------------------------------------------------------
#  *****************************************   class DonorSuite   *****************************************************
# ----------------------------------------------------------------------------------------------------------------------


class DonorSuite:
    """
    Donor data storage and manipulation class module
    Contains the following methods:
    __init__
    add_donor
    sort_donors
    """
    def __init__(self, donors=[]):
        """
        DonorSuite initializes with variable 'donors' assigned to an empty list
        :param donors: For stored donor data
        """
        self.donors = []
        for donor in donors:            # for individual donor amongst all donors, call method (add_donor)
            self.add_donor(donor)       # method call

    def add_donor(self, donor):
        """
        Adds donors to the 'container'
        :param donor: adding donor to maintained container
        :return: 
        """
        if not isinstance(donor, Donor):
            raise TypeError('Items in DonorSuite must be type \'Donor\'')
        self.donors.append(donor)

    def sort_donors(self):
        """
        Sorts donors based on donations (descending: for report)
        :return: 
        """
        self.donors.sort()

# ----------------------------------------------------------------------------------------------------------------------
#  ********************************************    class UI   ********************************************************
# ----------------------------------------------------------------------------------------------------------------------


class UI:
    """
    User-Interface module, contains the following methods:
    __init__
    start_program
    add_name
    thank_you
    create_report
    create_list
    @staticmethod get_report_header
    @staticmethod get_list_header
    write_letters
    @staticmethod quit_program
    """

    def __init__(self, donor_container):
        """
        Initializer for User Interface class
        :param donor_container: pertains to all information being stored for donors
        """
        self.donor_container = donor_container

    def start_program(self):
        """
        Main display with menu options (methods) for user to select through
        :return:
        """
        selection_dict = {'A': self.add_name, 'B': self.thank_you, 'C': self.create_report,
                          'D': self.write_letters, 'E': self.quit_program, 'Q': self.quit_program}
        while True:
            selection = input('''
--------------------------------------------------------------------------------------------------------------
                                                MAIL ROOM MENU
--------------------------------------------------------------------------------------------------------------

                                             -- Menu Options --

                                        A. Add donor to database
                                        B. Send Thank You letter to specific donor
                                        C. Create a donor report
                                        D. Send letters to all donors
                                        E. Quit
                                        
                                        Menu Selection: ''').upper()
            print()
            try:                                                            # error check
                selection_dict[selection]()
            except ValueError:
                print('Incorrect entry. Please enter A, B, C, D, or E.')

    def add_name(self):
        """
        To shorten methods/allow for quicker data entry (for build-up of content) name/donation
        entry are stand-alone and not tied to the thank_you process. User can enter from 0 to n names
        with associated donation values in this interface to be stored in the donor_container
        :return:
        """
        while True:
            name = input('Please enter first name: ').strip().capitalize()
            if name.lower() == 'list':
                print('Here is the the most current list of donor names:\n')
                self.create_list()
            elif name.upper() == 'Q':
                self.start_program()
            else:
                name += ' '
                l_name = input('Please enter last name: ').strip().capitalize()
                if l_name.lower() == 'list':
                    print('Here is the the most current list of donor names::\n')
                    self.create_list()
                elif name.upper() == 'Q':
                    self.start_program()
                else:
                    name += l_name
                    while True:
                        try:
                            donation = float(input('Enter in the donation amount from Donor {0}: $'.format(name)))
                            break
                        except ValueError:
                            print('Only numerical entries.')
                    for donor in self.donor_container.donors:
                        if name == donor.name:
                            current_donor = donor
                            break
                    else:
                        current_donor = Donor(name)
                        self.donor_container.add_donor(current_donor)

                    current_donor.add_donation(donation)
                    cont = input('Do you want to add additional donors? (Y/N): ').upper()
                    if cont == 'Y':
                        continue
                    else:
                        break

        return

    def thank_you(self):
        """
        Allows user to select specific donor name from container and send thank you.
        :return:
        """
        print('''
                        If you know the name of the donor you wish to thank, enter the name here, or enter "list"
                        to view the all donors within the list.''')
        while True:
            name = input('''
                        User Selection: ''').title()

            if name.lower() == 'list':
                print('Here is the the most current list of donor names::\n')
                for donor in self.donor_container.donors:
                    print(donor.name)
            elif name.upper() == 'Q':
                self.start_program()
            else:
                for donor in self.donor_container.donors:
                    if name == donor.name:
                        current_donor = donor
                        print(current_donor.get_thank_you())
                        again = input('Do you want to go back to the main menu? (Y/N): ').upper()
                        if again == 'Y':
                            self.start_program()
                        else:
                            continue

    def create_report(self):
        """
        Generates neatly formatted report of current donors and associated data (donations, number of
        donations, average donations)
        :return:
        """
        donor_header_width = max([len(donor.name) for donor in self.donor_container.donors])
        print(self.get_report_header(donor_header_width))
        self.donor_container.sort_donors()
        for donor in self.donor_container.donors:
            print(donor.get_report_row_header(donor_header_width))

    def create_list(self):
        """
        Displays header and list of current donor names to user.
        :return:
        """
        donor_name_list = max([len(donor.name) for donor in self.donor_container.donors])
        print(self.get_list_header(donor_name_list))
        self.donor_container.sort_donors()
        for donor in self.donor_container.donors:
            print(donor.get_report_row_list(donor_name_list))

    @staticmethod
    def get_list_header(donor_name_list):
        """
        Simple formatting for donor name heading used for create_list()
        :param donor_name_list: obtains size of donor list from donor_container
        :return:
        """
        return '{:{}}  '.format('Donor Name', donor_name_list)

    @staticmethod
    def get_report_header(donor_header_width):
        """
        Formatting for all headings for create_report()
        :param donor_header_width: obtains size of donor list from donor_container
        :return:
        """
        return '{:{}}  |  {:12}  |  {:10}  |  {:8}'.format('Donor Name', donor_header_width,
                                                           'Total Given', 'Num Gifts', 'Average Gift')

    def write_letters(self):
        """
        Writes thank you letters to all donors in the donor list as a .txt file on current working directory
        (unless other directory specified)
        :return:
        """
        user_dir = input('Change output directory (Y/N)?')
        if user_dir.upper() == 'Y':
            while True:
                try:
                    directory = str(input('\nEnter the file path where you want to write the letters - '
                                          'don\'t forget to use ''two \n\'\\\\\' as file separators to make sure'
                                          ' it is compatible if using Windows - (e.g. \'C:\\\\\': '))
                    os.chdir(directory)
                except FileNotFoundError as e:              # exception handler - prints line of error, and type
                    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                else:
                    today = datetime.datetime.today().strftime('%m-%d-%dY')
                    for donor in self.donor_container.donors:
                        filename = donor.name + '_' + today + '.txt'
                        with open(filename, 'w') as f:
                            print('Writing ' + filename + ' to disk...')
                            f.write(donor.get_thank_you_tofile())
                        print('Finished!')
        else:
            os.getcwd()
            today = datetime.datetime.today().strftime('%m-%d-%Y')
            for donor in self.donor_container.donors:
                filename = donor.name + '_' + today + '.txt'
                with open(filename, 'w') as f:
                    print('Writing ' + filename + ' to disk...')
                    f.write(donor.get_thank_you_tofile())
                print('Finished!')

    @staticmethod
    def quit_program():
        """
        Ends module
        :return:
        """
        sys.exit()

# ----------------------------------------------------------------------------------------------------------------------
#  ********************************************    Display    *******************************************************
# ----------------------------------------------------------------------------------------------------------------------


def main():
    """
    Stand-alone function -- starts by instantiating variables for DonorSuite(), and UI()
    and calls UI(DonorSuite).start_program()
    :return:
    """
    ds = DonorSuite()
    ui = UI(ds)
    ui.start_program()


if __name__ == '__main__':
    main()
