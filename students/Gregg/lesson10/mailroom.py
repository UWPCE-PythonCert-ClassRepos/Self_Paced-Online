#!/usr/bin/env python3
"""Use current knowledge to set up an interactive program"""

import datetime
from collections import defaultdict
import logging

donations_init = {
    "William Gates, III": [3, 5, 7],
    "Mark Zuckerberg": [4.50, 8, 2],
    "Jeff Bezos": [7.77],
    "Paul Allen": [3.6, 4.5],
    "bob": [.01]
}
#donations = defaultdict(list, donations)
# todo
# add file writing

class Donor():


    def __init__(self, name_in, donations=None):
        self.name = name_in
        if donations is not None:
            try:
                self._donation_list = list(donations)
            except TypeError as E:
                self._donation_list = [donations]
        else:
            self._donation_list = []

    def add_donation(self, donation_amount):
        """Add a dontation to to the database for donor"""
        donation_amount = float(donation_amount)
        if donation_amount <= 0:
            raise(ValueError)
        self._donation_list.append(donation_amount)

    def send_thank_you(self, this_thx_string):
        """send the thank you to the donor"""
        # leaving this as a sperate function because at some point I expect
        # to actually do things other than printing here
        print(f"Heres the thank you that should be sent to {self.name}:")
        print(this_thx_string)
        print('')

    def new_donation_handler(self, donation_amount):
        """add a donation to the list for given donor in donations dict"""
        try:
            self.add_donation(donation_amount)
        except (ValueError, TypeError) as E:
            print(f'{donation_amount} is not a valid donation amount, please enter a number greater than 0')
            raise(E)
        this_thx_string = self.last_don_thx_string
        self.send_thank_you(this_thx_string)

    @property
    def stats(self):
        """retrieve the statistics for a given donor"""
        donors_donations = self.all_donations
        total = sum(donors_donations)
        num = len(donors_donations)
        try:
            avg = total / num
        except ZeroDivisionError as E:
            avg = 0
        return self.name, total, num, avg

    @property
    def all_donations(self):
        """Return a list of all amounts made by donor ordered chronologically"""
        return self._donation_list

    line1 = 'Dear {},\n\n'
    line2 = '\tThank you for you generous donation of ${:.2f}.\n\n'
    line3 = '\tIt will be put to good use.\n\n'
    line4 = 'Sincerely,\n'
    line5 = '-The team'

    thankyou_string = (
        '{}{}{}{:>40}{:>45}'.format(line1, line2, line3, line4, line5).format
    )

    @property
    def last_don_thx_string(self):
        return self.thankyou_string(self.name, self.last_donation)

    def send_letter(self, letter_filename):
        """Send a thank you letter to a donor for the most recent donation"""
        try:
            donor_thx_string = self.last_don_thx_string
        except TypeError as E:
            print((
                "{0} is in our database but has not made a donation.\n"
                "No thank you was saved for {0}"
            ).format(self.name)
            )
        else:
            with open(letter_filename, 'w') as letter:
                letter.write(donor_thx_string)
            print(f'Sent letter to {self.name}')

    @property
    def last_donation(self):
        """Return the value of the last donation made by donor"""
        try:
            last_donation = self.all_donations[-1]
        except IndexError as E:
            last_donation = None
        # This is currently pointelss because the default dict took care of the
        # the situation where a donor would need to be added seperatley from their
        # donation. I will leave it in anyway in case it comes again in the future
        return last_donation



