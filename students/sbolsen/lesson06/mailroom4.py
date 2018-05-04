#!/usr/bin/env python3

import time
from operator import itemgetter


donors = {
        'Jesse Johnson': [150, 345],
        'Mary May': [1000, 750],
        'Spencer Samuels': [50, 200, 1100],
        'Zach Zillow': [85],
        'Tina Thompson': [76, 250, 300]
        }


def prompt_user():
    choice = input('Please select from the following: \n1) Send a Thank You \n2) Create a Report \n3) Send letters to '
            'everyone \n4) Quit\n')
    return choice


def thank_you():
    select_user = input('Enter a full name: ')
    if select_user == 'list':
        print(list(donors))
        select_user = input('Enter a full name: ')
    update_donation = int(input('Enter a donation amount: '))
    try:
        if select_user in donors:
            donors[select_user].append(update_donation)
        elif select_user not in donors:
            add_user(select_user, update_donation)
    except ValueError:
        print('Input error: please enter numbers only. Try again.\n')


def add_user(select_user, update_donation):
    donors[select_user] = [(update_donation)]


def create_report():
    title = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    print('{:20} | {:>17} | {:>17} | {:>17}'.format(*title))
    print('{:-<80}'.format(''))
    sorted_report = []
    for key, value in donors.items():
        a = sum(value)
        b = len(value)
        total = a // b
        sorted_report.append([key, a, b, total])
    for i in sorted(sorted_report, key=itemgetter(1), reverse=True):
        print('{:20} $ {:>17} $ {:>17} $ {:>17}'.format(i[0], i[1], i[2], i[3]))


def send_letters():
    for key, value in donors.items():
        timestr = time.strftime("%Y%m%d")
        filename = "{}_{}.txt".format(key.replace(" ","_"), timestr)
        with open(filename, 'w') as fp:
            fp.write('Dear {},\nThank you for your kind donation of {}. It will be put to good '
                    'use.\nSincerely,\n-The Team'.format(key, sum(value)))


def main():
    while True:
        try:
            a = int(prompt_user())
            decision = {
                    1: thank_you,
                    2: create_report,
                    3: send_letters,
                    4: quit,
                    }
            decision[a]()
        except KeyError:
            print('Please select a number 1 - 4')
        except ValueError:
            print('Please use an integer 1 - 4')


if __name__ == "__main__":
    main()
