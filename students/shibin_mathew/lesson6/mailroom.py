#!/usr/bin/env python3
import sys
from collections import defaultdict


def print_donor_names(donors2):
    list_test = []
    for names in donors2:
        print(names)
        list_test.append(names)  # Debug - for unit testing
    return list_test


def send_thank_you(donors2):
    #  Function to Send a Thank You Email
    program_quit = False
    while not program_quit:
        name = input("Please input your full name\n")
        if name == "list":
            print("list of names")
            print_donor_names(donors2)
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
                continue
    return None

def create_report(donors2):
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


def send_letters(donors2):
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


def switch_menu(option):
    dict_switch = {'1': send_thank_you, '2': create_report, '3': send_letters, '4': quit_menu}
    return dict_switch[option]


def quit_menu():
    print("Thank you for using the application!")
    sys.exit()


def question_module():
    #  Function that acts as the main gate into the app
    program_quit = False
    while not program_quit:
        user_response = input("Please choose an action:\n\n"
                              "1. Send a Thank You\n"
                              "2. Create a Report\n"
                              "3. Send letters to everyone\n"
                              "4: Quit\n")
        try:
            if user_response == '4':
                switch_menu(user_response)()
            else:
                switch_menu(user_response)(donors2)
        except KeyError:
            print("Please pick between 1,2,3 or 4")


if __name__ == "__main__":
    list_ = [('Shibin', 25.25), ('Shibin', 456.25), ('Kimberly', 125.50), ('Kimberly', 5.55), ('Jordy', 55),
             ('Jordy', 25), ('Andreck', 35)]
    donors2 = defaultdict(list)
    for name, amount in list_:
        donors2[name].append(amount)
    question_module()
