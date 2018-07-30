# ----------------------------------------------------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: Lesson 10 -- Functional Programming mailroom_fp.py
# PURPOSE: To delegate responsibilities of the mailroom.py program and making it more efficient by applying OOP
# principles to simplify objectives and tasks of program scope.
#
# DATE: 07/25/2018
#
# DESCRIPTION: Program functions much the same as lesson 9's mailroom module (class/method structure for entering
# and accessing donor information. Lesson 10 includes the new methods:
#
#                                               - donor_projections()
#                                               - existing_donors()
#                                               - count_matches()
#                                               - filter_count()
#
# these methods create the 'philanthropist' functions that were required for this assignment (allowing for the entry
# of a min/max filter against existing donation values and then a matching factor for the philanthropist to match
# such donations by.
#
# ----------------------------------------------------------------------------------------------------------------------

import os
import datetime
import sys
from copy import deepcopy

# ----------------------------------------------------------------------------------------------------------------------
#  ********************************************    class Donor    *****************************************************
# ----------------------------------------------------------------------------------------------------------------------


class Donor:
    """
    Main module for donor data storage and manipulation, contains:
    __init__
    add_donation
    set_avg_donation
    get_thank_you
    get_thank_you_tofile
    get_report_row_header
    get_report_row_list
    __lt__
    sum_the_donations
    filter_projections
    filter_count
    multiply_projections
    """

    def __init__(self, name):
        """
        Initializing characteristics to carry through module (e.g. name, donations, avg_donation, and getter)
        :param name:
        """
        self.name = name
        self.donations = []
        self.avg_donation = 0
        self.sum_donations = 0
        self._donation_size = 0
        self.set_avg_donation()

    def add_donation(self, donation):
        """
        Method adds the entered donation amount from ui_add_name() to the Donor object, and calls set_avg_donation
        to create the next characteristic that will be tracked for the donors.
        :param donation: passed in from ui_add_name()
        :return:
        """
        if type(donation) == list:
            for l in donation:
                self.donations.append(float(l))
        else:
            self.donations.append(float(donation))
        self.set_avg_donation()

    def set_avg_donation(self):
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
        return '{:{}}  |  ${:>14,.2f}  |  {:^10}  |  ${:>10,.2f}'.\
            format(self.name, donor_header_width, sum(self.donations),
                   len(self.donations), self.avg_donation)

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

    def sum_the_donations(self):
        """
        Sums all donations for all donors regardless of min/max
        :return: 
        """
        self.sum_donations = sum(self.donations)

    # noinspection PyAttributeOutsideInit
    def filter_projections(self, min_don, max_don):
        """
        Filters results in deep copy of donor data by user entries for min/max donation
        values.
        :param min_don: minimum allowable donation value to filter for
        :param max_don: maximum allowable donation value to filter for
        :return: 
        """
        if min_don:
            self.donations = list(filter(lambda x: x >= min_don, self.donations))
        if max_don:
            self.donations = list(filter(lambda x: x <= max_don, self.donations))

    def filter_count(self, min_don=False, max_don=False):
        """
        Similar to filter_projections, counts the number of times criteria are met in 
        min/max search.
        :param min_don: ""
        :param max_don: ""
        :return: 
        """
        if min_don == max_don and min_don is not False:
            self.donations = list(filter(lambda x: x >= min_don, self.donations))
            self.donations = list(filter(lambda x: x <= max_don, self.donations))

        else:
            if min_don is not False:
                self.donations = list(filter(lambda x: x >= min_don, self.donations))

            if max_don is not False:
                self.donations = list(filter(lambda x: x <= max_don, self.donations))

        return self.donations

    def multiply_projections(self, factor):
        """
        Multiplies donations within min/max donation criteria by factor of user's choice
        :param factor: float passed in by user
        :return: 
        """
        self.donations = list(map(lambda x: x * factor, self.donations))


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
    matching_factor
    count_matches
    sum_all_donations
    """

    # noinspection PyDefaultArgument
    def __init__(self, donors=[]):
        """
        DonorSuite initializes with variable 'donors' assigned to an empty list
        :param donors: For stored donor data
        """
        self.donors = []
        self.sum_donations = 0
        self.donors_filtered = 0
        self.full_copy = None
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

    def matching_factor(self, factor_match, min_don=False, max_don=False):
        """
        Calls filter method and multiplication method on user entries for donations.
        :param factor_match: donation amount to be matched by factored amount (e.g. 1:1, 2:1)
        :param min_don: float amount that is the lowest end to allow within scope
        :param max_don: float amount that is the highest end to allow within scope
        :return:
        """
        copy_donors = deepcopy(DonorSuite(donors=self.donors))
        for donor in copy_donors.donors:
            donor.filter_projections(min_don, max_don)
            donor.multiply_projections(factor_match)
        return copy_donors

    # noinspection PyProtectedMember
    def count_matches(self, min_don=False, max_don=False):
        """
        Calls filter method to filter values that will be within criteria set by user, counts
        number of values that meet criteria, returns number to user for display in UI.
        :param min_don: ""
        :param max_don: ""
        :return:
        """
        count_list = []
        deep_c = deepcopy(DonorSuite(donors=self.donors))
        for item in deep_c.donors:
            item.filter_count(min_don, max_don)
            count_list.append(Donor.filter_count(item))

        sub_list = [x for x in count_list if x]
        number_matches = len(sub_list)

        return number_matches

    def sum_all_donations(self):
        """
        Method accesses Donor() and sums all donation amounts to be passed back to UI for display
        :return:
        """
        self.sum_donations = 0
        for donor in self.donors:
            donor.sum_the_donations()
            self.sum_donations += donor.sum_donations


# ----------------------------------------------------------------------------------------------------------------------
#  ********************************************    class UI   ********************************************************
# ----------------------------------------------------------------------------------------------------------------------


class UI:
    """
    User-Interface module, contains the following methods:
    __init__
    start_program
    donor_projections
    existing_donors
    ui_add_name
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
        selection_dict = {'A': self.donor_projections, 'B': self.ui_add_name, 'C': self.thank_you,
                          'D': self.create_report, 'E': self.write_letters, 'F': self.quit_program,
                          'Q': self.quit_program}
        while True:
            selection = input('''
--------------------------------------------------------------------------------------------------------------
                                                MAIL ROOM MENU
--------------------------------------------------------------------------------------------------------------

                                             -- Menu Options --
                                        
                                        A. Run donor Projections
                                        B. Add donor to database
                                        C. Send Thank You letter to specific donor
                                        D. Create a donor report
                                        E. Send letters to all donors
                                        F. Quit
                                        
                                        Menu Selection: ''').upper()
            try:                                                            # error check
                selection_dict[selection]()
            except ValueError:
                print('\n\nIncorrect entry. Please enter A, B, C, D, or E.')

    def donor_projections(self):
        """

        :return:
        """
        print('''
--------------------------------------------------------------------------------------------------------------
                                               Projections Set-up
--------------------------------------------------------------------------------------------------------------
                
''')
        min_don = float(input(
                '''                      Enter the minimum donation amount to match: '''))
        max_don = float(input(
                '''                      Enter the maximum donation amount to match: '''))

        factor_match = float(input(
                '''                      Enter the factor amount to match: '''))

        self.donor_container.sum_all_donations()
        number_matches = self.donor_container.count_matches(min_don, max_don)

        print('                      Number of donations that match your criteria: {:}'.format
              (number_matches))
        print('                      The current total of all donations is ${:,.2f}'.format
              (self.donor_container.sum_donations))

        print('                      With the above configuration, your obligation will be: ', end='')
        match_container = self.donor_container.matching_factor(factor_match, min_don, max_don)
        match_container.sum_all_donations()
        print('${:,.2f}'.format(match_container.sum_donations))
        
    def existing_donors(self):
        """
        
        :return: 
        """
        donor1 = Donor('Harry Potter')
        donor1.add_donation(300)
        self.donor_container.add_donor(donor1)

        donor2 = Donor('Ron Weasley')
        donor2.add_donation(100)
        self.donor_container.add_donor(donor2)

        donor3 = Donor('Hermione Granger')
        donor3.add_donation(2600)
        donor3.add_donation(200)
        donor3.add_donation(200)
        self.donor_container.add_donor(donor3)

        donor4 = Donor('Severus Snape')
        donor4.add_donation(1000)
        self.donor_container.add_donor(donor4)

        donor5 = Donor('Albus Dumbledore')
        donor5.add_donation(500)
        self.donor_container.add_donor(donor5)

        donor6 = Donor('Minerva McGonagall')
        donor6.add_donation(1775)
        self.donor_container.add_donor(donor6)

        donor7 = Donor('Rubeus Hagrid')
        donor7.add_donation(65)
        donor7.add_donation(150)
        donor7.add_donation(280)
        donor7.add_donation(495)
        donor7.add_donation(50)
        self.donor_container.add_donor(donor7)

        return
        
    def ui_add_name(self):
        """
        To shorten methods/allow for quicker data entry (for build-up of content) name/donation
        entry are stand-alone and not tied to the thank_you process. User can enter from 0 to n names
        with associated donation values in this interface to be stored in the donor_container
        :return:
        """
        while True:
            print()
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
        print()
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
        return '{:{}}  |  {:>15}  |  {:>10}  |  {:>10}'.format('Donor Name', donor_header_width,
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
    ui.existing_donors()
    ui.start_program()


if __name__ == '__main__':
    main()
