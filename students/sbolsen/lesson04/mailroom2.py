#!/usr/bin/env python3

import time

donors = {
        'Jesse Johnson': [150, 345],
        'Mary May': [1000, 750],
        'Spencer Samuels': [50, 200, 1100],
        'Zach Zillow': [85],
        'Tina Thompson': [76, 250, 300]
        }


def donor_list():
    for donor in donors:
        print(donor)


def prompt_user():
    choice = input('Please select from the following: \n1) Send a Thank You \n2) Create a Report \n3) Send letters to everyone \n4) Quit\n')
    return choice


def thank_you():
    select_user = input('Enter a full name: ')
    if select_user == 'list':
        donor_list()
        select_user = input('Enter a full name: ')
    return select_user


def user():
    select_user = thank_you()
    update_donation = int(input('Enter a donation amount: '))
    try:
        if select_user in donors.keys():
            donors[select_user].append(update_donation)
        elif select_user not in donors:
            donors[select_user] = [update_donation]
        print(donors)
    except Exception as e:
        print('Exception [{}]'.format(e))


def create_report():
    title = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    print('{:20} | {:>17} | {:>17} | {:>17}'.format(*title))
    print('{:-<80}'.format(''))
    for key, value in donors.items():
        a = sum(value)
        b = len(value)
        total = a // b
        print('{:20} $ {:>17} $ {:>17} $ {:>17}'.format(key, a, b, total))

def send_letters():
    for key, value in donors.items():
        timestr = time.strftime("%Y%m%d")
        filename = "{}_{}.txt".format(key.replace(" ","_"), timestr)
        with open(filename, 'w') as fp:
            fp.write('Dear {},\nThank you for your kind donation of {}. It will be put to good use.\nSincerely,\n-The Team'.format(key, sum(value)))


def main():
    while True:
        a = int(prompt_user())
        decision = {
                1: user,
                2: create_report,
                3: send_letters,
                4: quit,
                }
        try:
            decision[a]()
        except Exception as e:
            print("Exception [{}]".format(e))

if __name__ == "__main__":
    main()
