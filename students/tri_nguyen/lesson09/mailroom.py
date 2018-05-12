# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  30-Apr-2018
# ------------------------------------------- #

import time
from operator import itemgetter

local_time = time.localtime()


class Donor:

    donor_dict = {
    'William Gates, III': {'total': 653784.49, 'num_gifts': 2, 'avg': 326892.24},
    'Mark Zuckerberg': {'total': 16396.10, 'num_gifts': 3, 'avg': 5465.37},
    'Jeff Bezos': {'total': 877.33, 'num_gifts': 1, 'avg': 877.33},
    'Paul Allen': {'total': 708.42, 'num_gifts': 3, 'avg': 236.14},
    'Tri Nguyen': {'total': 100.00, 'num_gifts': 1, 'avg': 100.00}}

    def __init__(self, full_name, donation_amount):
        self.full_name = full_name.title()
        if isinstance(donation_amount, str) and donation_amount.isdecimal():
            self.donation_amount = float(donation_amount)
        else:
            raise ValueError('value entered is not a number.')
        if Donor.donor_dict.get(self.full_name):
            Donor.donor_dict[self.full_name]['total'] += self.donation_amount
            Donor.donor_dict[self.full_name]['num_gifts'] += 1
            Donor.donor_dict[self.full_name]['avg'] = Donor.donor_dict[self.full_name]['total'] / Donor.donor_dict[self.full_name]['num_gifts']
        else:
            Donor.donor_dict[self.full_name] = dict(total=self.donation_amount, num_gifts=1, avg=self.donation_amount)

    def __str__(self):
        return '{0}: {1.full_name}'.format(self.__class__.__name__, self)

    def get_name(self):
        return '{0.full_name}'.format(self)

    def get_donation_amount(self):
        return '{0.full_name} donated ${0.donation_amount:,.2f}'.format(self)

    def send_thanks(self):
        thank_you_message = '''
            Dear {0.full_name},

            Thank you for giving us ${0.donation_amount:,.2f}. Your money will be put to good use.
            Please come back and donate more.

            Best Regards,

            John Doe
        '''.format(self)

        return thank_you_message


class DonorHandle:

    def display_donor_list(self):
        donor_name = enumerate([donor for donor in Donor.donor_dict])
        for idx, name in donor_name:
            print(idx + 1, '-', name)

    def generate_report(self):
        header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
        formatted_header = '{0:<26}|{1:^13}|{2:^11}|{3:^14}'.format(*header)
        border = '{}'.format('-' * len(formatted_header))
        value_template = '{0:<26} ${1:12.2f} {2:11} ${3:13.2f}'

        donor_list = [(name, Donor.donor_dict[name]['total'], Donor.donor_dict[name]['num_gifts'], Donor.donor_dict[name]['avg'])
        for name in Donor.donor_dict]
        donor_list.sort(key=itemgetter(1), reverse=True)

        print('Report of donors:\n')
        print(formatted_header)
        print(border)

        for item in donor_list:
            print(value_template.format(item[0], item[1], item[2], item[3]))
        print()

    @staticmethod
    def format_filename(name):
        if isinstance(name, (int, float)):
            raise TypeError('name must be a string.')
        if ',' in name:
            name = name.replace(',', '').replace(' ', '_') + '.txt'
            return name
        else:
            name = name.replace(' ', '_') + '.txt'
            return name

    def send_all_letters(self):
        email_temp = ['Thank you for your kind donation of',
        'It will be put to very good use.',
        'Sincerely',
        '-The Team']

        for name in Donor.donor_dict:
            with open(DonorHandle.format_filename(name), 'w') as f:
                f.write('Dear {},\n\n'.format(name))
                f.write('\t{0} ${1:,.2f}\n\n'.format(email_temp[0], Donor.donor_dict[name]['total']))
                f.write('\t{}\n\n'.format(email_temp[1]))
                f.write('\t\t{}.\n'.format(email_temp[2]))
                f.write('\t\t    {}\n'.format(email_temp[3]))
                f.write('\t\t    {0}/{1}/{2}'.format(local_time.tm_mon, local_time.tm_mday, local_time.tm_year))

        print('ALL LETTERS HAVE BEEN SENT!!!\n')

    def find_donor(self, full_name):
        full_name = full_name.title()
        if full_name.title() in Donor.donor_dict:
            return '\n{}\nTotal donation amount: ${:,.2f}\nDonated: {} times\nAverage: ${:,.2f}'.format(full_name, Donor.donor_dict[full_name]['total'],
                Donor.donor_dict[full_name]['num_gifts'], Donor.donor_dict[full_name]['avg'])
        else:
            return 'Donor not found.'


def display_menu():
    ''' display a menu of 3 actions '''

    menu = ''' Select one of the actions below:

    1. Send a Thank You
    2. Create a Report
    3. Send letters to everyone
    4. Quit

    '''
    return menu


def send_thank_you():

    donor_handle = DonorHandle()

    while True:
        full_name = input('Enter a Full Name (or type "list" to get the list of donors): ').title()
        if full_name.lower() == 'list':
            donor_handle.display_donor_list()
            continue

        donation_amount = input('Enter donation amount: ')
        donor_instance = Donor(full_name, donation_amount)

        choice = input('\nDo you want to quit and send email?(y/n) ')
        if choice == 'y':
            print('\n', donor_instance.send_thanks(), '\n')
            break
        else:
            continue


def default():
    print('BAD CHOICE\n')


def main():

    donor_handle = DonorHandle()

    while True:
        print(display_menu())

        action = input('Enter the corresponding number for action [1 to 4]: ')
        print()
        if action == '4':
            break

        options = {
            '1': send_thank_you,
            '2': donor_handle.generate_report,
            '3': donor_handle.send_all_letters}
        options.get(action, default)()


if __name__ == '__main__':
    main()