class Donations_db():

    def __init__(self, donor_dict = None):
        self._donors = []
        self._mp_scale_factor = None
        self._mp_min_donation = None
        self._mp_max_donation = None
        if donor_dict is not None:
            for name, donations in donor_dict.items():
                self.add_donor(name, donations)

    def add_donor(self, name, donations=None):
            donor = Donor(name, donations)
            self._donors.append(donor)

    def list_donors(self):
        """print all the donors currently as keys of donations dictionary"""
        self.print_list(self.names_in_database, 'donors')

    @property
    def mp_scale_factor(self):
        return self._mp_scale_factor

    @mp_scale_factor.setter
    def mp_scale_factor(self, scale_factor_in):
        try:
            assert(int(scale_factor_in) > 0)
            self._mp_scale_factor = int(scale_factor_in)
        except (ValueError, TypeError) as E:
            print('The match per dollar should be greater than 0')
            raise(E)


    @property
    def mp_min_donation(self):
        return self._mp_min_donation

    @mp_min_donation.setter
    def mp_min_donation(self, min_donation_in):
        try:
            self._mp_min_donation = int(min_donation_in)
        except ValueError as E:
            if min_donation_in.lower() == 'none':
                self._mp_min_donation = None
            else:
                print('The minimum donation must be a number or None')
                raise(E)

    @property
    def mp_max_donation(self):
        return self._mp_max_donation

    @mp_max_donation.setter
    def mp_max_donation(self, max_donation_in):
        try:
            self._mp_max_donation = int(max_donation_in)
        except ValueError as E:
            if max_donation_in.lower() == 'none':
                self._mp_max_donation = None
            else:
                print('The maximum donation must be a number or None')
                raise(E)


    def donor_from_name(self, name):
        for donor in self._donors:
            if donor.name == name:
                return donor

    @property
    def names_in_database(self):
        """Retunr the donors in the database"""
        # putting this in in case the data strict changes
        name_list = []
        for donor in self._donors:
            name_list.append(donor.name)
        return name_list

    def send_letters(self, filename_sufffix = None):
        """Send letters to the donors in the DB that have made donations"""
        if filename_sufffix is None:
            filename_sufffix = datetime.datetime.now().strftime("%m.%d.%Y.%H.%M.%S")
        for donor in self._donors:
            letter_filename = "{}_{}.txt".format(donor.name, filename_sufffix)
            donor.send_letter(letter_filename)

    @property
    def donation_report(self):
        """Create a report of summarry statistics for the current database

        The columns are name, total, number and average
        """
        row_list = []
        headers = 'Donor name', 'Total Given', 'Num Gifts', 'Average Gift'
        format_column_header = "{:<26}|{:^13}|{:^13}|{:^13}".format
        row_list.append(format_column_header(*headers))
        row_list.append('_' * 68)

        donor_rows_list = [donor.stats for donor in self._donors]
        donor_rows_list.sort(key=self.key1, reverse=True)

        format_row = "{:<27}${:>12.2f} {:>12}  ${:>12.2f}".format
        row_list.extend([
            format_row(*row)
            for row in donor_rows_list
        ])
        report_string = ('\n').join(row_list)
        return report_string

    def print_report(self):
        """Print report to prompt"""
        print(self.donation_report)

    def new_donation_handler(self, name, donation_amount):
        donor = self.donor_from_name(name)
        donor.new_donation_handler(donation_amount)


    def scaled_database(self, scale_factor, min_donation=0, max_donation=None):
        scaled_db = Donations_db()
        def in_this_range(value):
            return self.in_range(value, min_donation, max_donation)

        def this_scale(value):
            return self.scale(value, scale_factor)

        for donor in self._donors:
            filtered_donations = filter(in_this_range, donor._donation_list)
            scaled_donations = map(this_scale, filtered_donations)
            scaled_db.add_donor(donor.name, scaled_donations)
        return scaled_db

    def matching_projection(self, scale_factor, min_donation=0, max_donation=None):
        scaled_db = self.scaled_database(scale_factor, min_donation, max_donation)
        filtered_db = self.scaled_database(1, min_donation, max_donation)
        scaled_total = scaled_db.total_donations
        matching_contribution = scaled_total - filtered_db.total_donations
        return matching_contribution

    @staticmethod
    def scale(value, scale_factor):
        return scale_factor * value

    @staticmethod
    def in_range(value, min_donation=0, max_donation=None):
        above_min = min_donation is None or value >= min_donation
        below_max = max_donation is None or value <= max_donation
        return above_min and below_max


    @property
    def total_donations(self):
        total_donations = sum([
            sum(donor._donation_list)
            for donor in self._donors
        ])
        return round(total_donations, 2)

    @staticmethod
    def key1(iterable):
        """Sort key for creating report"""
        return iterable[1]

    @staticmethod
    def print_list(list_in, descriptor_str):
            """prints the elements of the list with some nice UI text"""
            # makes it more flexible so I could print other lists if I wanted to
            # such as the donations for a given donor
            print("These are the {} currently in the database:".format(descriptor_str))
            print('\n'.join(list_in))
            print('')

donation_db = Donations_db(donations_init)

