#!/usr/bin/env python
from operator import itemgetter
from functools import reduce


class Donor():
    letter = ('FROM: Your friendly local charity mailroom.\n'
              'TO: {title_name}\n'
              'RE: Your recent donation\n\n'
              '\nThank you so much for your recent donation of'
              ' ${last_don:,.2f}. This will go a long way towards helping'
              ' to save the pythons. Your generosity is most appreciated!'
              '\n\nBest Regards,\nSave The Pythons\n'
              )

    def __init__(self, first_name, last_name, donation):
        if isinstance(donation, (list, tuple)):
            self.donations = list(donation)
        else:
            self.donations = [donation]
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = ' '.join((first_name.lower(), last_name.lower()))
        self.title_name = ' '.join((first_name.title(), last_name.title()))
        self.last_don = self.donations[-1]

    def add_donation(self, donation):
        self.donations.append(donation)
        self.last_don = donation

    def tot_donations(self):
        return sum(self.donations)

    def num_donations(self):
        return len(self.donations)

    def avg_donation(self):
        return self.tot_donations() / self.num_donations()

    def letter_to_screen(self, letter=letter):
        print('\n\n' + letter.format(**vars(self)))

    def letter_to_file(self, write_dir='.', file_name=None, letter=letter):
        if not file_name:
            file_name = (self.last_name + '_' + self.first_name + '.txt')
        with open('/'.join([write_dir, file_name]), 'w') as f:
            print('Writing Letter: {}'.format(file_name))
            f.write(letter.format(**vars(self)))

    def __str__(self):
        return ('{}, {}'.format(self.last_name.title(),
                                self.first_name.title()))

    def __repr__(self):
        return ('Donor({}, {}, {})'.format(self.first_name, self.last_name,
                                           self.donations))


class Donors_List():
    def __init__(self, *args):
        self.donors = {}
        for arg in args:
            try:
                self.donors[arg.full_name] = arg
            except AttributeError:
                print('Only Donor objects may be input')

    def new_donation(self, first_name, last_name, donation):
        full_name = ' '.join((first_name.lower(), last_name.lower()))
        if full_name in self.donors:
            self.donors[full_name].add_donation(donation)
        else:
            self.donors[full_name] = Donor(first_name, last_name, donation)
        self.donors[full_name].letter_to_screen()

    def gen_donor_report(self):
        donors_summary = [[str(donor), donor.tot_donations(),
                           donor.num_donations(), donor.avg_donation()] for
                          donor in sorted(self.donors.values(),
                          key=Donor.tot_donations, reverse=True)]
        return donors_summary

    def print_report(self):
        header = ' | '.join(('     Donor Name    ', 'Total Given', 'Num Gifts',
                             'Average Gift'))
        print('\n\n' + header)
        print('-' * len(header))
        for row in self.gen_donor_report():
            print(('{:20s}  $ {:>10.2f}   {:>9d}  $ {:>10.2f}').format(*row))

    def list_donors(self):
        print('\n\nCurrent Donors:\n')
        for donor in self.donors.values():
            print(donor)

    def all_letters_to_file(self, write_dir=None):
        write_dir = '.' if not write_dir else write_dir
        for donor in self.donors.values():
            donor.letter_to_file(write_dir)
            
    def challenge(self, factor):
        new_donor_list = self
        for donor in new_donor_list.donors.values():
            donor.donations = list(map(lambda don: don * factor, 
                                       donor.donations))
        return new_donor_list


def send_thank_you():
    """Print a thank you email"""
    donate_prompt = ('\n\nSend a Thank You Letter:\n\n'
                     'Please select an option from the list:\n'
                     '1 - Send a Thank You for New Donation\n'
                     '2 - List Current Donors\n'
                     '3 - Exit to Main Menu\n'
                     '>> '
                     )
    donate_menu = {'1': new_donation,
                   '2': cur_donors.list_donors,
                   '3': quit_menu
                   }
    show_menu(donate_prompt, donate_menu)


def send_all_letters():
    while True:
        try:
            write_dir = input('\nWhich directory should the letters be '
                              'written in? (leave blank for current dir): ')
            cur_donors.all_letters_to_file(write_dir)
            break
        except FileNotFoundError:
            print('Error: Directory not found. Please try again.')
    print('\nAll letters complete.\n')


def new_donation():
    """Add a new donation to donor and print thank you email to screen"""
    print('\nNew Donation:')
    last_name = input("  Please enter donor's last name: ")
    first_name = input("  Please enter donor's first name: ")
    while True:
        try:
            donation = float(input('  Enter the donation amount: '))
            break
        except ValueError:
            print('Error: Enter a numeric value for the dollar amount.\n')
    cur_donors.new_donation(first_name, last_name, donation)
    return False


def quit_menu():
    """Quit current menu"""
    return False


def show_menu(prompt, disp_dict):
    """Generate menu with dispatch dictionary"""
    while True:
        sel = input(prompt)
        try:
            if disp_dict[sel]() is False:
                return
        except KeyError:
            print('Error: Please enter an integer from the menu only.')


if __name__ == '__main__':
    cur_donors = Donors_List(Donor('Jeff', 'Bezos', [3456.89, 130]),
                             Donor('Bill', 'Gates', [789.25, 87562.22,
                                                     125000]),
                             Donor('Jimmy', 'Buffett', 85000),
                             Donor('Abe', 'Lincoln', [5, 2, 1]),
                             Donor('Yankee', 'Doodle', [67])
                             )

    main_prompt = ('\n\nMain Menu:\n\n'
                   'Please select an option from the list:\n'
                   '1 - Send a Thank You\n'
                   '2 - Create a Report\n'
                   '3 - Send Thank You Letters to All\n'
                   '4 - Quit Menu\n'
                   '>> '
                   )
    main_menu = {'1': send_thank_you,
                 '2': cur_donors.print_report,
                 '3': send_all_letters,
                 '4': quit_menu
                 }
    show_menu(main_prompt, main_menu)
