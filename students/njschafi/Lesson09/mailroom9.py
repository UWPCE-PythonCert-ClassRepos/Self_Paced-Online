#!/usr/bin/env python3
# NEIMA SCHAFI, LESSON 9 Assignment Mailroom
import sys


def menu(d, prompt):
    """Main menu function which user can select one of the options shown"""
    pick = {1: d.thank_you, 2: d.report, 3: d.send_all, 4: end}
    while True:
        selection = input(prompt)
        try:
            selection = int(selection)
        except ValueError:
            print('ERROR: Input a menu item number.')
            continue
        try:
            pick.get(selection)()
        except TypeError:
            print('ERROR: Number inputted is not a menu item.')
            continue


class Donor():

    def __init__(self, name):
        """Main Constuctor"""
        self.__name = name
        self.__total = 0
        self.__amount = 0
        self.__donationlist = []
        self.__donation = 0

    @property
    def name(self):
        """Returns name of donor"""
        return self.__name.title()

    @property
    def donationlist(self):
        """Returns historical list of given donations"""
        return self.__donationlist

    @property
    def total(self):
        """Returns number of donations"""
        return len(self.__donationlist)

    @property
    def amount(self):
        """Return total amount ($) of donations"""
        return round(sum(self.__donationlist), 2)

    @property
    def donation(self):
        """Return the current donation amount"""
        return self.__donation

    @property
    def average(self):
        """Return avg donation amount"""
        if self.total == 0:
            return 0
        else:
            return round((self.amount/self.total), 2)

    def add_donation(self, n):
        """Adds new donation to historical donations list for donor"""
        self.__donationlist.append(float(n))

    def initlist(self, d=[]):
        """Allows for a list of multiple donation amounts to be set
        as donors __donationlist"""
        self.__donationlist = d

    def email(self, current):
        """Writes thank you email to donor for given amount"""
        return ('\nDear {}, \n\tThank you for your generous ${:.2f} donation.'
                '\n\tYou are an amazing person. '
                'Good job!'.format(self.name, current))

    def write_email(self):
        """Writes email to thank donor for donation"""
        s = ('Dear {},\n\n\tThanks for the ${:.2f} in donations.\n\n\t'
                'We will use it to bring back the spin doctors.\n\n\n\t\t'
                'Thanks,\n\t\t\tPost Malone'
                .format(self.__name, self.amount))
        split = self.name.split(' ')
        if len(split) >= 3:  # 3 names ex: William Gates III
                with open('{}_{}_{}.txt'
                .format(split[0], split[1], split[2]), 'w') as f:
                    f.write(s)
        else:
                with open('{}_{}.txt'.format(split[0], split[1]), 'w') as f:
                    f.write(s)


class Donors():
    def __init__(self):
        """Main Constuctor"""
        self.donors = [Donor("Leon Dechino"), Donor("Michael Scarn"),
                        Donor("Lamar Dankers"), Donor("Horse Malone"),
                        Donor("Rupert Everton")]
        # Set Donation Amounts for Donors in Initial Donors List
        self.donors[0].initlist([200.43, 30.23, 1.50])
        self.donors[1].initlist([23.99])
        self.donors[2].initlist([400.00, 500.00, 600.00])
        self.donors[3].initlist([23.23, 100.45])
        self.donors[4].initlist([1.00, 2.00])
        self.donorslist = []

        for i in self.donors:
            self.donorslist.append(i.name)

    def list_names(self):
        """Lists names of Donors"""
        s = 'List of Donors\n' + '--------------\n'
        for i in self.donors:
            s += i.name + '\n'
        print(s)

    def add_donor(self, d):
        """Adds new donor to object Donors"""
        if isinstance(d, Donor):
            self.donors.append(d)
            self.donorslist.append(d.name)
        else:
            print('Not a donor object. Not added to donors list.')

    def send_all(self):
        for x in self.donors:
            x.write_email()
        print('Sent out emails to everyone!\n')

    def report(self):
        """Prints table of donors sorted from most donated to least"""
        print('{:25} | {:>15} | {:9} | {:>14}'.format('Donor Name',
                'Total Given', 'Num Gifts', 'Average Gift') + '\n' + '-'*73)
        d_total = {item.amount: item for item in self.donors}
        d_sort = sorted(d_total, reverse=True)
        for i in d_sort:
                print('{:25} | ${:>14.2f} | {:9} | ${:14.2f}'
                        .format(d_total[i].name, d_total[i].amount,
                        d_total[i].total, d_total[i].average))

    def thank_you(self):
        """Function which tests if name inputted is in a list or not, adds the
        name if not on the list then calls donation function"""
        name = input('Please enter a full name or enter "list" for'
                        ' list of names or enter "Menu" to return to'
                        ' main prompt: ')
        while name.isdigit() or name == "":
            name = input('\nNot a valid name. Please enter a full name or '
                            'enter "list" for list of names or enter '
                            '"Menu" to return to main prompt: ')
        if name.title() == "Menu":
            menu(self, prompt)
        elif name.lower() == "list":
            self.list_names()
        elif name.title() in self.donorslist:
            self.donation(name.title())
        else:
            self.add_donor(Donor(name.title()))
            self.donation(name.title())

    def donation(self, n):
        """
        Adds donation (if numeric) to selected donor and then calls
        email funtion to print out thank you note.
        """
        while True:
            current = input('Enter donation amount or enter "Menu" '
                            'to return to main prompt: ')
            if current.title() == "Menu":
                menu(self, prompt)
            try:
                for i in self.donors:
                    if n == i.name:
                        i.add_donation(float(current))
                        print(i.email(float(current)))
                        menu(self, prompt)
            except ValueError:
                print('Error: Enter a Numberic Value')


prompt = ('\nChoose an action (select number):\n 1 - Send a Thank You\n'
                ' 2 - Create a Report\n 3 - Send letters to everyone\n'
                ' 4 - Quit\n Your selection: ')


def end():
    sys.exit()


if __name__ == '__main__':
    d = Donors()
    menu(d, prompt)
