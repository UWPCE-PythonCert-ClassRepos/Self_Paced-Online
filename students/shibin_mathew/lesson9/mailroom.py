#!/usr/bin/env python3
import sys
from collections import defaultdict


class Donor:
    # Donor class - it can have other attributes about the donors (address, location, etc.)
    def __init__(self, names, amount):
        self.names = names
        self.amount = amount


class Collection:
    def __init__(self, donors=None):
        self.donors = donors

    def print_donor_names(self):
        list_test = []
        for names in self.donors:
            list_test.append(names)
        return list_test

    def send_thank_you(self):
        #  Function to Send a Thank You Email
        #c1 = Collection()
        program_quit = False
        while not program_quit:
            name = input("Please input your full name\n")
            if name == "list":
                print("list of names")
                print(self.print_donor_names())
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
                    self.donors[name].append(donation)
                    break  # break out of the while loop
                except ValueError:
                    print("please input a valid amount")

    def create_report(self):
        #  Function to create a report
        list_test = []
        print("hello")
        print("{: <20s}{: ^4s}{: <10s}{: ^4s}{: <10s}{: ^4s}{: <10s}"
              .format('Donor Name', '|', 'Total Given', '|',
                      'Num Gifts', '|', 'Average Gift'))
        print('-' * 70)
        print(' ')
        for names in self.donors:
            print("{: <24s}{: <2s}{: >10}{: >13}{: >6s}{: >11}"
                  .format(names, '$', round(sum(self.donors[names]), 2),
                          len(self.donors[names]), '$',
                          round(sum(self.donors[names])/len(self.donors[names]), 2)))
            list_test.append([names, round(sum(self.donors[names]), 2), len(self.donors[names]),
                             round(sum(self.donors[names])/len(self.donors[names]), 2)])
        return list_test

    def send_letters(self):
        #  send letters to everyone
        list_name = []
        for names in self.donors:
            try:
                with open(names+'.txt', 'w') as text_file:
                    text_file.write('Dear {},\n\n'
                                    'Thank you for your kind donation of ${}.\n'
                                    'It will be put to very good use\n\n'
                                    '\t\t\tSincerely,\n'
                                    '\t\t\t\t-The Team'.format(names, round(sum(self.donors[names]), 2)))
                list_name.append(names+'.txt')  # Debug - for unit testing
            except IOError:
                print("Could not open file: "+names+'.txt')
        print("Letters have been sent to everyone!")
        return list_name

    def quit_menu(self):
        print("Thank you for using the application!")
        sys.exit()

    def switch_menu(self, option):
        dict_switch = {'1': self.send_thank_you, '2': self.create_report, '3': self.send_letters, '4': self.quit_menu}
        return dict_switch[option]


class UserModule:
    # class to handle user inputs
    def __init__(self, donors):
        self.donors = donors

    def question_module(self):
        #  Function that acts as the main gate into the app
        c1 = Collection(self.donors)
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
                    c1.switch_menu(user_response)()
            except KeyError:
                print("Please pick between 1,2,3 or 4")


def main():
    d1 = Donor("Shibin", 25.25)  # Create a donor object to demonstrate the capability of the User Module
    list_ = [(d1.names, d1.amount)]
    donors = defaultdict(list)
    for name, amount in list_:
        donors[name].append(amount)
    c = UserModule(donors)  # Pass in a donor
    c.question_module()  # Call the question module


if __name__ == "__main__":
    main()
