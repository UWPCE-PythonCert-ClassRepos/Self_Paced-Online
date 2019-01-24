#!/usr/bin/env python
# This script maintains a databse of donors including name and donation amounts
import statistics
import datetime
import copy
from itertools import filterfalse

# Define exception to exit script
class ExitScript(Exception): pass


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

    def __iter__():
        return self.donations

    def __eq__(self, other):
        return self.name == other.name and \
            sorted(list(map(lambda x: float(x), self.donations))) == \
            sorted(list(map(lambda x: float(x), other.donations)))

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


class DonorDict():
    """A container for Donor objects."""

    def __init__(self, donors=None):
        self._donors = {}
        if donors is not None:
            for donor in donors:
                self.add_donor(donor)

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

    def __sub__(self, other):
        return self.total_donations - other.total_donations

    def __eq__(self, other):
        for donor in self:
            if donor.name.lower() not in other:
                return False
            if donor != other[donor.name]:
                return False
        return True

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

    @property
    def total_donations(self):
        return sum(donor.total_donations for donor in self)

    def add_donor(self, name, donations=None):
        """
        Add a donor to a DonorDict object. An optional list of donations
        can be provided as an input.
        """
        if isinstance(name, Donor):
            self._donors[name.name.lower()] = name
        else:
            self._donors[name.lower()] = Donor(name,donations)

    def add_donation(self, name, amount):
        """Add a donation to a apecified Donor object within DonorDict."""
        print(self[name])
        self[name].add_donation(amount)


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

    print(); print(thank_donor(donors, name, amount))

def create_report():
    """Print a report of donors with a summary of their donation history."""
    print(report(donors))

def send_letters():
    """Send letters to all donors thanking them for most recent donation."""
    thank_all_donors(donors)

def match_donations():
    """Match all donations by multiplying by a user-specified factor."""
    global donors
    donors = match(donors)

def project_donations():
    """
    Given a multiplication factor, display to the user their projected
    donation total.
    """
    projected_donors = match(donors)
    print(f"\nYour donation of ${projected_donors - donors:.2f} would " +\
        "increase The Wookie Foundation's endowment from " +\
        f"${donors.total_donations:.2f} to "+\
        f"${projected_donors.total_donations:.2f}")

def quit():
    raise ExitScript

# Define sub-functions
def report(donor_dict):
    """Print a report of donors with summary of their donation history."""
    # Determine table size_report
    table_size = size_report(donor_dict)

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
    for donor in donor_dict.names_by_donations():
        report_list.append(row_string.format(donor.name, table_size[0],
            donor.total_donations, table_size[1], donor.count_donations,
            table_size[2], donor.average_donation, table_size[3]))
    return report_str + '\n'.join(report_list)

def size_report(donor_dict):
    """Determine column widths for a donor report."""
    # Determine width of columns based on data in donors data structure
    # Convert numbers to strings to determine their length in characters
    # Convert the dollar amounts to an integer to remove decimal places (since
        # there are an unknown number of them), then add 3 to the length to
        # accomodate for a period and 2 decimal places
    # Ensure column size is at least as wide as header text

    name_width = max(len(donor.name) for donor in donor_dict)
    name_width = max(name_width, len('Donor Name'))

    total_width = max(len(str(int(donor.total_donations))) for donor in
        donor_dict)+3
    total_width = max(total_width, len('Total Given'))

    num_width = max(len(str(donor.count_donations)) for donor in donor_dict)
    num_width = max(num_width, len('Num Gifts'))

    avg_width = max(len(str(int(donor.average_donation))) for donor in
        donor_dict)+3
    avg_width = max(avg_width, len('Average Gift'))

    return [name_width, total_width, num_width, avg_width]

def thank_all_donors(donor_dict):
    """Send letters to all donors thanking them for most recent donation."""
    for donor in donor_dict:
        with open(filename(donor), 'w') as f:
            f.write(thank(donor, donor.donations[-1]))
        f.closed

def thank_donor(donor_dict, name, amount):
    """Return a string thanking donor name for a donation of amount."""
    amount = float(amount)
    return thank(donor_dict[name], amount)

def thank(donor, amount):
    """Return a string thanking donor name for a donation of amount."""
    return f"Dear {donor.name},\n\n" + \
        "Thank you so much for your generous donation of " + \
        f"${amount:.2f}.\n\nWe really appreciate your donations " + \
        f"totalling ${donor.total_donations:.2f}.\n" + \
        f"You are ${1000000000-donor.total_donations:.2f} away from a" + \
        " gift of Spaceballs: The Flamethrower!\n\n" + \
        "Sincerely, The Wookie Foundation"

def filename(donor):
    """Return filename for a thankyou letter to a donor."""
    d = datetime.date.today()
    # Build file name using donor name and today's date separated by _
    filename = '_'.join([donor.name.replace(' ','_'), str(d.month),
        str(d.day), str(d.year)])+'.txt'
    return filename

def match(donors):
    """
    Take user input for matching gifts and return updated DonorDict object.
    """
    while True:
        factor = input('Please enter a multiplication factor for matching' + \
            ' gifts:')
        if factor.lower() == 'return':
            return
        try:
            factor = float(factor)
            if factor <= 1:
                print("Multiplication factor must be greater than 1," +\
                    " otherwise you're stealing money from the poor wookies.")
                continue
            break
        except ValueError:
            print('Value must be a number.')

    while True:
        min_donation = input('Please enter min donation for matching gifts ' +\
            'or press Enter for none:')
        if min_donation.lower() == 'return':
            return
        if not min_donation:
            min_donation = None
            break
        try:
            min_donation = float(min_donation)
            break
        except ValueError:
            print('Value must be a number.')
    while True:
        max_donation = input('Please enter max donation for matching gifts ' +\
            'or press Enter for none:')
        if max_donation.lower() == 'return':
            return
        if not max_donation:
            max_donation = None
            break

        try:
            max_donation = float(max_donation)
            if min_donation and max_donation <= min_donation:
                print('Max donation must be greater than min donation.')
                continue
            break
        except ValueError:
            print('Value must be a number.')
    return challenge(donors, factor, min_donation=min_donation,
        max_donation=max_donation)

def challenge(donor_dict, factor, min_donation=None, max_donation=None):
    """
    Return a new DonorDict object with all donations in donor_dict
    multiplied by factor. Keyword arguments min_donation and max_donation
    specify range of donations to be multiplied.
    """
    new_donors = DonorDict()
    for donor in donor_dict:
        donations = donor.donations
        if min_donation:
            leftover_donations_min = list(filterfalse(lambda x: x >= min_donation,
                donations))
            donations = list(filter(lambda x: x >= min_donation, donations))

        if max_donation:
            leftover_donations_max = list(filterfalse(lambda x: x <= max_donation,
                donations))
            donations = list(filter(lambda x: x <= max_donation, donations))
        new_donations = list(map(lambda x: x*factor, donations))
        try:
            new_donations += leftover_donations_min
        except NameError:
            pass
        try:
            new_donations += leftover_donations_max
        except NameError:
            pass
        new_donors.add_donor(donor.name, new_donations)

    return new_donors



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
    '4': match_donations,
    '5': project_donations,
    '6': quit
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
                4: Match Donations
                5: Project Donations
                6: Quit\n
                ''')
            actions.get(action)()
        except ExitScript:
            break
        except TypeError:
            if action not in actions:
                continue
