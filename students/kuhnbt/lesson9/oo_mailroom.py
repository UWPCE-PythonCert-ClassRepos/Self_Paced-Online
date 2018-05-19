#!/usr/bin/env python3
import os
import datetime
import sys


class UserInteraction:

    def __init__(self, donor_collection):
        self.donor_collection = donor_collection

    def start_program(self):
        selection_dict = {'1': self.send_thank_you, '2': self.create_report,
                          '3': self.send_to_everyone, '4': self.quit_program}
        while True:
            selection = input('''Please enter a selection (1-4):
                               1. Send a thank you
                               2. Create a report
                               3. Send letters to everyone
                               4. Quit
                               ''')
            try:
                selection_dict[selection]()
            except ValueError:
                print('Selection not found. Please enter a number 1-4')

    def send_thank_you(self):
        """Send a thank you note to person designated by user; add person to
        donor_info if they aren't already there"""
        while True:
            name = input('Please enter full name:\n')
            if name == 'list':
                print('This is the list of donor names:\n')
                for donor in self.donor_collection.donors:
                    print(donor.name)
            else:
                while True:
                    try:
                        donation = float(input('Please enter donation'
                                               ' amount:\n'))
                        break
                    except ValueError:
                        print('Please enter a number')
                for donor in self.donor_collection.donors:
                    if name == donor.name:
                        current_donor = donor
                        break
                else:
                    current_donor = Donor(name)
                    self.donor_collection.add_donor(current_donor)

                current_donor.add_donation(donation)

                print(current_donor.get_thank_you())
                break
        return

    def create_report(self):
        """Print summary report of donor info"""
        max_donor_width = max([len(donor.name) for donor in
                               self.donor_collection.donors])
        print(self.get_report_header(max_donor_width))
        self.donor_collection.sort_donors()
        for donor in self.donor_collection.donors:
            print(donor.get_report_row(max_donor_width))

    def get_report_header(self, max_donor_width):
        """Return string representing the header of the report"""
        return '{:{}}|{:12}|{:10}|{:8}'.format('Donor Name',
                                               max_donor_width, 'Total Given',
                                               'Num Gifts', 'Average Gift')

    def send_to_everyone(self, directory=os.getcwd()):
        """Write thank you notes to specified directory for each donor in
           donor_info"""
        user_dir = input('Change output directory (y/n)?')
        if user_dir.lower() == 'y':
            while True:
                directory = input('Please enter desired directory:')
                try:
                    os.chdir(directory)
                    break
                except FileNotFoundError:
                    print('Please enter a valid directory')
                except TypeError:
                    print('Please enter a valid directory')

        today = datetime.datetime.today().strftime('%Y-%m-%d')
        for donor in self.donor_collection.donors:
            filename = donor.name + '_' + today + '.txt'
            with open(filename, 'w') as f:
                print('Writing to ' + filename + '...')
                f.write(donor.get_thank_you())
            print('Finished!')

    def quit_program(self):
        """Exit program"""
        sys.exit()


class DonorCollection:
    def __init__(self, donors=[]):
        self.donors = []
        for donor in donors:
            self.add_donor(donor)

    def add_donor(self, donor):
        if not isinstance(donor, Donor):
            raise TypeError('Items in DonorCollection must be of type '
                            'Donor')
        self.donors.append(donor)

    def sort_donors(self):
        self.donors.sort()


class Donor:

    def __init__(self, name, donations=[]):
        self.name = name
        self.donations = []
        self.average_donation = 0
        self.get_average_donation()

    def add_donation(self, donation):
        if type(donation) == list:
            for l in donation:
                self.donations.append(float(l))
        else:
            self.donations.append(float(donation))
        self.get_average_donation()

    def get_average_donation(self):
        if self.donations:
            self.average_donation = sum(self.donations) / len(self.donations)

    def get_thank_you(self):
        """Return thankyou note for donor"""
        donor_dict = {'name': self.name, 'donation': self.donations[-1],
                      'num_donations': len(self.donations)}
        donor_dict['multiple'] = 's' if len(self.donations) > 1 else ''

        thankyou = ('Dear {name}:\n'
                    'Thank you for your generous donation of '
                    '${donation:.2f}.\nI really appreciate your '
                    '{num_donations}\ndonation{multiple} to our '
                    'organization.\nI assure you that your contributions '
                    'will be put to\ngood use!\n\n'
                    'Regards,\nBen').format(**donor_dict)

        return thankyou

    def get_report_row(self, max_donor_width):
        """Return string representing one row in report"""
        return '{:{}}|${:^11.2f}|{:^10}|${:^8.2f}'\
               .format(self.name, max_donor_width, sum(self.donations),
                       len(self.donations), self.average_donation)

    def __lt__(self, other):
        return sum(self.donations) > sum(other.donations)


def main():
    dc = DonorCollection()
    ui = UserInteraction(dc)
    ui.start_program()


if __name__ == '__main__':
    main()
