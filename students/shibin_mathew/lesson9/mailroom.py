#!/usr/bin/env python3
import sys
from collections import defaultdict


class Donor:
    def __init__(self, names, amount):
        self.names = names
        self.amount = amount

    @property
    def names(self):
        return "{}".format(self._names)

    @names.setter
    def names(self, names):
        self._names = names

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount


class Collection:
    def __init__(self, donors2=None):
        self.donors2 = donors2

    @property
    def donors2(self):
        return self._donors2

    @donors2.setter
    def donors2(self, donors2):
        self._donors2 = donors2

    def print_donor_names(self, donors2):
        list_test = []
        for names in donors2:
            list_test.append(names)
        return list_test

    def send_thank_you(self, donors2):
        #  Function to Send a Thank You Email
        c1 = Collection()
        program_quit = False
        while not program_quit:
            name = input("Please input your full name\n")
            if name == "list":
                print("list of names")
                print(c1.print_donor_names(donors2))
            elif name == 'quit' or name == 'Quit':
                break
            else:
                break
        while True:
            donation = input("Please enter a donation amount\n")
            if donation == 'quit' or donation == 'Quit':
                return
            else:
                try:
                    donation = float(donation)
                    donors2[name].append(donation)
                    break  # break out of the while loop
                except ValueError:
                    print("please input a valid amount")

    def create_report(self, donors2):
        #  Function to create a report
        list_test = []
        print("hello")
        print("{: <20s}{: ^4s}{: <10s}{: ^4s}{: <10s}{: ^4s}{: <10s}"
              .format('Donor Name', '|', 'Total Given', '|',
                      'Num Gifts', '|', 'Average Gift'))
        print('-' * 70)
        print(' ')
        for names in donors2:
            print("{: <24s}{: <2s}{: >10}{: >13}{: >6s}{: >11}"
                  .format(names, '$', round(sum(donors2[names]), 2),
                          len(donors2[names]), '$',
                          round(sum(donors2[names])/len(donors2[names]), 2)))
            list_test.append([names, round(sum(donors2[names]), 2), len(donors2[names]),
                             round(sum(donors2[names])/len(donors2[names]), 2)])  # Debug - for unit testing
        return list_test


    def send_letters(self, donors2):
        #  send letters to everyone
        list_name = []
        for names in donors2:
            try:
                with open(names+'.txt', 'w') as text_file:
                    text_file.write('Dear {},\n\n'
                                    'Thank you for your kind donation of ${}.\n'
                                    'It will be put to very good use\n\n'
                                    '\t\t\tSincerely,\n'
                                    '\t\t\t\t-The Team'.format(names, round(sum(donors2[names]), 2)))
                list_name.append(names+'.txt')  # Debug - for unit testing
            except IOError:
                print("Could not open file: "+names+'.txt')
        print("Letters have been sent to everyone!")
        return list_name


    def switch_menu(self, option):
        c = Collection()
        dict_switch = {'1': c.send_thank_you, '2': c.create_report, '3': c.send_letters, '4': c.quit_menu}
        return dict_switch[option]

    def quit_menu(self):
        print("Thank you for using the application!")
        sys.exit()

    def question_module(self, donors2):
        #  Function that acts as the main gate into the app
        c1 = Collection()
        program_quit = False
        while not program_quit:
            user_response = input("Please choose an action:\n\n"
                                  "1. Send a Thank You\n"
                                  "2. Create a Report\n"
                                  "3. Send letters to everyone\n"
                                  "4: Quit\n")
            try:
                if user_response == '4':
                    c1.switch_menu(user_response)()
                else:
                    c1.switch_menu(user_response)(donors2)
            except KeyError:
                print("Please pick between 1,2,3 or 4")


def main():
    d1 = Donor("Shibin", 25.25)
    d2 = Donor("Kimberly", 125.50)
    d3 = Donor("Jordy", 12)
    d4 = Donor("Andreck", 14)
    list_ = [(d1.names, d1.amount), (d2.names, d2.amount), (d3.names, d3.amount), (d4.names, d4.amount)]
    donors2 = defaultdict(list)
    for name, amount in list_:
        donors2[name].append(amount)

    q = Collection()
    q.donors2 = donors2
    q.question_module(q.donors2)


if __name__ == "__main__":
    main()
