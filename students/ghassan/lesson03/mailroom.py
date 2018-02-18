#!/usr/bin/env python3

import sys

donors = [
    ('Jessie', (100, 300, 500)),
    ('James', (343, 22.11)),
    ('Ford', (3000, 400))]


def prompt():
    choice = input(
        'Pick one:\n1) Send a thank you\n2) Create a Report\n3) Quit\n')
    while choice not in ['1', '2', '3']:
        choice = input(
            'Pick one:\n1) Send a thank you\n2) Create a Report\n 3) Quit\n')
    return choice


def send_thankyou():
    donor_name = input('Enter the donor\'s name: ')
    if donor_name == 'list':
        for donor in donors:
            print(donor[0])
    elif donor_name not in donors:
        donors.append((donor_name, ))
    donation_amount = input(
        'Please enter a donation amount: ')
    print('Thank you {} for yout generous donation of {}'.format(
        donor_name, donation_amount))
    prompt()


def create_report():
    print('{:20} | {:15} | {:10} | {:15}'.format(
        'Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-'*70)
    for donor in donors:
        print('{:20} | {:15} | {:10} | {:15}'.format(
            donor[0], sum(int(x) for x in donor[1]),
            len(donor[1]),
            sum(int(x) for x in donor[1]) / len(donor[1])))


def quittt():
    sys.exit()


def main():
    users_choice = prompt()
    if users_choice == '1':
        send_thankyou()
    elif users_choice == '2':
        create_report()
    else:
        quittt


if __name__ == '__main__':
    main()