def menu(prompt, menu_dict, quit_string='q'):
    """Continues prompting with prompt until the quit_string is returned

    Prompt handler is set up to return values based on the functions in
    action_list, so one of these functions should return the quit_string
    otherwise there is no way to quit
    """
    def menu_function(key_in):
        menu_handler(key_in, menu_dict)

    while(True):
        result = quitable_function_prompt(prompt, menu_function, quit_string)
        if result is not None:
            break


def menu_handler(key_in, menu_dict):
    """use a switch dict to choose route the program based on input

    includes nice handling of invlaid options
    """
    try:
        selected_action = menu_dict[key_in]
    except KeyError as E:
        print("That isn't one of the menu options")
        raise(E)
    else:
        selected_action()


def quitable_function_prompt(prompt, function_in, quit_string='q'):
    """Runs function with user input unless input is quit string

    Will repeat if the input is invalid
    """
    while True:
        result = input(prompt_formatter(prompt))
        print('')
        if result == quit_string:
            return result
        try:
            function_in(result.upper())
            return None
        except (KeyError, ValueError) as E:
            # I feel like maybe these should be custom errors?
            # made dbugging a bit of a pain
            print('Unable to continue, please try again')


prompt_formatter = '{}\nInput: '.format


def primary_menu():
    """Guide user through the mailroom UI"""
    menu(primary_prompt, primary_switch_dict, quit_string='Q')


primary_prompt = (
    "\nWould you like to Send a Thank You (enter TY), "
    "Create a Report (enter CR), send thank you letters to everyone (enter SL)"
    ", run a projection for matching contributions (enter MP)"
    " or quit (enter Q).\n"
    "At any point enter q to return to this prompt"
)


def prompt_thank_you():
    """Guide user to create a thank you for a new donation"""
    quitable_function_prompt(thank_you_prompt, thank_you)


def thank_you(donor):
    """Prompt the necessary actions to send thankyou to donor"""
    #print(donor)
    if donor.lower() == 'list':
        donation_db.list_donors()
        prompt_thank_you()
    else:
        add_donation_prompt = f"How much did {donor} donate today?"
        if not(donor in donation_db.names_in_database):
            print(f'{donor} is not in our database yet, lets add them.\n')
            donation_db.add_donor(donor)
        def add_donation_for_donor(donation_amount):
            donation_db.new_donation_handler(donor, donation_amount)
        quitable_function_prompt(add_donation_prompt, add_donation_for_donor)

thank_you_prompt = (
    "Enter a full name to send them a thank you\n"
    "Enter 'list' to see current donors"
)

def prompt_match_projection1():
    """Guide user to create a matching projection with scale, min and max"""
    quitable_function_prompt(projection_prompt_1, prompt_match_projection2)

def prompt_match_projection2(min_donation):
    donation_db.mp_min_donation = min_donation
    quitable_function_prompt(projection_prompt_2, prompt_match_projection3)

def prompt_match_projection3(max_donation):
    donation_db.mp_max_donation = max_donation
    quitable_function_prompt(projection_prompt_3, prompt_match_projection4)

def prompt_match_projection4(scale_factor):
    donation_db.mp_scale_factor = scale_factor
    try:
        contribution = donation_db.matching_projection(
            donation_db.mp_scale_factor+1,
            donation_db.mp_min_donation,
            donation_db.mp_max_donation
        )
        print(match_string(
            donation_db.mp_min_donation,
            donation_db.mp_max_donation,
            donation_db.mp_scale_factor,
            contribution
        ))
    except Exception as E:
        logging.exception(E)
        raise(E)



projection_prompt_1 = (
    "Please enter the minimum donaion to match "
    "(enter \"None\" to opt for no minumum):"
)

projection_prompt_2 = (
    "Please enter the maximum donaion to match "
    "(enter \"None\" to opt for no minumum):"
)

projection_prompt_3 = (
    "Please enter the amount you want to match for each $1 in the range:"
)

match_string = (
    "If you chose to match all donations between ${} and ${} and match "
    "${} on the dollar, then you would've contributed total of ${} based on our "
    "current donations".format
)


primary_switch_dict = {
    'TY': prompt_thank_you,
    'CR': donation_db.print_report,
    'SL': donation_db.send_letters,
    'MP': prompt_match_projection1
}



if __name__ == "__main__":

    print("Welcome to Gregg's Mailroom 1.3\n")
    primary_menu()
