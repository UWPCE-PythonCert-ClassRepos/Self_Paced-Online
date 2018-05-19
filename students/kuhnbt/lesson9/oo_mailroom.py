import os
import datetime
import sys


class Donor:
    """Class representing an individual donor

    Attributes:
        name (str):Donor's name
        donations (list): Donor's previous donations
        avg_donation (float): Average donation amount
    """
    def __init__(self, name, donations=[]):
        self.name = name
        self.donations = donations
        self.avg_donation = None
        self.get_avg_donation()

    def add_donation(self, donation):
        if type(donation) == list:
            for l in donation:
                self.donations.append(float(l))
        else:
            self.donations.append(float(donation))
        self.get_avg_donation()

    def get_avg_donation(self):
        if self.donations:
            self.avg_donation = sum(self.donations) / len(self.donations)


class DonorCollection:
    """Class representing a collection of donors"""
    def __init__(self, donors=[]):
        self.donors = []
        for donor in donors:
            self.add_donor(donor)

    def add_donor(self, donor):
        if not isinstance(donor, Donor):
            raise TypeError('Items in DonorCollection must be of type '
                            'Donor')
        self.donors.append(donor)

    def send_thank_you(self):
        while True:
            name = input('Please enter full name:\n')
            if name == 'list':
                print('This is the list of donor names:\n')
                for item in self.donors:
                    print(item.name)
            else:
                while True:
                    try:
                        donation = float(input('Please enter donation'
                                               ' amount:\n'))
                        break
                    except ValueError:
                        print('Please enter a number')
                for donor in self.donors:
                    if donor.name == name:
                        current_donor = donor
                        current_donor.add_donation(donation)
                        break
                else:
                    current_donor = Donor(name, donations=[donation])
                    self.add_donor(current_donor)

                print(self.get_thank_you(current_donor))
                break
        return

    def send_to_everyone(self):
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
        for donor in self.donors:
            filename = donor.name + '_' + today + '.txt'
            with open(filename, 'w') as f:
                print('Writing to ' + filename + '...')
                f.write(self.get_thank_you(donor))
        print('Finished!')

    def get_thank_you(self, donor):
        """Return text of thank you letter for given donor"""
        donor_dict = {'name': donor.name, 'donation': donor.donations[-1],
                      'num_donations': len(donor.donations)}
        donor_dict['multiple'] = 's' if len(donor.donations) > 1 else ''

        thankyou = ('Dear {name}:\n'
                    'Thank you for your generous donation of '
                    '${donation:.2f}.\nI really appreciate your '
                    '{num_donations}\ndonation{multiple} to our '
                    'organization.\nI assure you that your contributions '
                    'will be put to\ngood use!\n\n'
                    'Regards,\nBen').format(**donor_dict)
        return thankyou

    def get_report_header(self, max_donor_width):
        return '{:{}}|{:12}|{:10}|{:8}'.format('Donor Name',
                                               max_donor_width, 'Total'
                                               ' Given', 'Num Gifts',
                                               'Average Gift')

    def get_report_row(self, donor, max_donor_width):
        return '{:{}}|${:^11.2f}|{:^10}|${:^8.2f}'.format(donor[0],
                                                          max_donor_width,
                                                          sum(donor[1]),
                                                          len(donor[1]),
                                                          sum(donor[1]) /
                                                          len(donor[1]))

    def create_report(self):
        max_donor_width = max([len(donor.name) for donor in self.donors])
        max_donor_width = 10 if max_donor_width < 10 else max_donor_width
        print(self.get_report_header(max_donor_width))
        donor_list = [(donor.name, donor.donations) for donor in self.donors]
        for donor in sorted(donor_list, key=lambda x: sum(x[1])):
            print(self.get_report_row(donor, max_donor_width))

    def quit_program(self):
        sys.exit()


def start_program(dc):
    """Prompt user for desired donor action and fulfill the request"""
    selection_dict = {'1': dc.send_thank_you, '2': dc.create_report,
                      '3': dc.send_to_everyone, '4': dc.quit_program}
    while True:
        selection = input('''Please enter a selection (1-4):
                           1. Send a thank you
                           2. Create a report
                           3. Send letters to everyone
                           4. Quit
                           ''')
        try:
            selection_dict[selection]()
        except KeyError:
            print('Selection not found. Please enter a number 1-4')


if __name__ == '__main__':
    donors = DonorCollection()
    start_program(donors)
