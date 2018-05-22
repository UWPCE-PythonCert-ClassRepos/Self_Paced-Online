#!/usr/bin/env python3

# chmod +x mailroom.py needs to be performed before executable

'''
    File Name: mailroom.py
    Author: Matt Hudgins
    Date created: 5/6/18
    Date last modified: 5/6/18
    Python Version 3.6.4
'''
import sys

donors = [
    ("Rick Grimes", (5.00, 10.00, 2.00)), 
    ("Shane Walsh", (4.00, 10.00, 9.00)), ("Carl Grimes", 
    (72.00, 10.00, 88.00)), ("Morgan Jones", (68.00, 10.00, 98.00))]


def prompt():
    """ This function defines the users options"""
    choice = input(
        'Pick one:\t1) Send a thank you\t2) Create a Report\t3) Quit\t:')
    while choice not in ['1', '2', '3']:
        choice = input(
            'Pick one:\t1) Send a thank you\t2) Create a Report\t 3) Quit\t:')
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
    print('Thank you {} for yout donation of {}'.format(donor_name, donation_amount))
    prompt()


def create_report():
    """ This function creates a report for the user"""
    print('{:20} | {:20} | {:20} | {:20}'.format(
        'Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-' * 70)
    for donor in donors:
        print('{:20} | {:<20} | {:<20} | {:<20}'.format(donor[0], sum(int(x) for x in donor[1]), len(donor[1]), sum(int(x) for x in donor[1]) / len(donor[1])))


def quit():
    """ This function exits the executable"""
    print("Thanks for your time!")
    sys.exit()


def main():
    """main block"""
    users_choice = prompt()
    if users_choice == '1':
        send_thankyou()
    elif users_choice == '2':
        create_report()
    elif users_choice == '3':
        quit()


if __name__ == '__main__':
    main()
