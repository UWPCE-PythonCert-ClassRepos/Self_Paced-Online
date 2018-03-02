#!/usr/bin/env python3

import sys


donors = {
        'Jessie': [100, 300, 500],
        'James': [343, 22.11],
        'Ford': [3000, 400]}


def main_menu():
    choice = input(
        'Pick one:\n1) Send a thank you\n2) Create a Report\n\
3) Send letters to everyone\n4) Quit\n')
    return choice


def send_thankyou():
    donor_name = input(
        'Enter the donor\'s name: (type list if you want to get a list of\
 donors)\n')
    if donor_name == 'list':
        for z in donors.keys():
            print(z)
        send_thankyou()
    elif donor_name not in donors.keys():
        donors[donor_name] = []
    donation_amount = input(
        'Please enter a donation amount: ')
    donors[donor_name].append(float(donation_amount))
    print('Thank you {} for yout generous donation of {}'.format(
        donor_name, donation_amount))


def create_report():
    print('{:20} | {:15} | {:10} | {:15}'.format(
        'Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-'*70)
    for donor, amounts in donors.items():
        print('{:20} | {:15} | {:10} | {:15}'.format(
            donor, sum(amounts),
            len(amounts),
            sum(amounts) / len(amounts)))


def save_report():
    for donor, amounts in donors.items():
        with open(donor+'.txt', 'w') as donorfh:
            donorfh.write(
                'Thank you {} for yout generous donation of {}\n'.format(
                    donor, sum(amounts)))


def quittt():
    sys.exit()


def main():
    while True:
        users_choice = main_menu()
        selection = {
            '1': send_thankyou,
            '2': create_report,
            '3': save_report,
            '4': quittt
        }
        try:
            selection.get(users_choice)()
        except KeyError:
            print('Choose 1 to 4')
            main_menu()


if __name__ == '__main__':
    main()
