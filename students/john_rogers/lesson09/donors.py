"""
Donor classes for mailroom_L9.py
Author: JohnR
Version: .1 (Lesson 09)
Last updated: 2/16/2019
Notes: Guidelines:
        Works with one donor --> Donor class
        Works with multiple donors --> DonorDB
        User input --> Main script
        Complete separation of input and data handling
"""

import datetime as dt


class Donor(object):
    def __init__(self, first, last, donations=None):
        self.first = first
        self.last = last
        self.donations = donations

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    def new_donation(self, amount):
        return self.donations.append(amount)

    def total_donations(self):
        return sum(self.donations)


class DonorDB(object):
    def __init__(self, donors=None):
        if donors is None:
            self.donors = []
        else:
            self.donors = donors

    def new_donor(self, donor):
        self.donors.append(donor)

    def sorted_list(self):
        """
        Sort a give list of donors by total amount given, large to small
        :param data: dictionary of donor data
        :return: sorted list of donors
        """
        sorted_donors = []
        for name, donations in self.donors.items():

            try:
                total = round(sum(donations), 2)
                number = round(len(donations), 2)
                avg = total / len(donations)
                avg = round(avg, 2)
                sorted_donors.append([[name], [total], [number], [avg]])
            except TypeError as e:
                print('hit an error in sorted list: ', e)
                return None

        sorted_donors.sort(key=lambda x: x[1])
        sorted_donors.reverse()
        return sorted_donors

    def print_summary(self):
        """
        Print a list of donors sorted by historical donation amount.
        List donor name, number of donations and average donation amount.
        :return: none
        """
        donors = DonorDB.sorted_list(self.donors)
        print()
        print('Donor Name       | Total Given | Num Gifts | Avg Gift Amount')
        print('-' * 60)

        for d in donors:
            try:
                print(f'{d[0][0]:<17} ${d[1][0]:^15} {d[2][0]:^13}'
                      f'${d[3][0]:^8}')
            except Exception as e:
                print(e)

    def thank_all(self):
        """
        Print a form letter for each donor in the database
        :param db: current donor db
        :return: None
        """
        donors = DonorDB.sorted_list(self.donors)
        for d in donors:
            letter = DonorDB.form_letter(d[0][0], d[1][0])
            print(letter)

    @staticmethod
    def form_letter(name, donation):
        """
        create a form letter
        :param name: donor name
        :param donation: amount of donation as a float
        :return: form letter filled in with donor and amount
        """
        today = dt.today()
        letter = (
            f'Hey {name.capitalize()}, thanks for your donations! '
            f'As of today, {today}, you have donated a total of '
            f'${donation}.'
        )

        return letter

    def save_report(self):
        """
        Generate a thank you letter for each donor and write to individual
        files on disk.
        :param db: donor database
        :return: None
        """
        today = dt.today()
        donors = DonorDB.sorted_list(self.donors)
        print('Saving a copy to local disk....')
        for d in donors:
            letter = DonorDB.form_letter(d[0][0], d[1][0])
            user_file = "{}.{}.txt".format(d[0][0], today)

            with open(user_file, 'w') as outfile:
                outfile.write(letter)
                print(user_file, ' has been saved to disk.')

    def exit_menu(self):
        """
        write to file and exit the program
        :return: SystemExit
        """
        DonorDB.save_report(self.donors)
        print('Exiting program, thank you for your time today!')
        raise SystemExit

