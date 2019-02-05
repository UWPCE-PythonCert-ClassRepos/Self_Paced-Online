#!/usr/bin/env python
# This script maintains a databse of donors including name and donation amounts
import statistics
import datetime

# Define exception to exit script
class ExitScript(Exception): pass

# Create a dict that contains the donors and a history of the amounts they have
# donated
class Donor():
    """Class to contain information about a single donor."""

    def __init__(self, name, donations=None):
        # donations is a list
        self._name = name.lower()
        self._donations = donations if donations is not None else []

    def __repr__(self):
        return 'Donor({}, {})'.format(self.name, self.donations)

    def __str__(self):
        return 'Donor(Name: {}, Donations: {})'.format(self.name,
            self.donations)

    def __eq__(self, other):
        return self.name == other.name and self.donations == other.donations

    @property
    def name(self):
        return self._name.title()

    @property
    def donations(self):
        return self._donations

    @property
    def count_donations(self):
        return len(self._donations)

    @property
    def total_donations(self):
        return sum(self._donations)

    @property
    def average_donation(self):
        return statistics.mean(self._donations)

    def add_donation(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            print('Please enter a number value for donation amount.')
        self._donations.append(amount)

    def thank(self, amount):
        """Return a string thanking donor name for a donation of amount."""
        return f"Dear {self.name},\n\n" + \
            "Thank you so much for your generous donation of " + \
            f"${amount:.2f}.\n\nWe really appreciate your donations " + \
            f"totalling ${self.total_donations:.2f}.\n" + \
            f"You are ${1000000000-self.total_donations:.2f} away from a" + \
            " gift of Spaceballs: The Flamethrower!\n\n" + \
            "Sincerely, The Wookie Foundation"


    @property
    def filename(self):
        """Return filename for a thankyou letter to a donor."""
        d = datetime.date.today()
        # Build file name using donor name and today's date separated by _
        filename = '_'.join([self.name.replace(' ','_'), str(d.month),
            str(d.day), str(d.year)])+'.txt'
        return filename



class DonorDict():
    """A container for Donor objects."""

    def __init__(self):
        self._donors = {}

    def __repr__(self):
        return 'DonorDict Object'

    def __str__(self):
        return str(self._donors)

    def __len__(self):
        return len(self._donors)

    def __getitem__(self, key):
        return self._donors[key.lower()]

    def __delitem__(self, key):
        del self._donors[key]

    def __iter__(self):
        return iter(self._donors.values())

    def __contains__(self, key):
        return key in self._donors

    def names_by_donations(self):
        """Return a list of donor objects sorted by total donation amount."""
        return sorted(self, key=self.sort_key, reverse=True)

    @staticmethod
    def sort_key(x):
        return x.total_donations

    @property
    def donors(self):
        return self._donors

    @property
    def names(self):
        """Return a list of Donors in DonorDict object sorted by name."""
        return sorted([donor.name for donor in self])

    def add_donor(self, name, donations=None):
        """
        Add a donor to a DonorDict object. An optional list of donations
        can be provided as an input.
        """
        self._donors[name.lower()] = Donor(name,donations)

    def add_donation(self, name, amount):
        """Add a donation to a apecified Donor object within DonorDict."""
        print(self[name])
        self[name].add_donation(amount)

    def thank_donor(self, name, amount):
        """Return a string thanking donor name for a donation of amount."""
        amount = float(amount)
        return self[name].thank(amount)

    def report(self):
        """Print a report of donors with summary of their donation history."""
        # Determine table size_report
        table_size = self.size_report()

        # Build format strings for header and table rows
        head_string = '{:{}s} | {:^{}s} | {:^{}s} | {:^{}s}'
        row_string  = '{:{}s} | $ {:>{}.2f} | {:>{}d} | $ {:>{}.2f}'

        # Table header - Add 2 to width of dollar value fields to account for
        # dollar sign and space
        report_str = head_string.format('Donor Name', table_size[0],
            'Total Given', table_size[1]+2, 'Num Gifts', table_size[2],
            'Average Gift', table_size[3]+2) + '\n'
        #report_str = report_str +  ('-'*(sum(table_size) + 13)) + '\n')

        # Table rows
        report_list = []
        for donor in self.names_by_donations():
            report_list.append(row_string.format(donor.name, table_size[0],
                donor.total_donations, table_size[1], donor.count_donations,
                table_size[2], donor.average_donation, table_size[3]))
        return report_str + '\n'.join(report_list)

    def size_report(self):
        """Determine column widths for a donor report."""
        # Determine width of columns based on data in donors data structure
        # Convert numbers to strings to determine their length in characters
        # Convert the dollar amounts to an integer to remove decimal places (since
            # there are an unknown number of them), then add 3 to the length to
            # accomodate for a period and 2 decimal places
        # Ensure column size is at least as wide as header text

        name_width = max(len(donor.name) for donor in self)
        name_width = max(name_width, len('Donor Name'))

        total_width = max(len(str(int(donor.total_donations))) for donor in
            self)+3
        total_width = max(total_width, len('Total Given'))

        num_width = max(len(str(donor.count_donations)) for donor in self)
        num_width = max(num_width, len('Num Gifts'))

        avg_width = max(len(str(int(donor.average_donation))) for donor in
            self)+3
        avg_width = max(avg_width, len('Average Gift'))

        return [name_width, total_width, num_width, avg_width]

    def thank_all_donors(self):
        """Send letters to all donors thanking them for most recent donation."""
        for donor in self:
            with open(donor.filename, 'w') as f:
                f.write(donor.thank(donor.donations[-1]))
            f.closed

# Define main menu functions
def add_donation():
    """Add a donation to donors dict and compose a thank you email."""
    while True:
        name = input("Enter the donor's Full Name, or 'list': ").lower()
        if name == 'return':
            return
        elif name == 'list':
            for name in donors.names:
                print(name)
        else:
            if name not in donors:
                donors.add_donor(name)
            break

    while True:
        amount = input('Enter the donation amount: ')
        if amount.lower() == 'return':
            # Remove donor from donors if user chooses to return
            del donors[name]
            return
        try:
            donors.add_donation(name, amount)
            break
        except ValueError:
            print('Please enter a number value for donation amount.')

    print(); print(donors.thank_donor(name, amount))


# Define main menu functions
def create_report():
    """Print a report of donors with a summary of their donation history."""
    print(donors.report())

def send_letters():
    """Send letters to all donors thanking them for most recent donation."""
    donors.thank_all_donors()

def quit():
    raise ExitScript


if __name__ == '__main__':

    donors = DonorDict()
    donors.add_donor('han solo', [3468.34, 457, 34.2])
    donors.add_donor('luke skywalker', [5286286.3, 567, 23.5678])
    donors.add_donor('chewbacca', [432, 679.4553])
    donors.add_donor('princess leia', [5.3434])
    donors.add_donor('bobba fett, bounty hunter', [67])

    actions = {
    '1': add_donation,
    '2': create_report,
    '3': send_letters,
    '4': quit
    }

    # User interaction
    while True:
        try:
            # Main menu - prompt user for an action
            print('''
                \nSelect an action to perform...\n
                Type "return" at any time to return to main menu.\n
                ''')
            action = input('''
                1: Send a Thank You
                2: Create a Report
                3: Send Letters to Everyone
                4: Quit\n
                ''')
            actions.get(action)()
        except ExitScript:
            break
        except TypeError:
            if action not in actions:
                continue


# # Define main menu functions
# def add_donation():
#     """Add a donation to donors dict and compose a thank you email."""
#     while True:
#         name = input("Enter the donor's Full Name, or 'list': ").lower()
#         if name == 'return':
#             return
#         elif name == 'list':
#             print(donors.names)
#         else:
#             donors.add_donor(name)
#             break
#
#     while True:
#         amount = input('Enter the donation amount: ')
#         if amount.lower() == 'return':
#             # delete donor?
#             return
#         try:
#             donors.add_donation(name, amount)
#         except ValueError:
#             print('Please enter a number value for donation amount.')
#
#     print(donors.thank_donor(name, amount))
#
#
# def create_report():
#     """Print a report of donors with a summary of their donation history."""
#     print(donors.report())
#
# def send_letters():
#     """Send letters to all donors thanking them for most recent donation."""
#     donors.thank_all_donors()
#
# def quit():
#     raise ExitScript

# # Define sub-functions
# def build_filename(info):
#     """Build up a filename for a thankyou letter to a donor."""
#     d = datetime.date.today()
#     # Build file name using donor name and today's date separated by _
#     filename = '_'.join([info['name'].replace(' ','_'), str(d.month),
#         str(d.day), str(d.year)])+'.txt'
#     return filename

# def donor_name(name):
#     """Add a donor name to the donors dict or display list of donors."""
#     if name.lower() == 'return':
#         raise MainMenu
#     elif name.lower() == 'list':
#         # If the user enters list, display a list of donor names
#         print_names()
#     else:
#         # If the user enters a name, add it to the donors dict
#         # structure if not already there.
#         donors.setdefault(name.lower(),{'name': name, 'donations': []})
#         return True
#
# def donor_amount(amount,name):
#     """Add a donation amount to the donors dict for donor name."""
#     if amount.lower() == 'return':
#         raise MainMenu

    # try:
    #     # Try to add donation amount to donors data structure
    #     amount = float(amount)
    #     donors[name.lower()]['donations'].append(amount)
    #     return True
    # except ValueError:
    #     # If value is not a number, ask the user to enter a number
    #     print('Please enter a number value for donation amount.')

# def print_names():
#     """Print the list of donor names in alphabetical order."""
#     for donor in sorted(donors):
#         print(donors[donor]['name'])

# def compose_email(donor):
#     """Print an email to the command line thanking donor name for a donation
#     of amount."""
#     name=donors[donor.lower()]['name']
#     amount=donors[donor.lower()]['donations'][-1]
#     total = sum(donors[donor]['donations'])
#     balance = 1000000000-total
#     return f"""
#         Dear {name},\n
#         Thank you so much for your generous donation of ${amount:.2f}.\n
#         We really appreciate your donations totalling ${total:.2f}. You are
#         ${balance:.2f} away from a gift of Spaceballs: The Flamethrower!\n
#         Sincerely, The Wookie Foundation
#         """
#
# def size_report(in_dict):
#     """Determine column widths for a donor report."""
#     # Determine width of columns based on data in donors data structure
#     # Convert numbers to strings to determine their length in characters
#     # Convert the dollar amounts to an integer to remove decimal places (since
#         # there are an unknown number of them), then add 3 to the length to
#         # accomodate for a period and 2 decimal places
#     # Ensure column size is at least as wide as header text
#
#     name_width = max(len(name) for name in in_dict)
#     name_width = max(name_width, len('Donor Name'))
#
#     total_width = max(len(str(int(sum(value['donations'])))) for value in
#         in_dict.values())+3
#     total_width = max(total_width, len('Total Given'))
#
#     num_width = max(len(str(len(value['donations']))) for value in
#         in_dict.values())
#     num_width = max(num_width, len('Num Gifts'))
#
#     avg_width = max(len(str(int(statistics.mean(value['donations'])))) for
#         value in in_dict.values())+3
#     avg_width = max(avg_width, len('Average Gift'))
#
#     return [name_width, total_width, num_width, avg_width]
#
# def sort_donors():
#     """Sort donors dict in order of total amount donated."""
#     return sorted(donors,key=sort_fun, reverse=True)
#
# def sort_fun(x):
#     """"Sort function for use in sort_donors. x is a value in donors
#     (type dict)"""
#     return sum(donors[x]['donations'])

# # Dict of possible main menu actions the user can select
# actions = {
# '1': add_donation,
# '2': create_report,
# '3': send_letters,
# '4': quit
# }
#
#
# # User interaction
# if __name__ == '__main__':
#     while True:
#         try:
#             # Main menu - prompt user for an action
#             print(); print('Select an action to perform...')
#             print('Type "return" at any time to return to main menu.')
#             action = input('1: Send a Thank You\n2: Create a Report\n' +\
#             '3: Send Letters to Everyone\n4: Quit\n')
#
#             actions.get(action)()
#         except ExitScript:
#             break
#         except TypeError:
#             continue
