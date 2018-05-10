'''
file: functions_mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: functions for OOP mailroom program 
'''

from classes_mailroom import Mailroom
from collections import defaultdict

def efunc():
    return 'exiting'


def fakefunc():
    pass

def thankyou():
    db = Mailroom()
    db.thankyou()


def report():
    db = Mailroom()
    db.report()
    

def enter_donor():
    while True: 
        donor = input('Please enter donor name: ')
        if not donor.isalpha():
            print('Only alphabetical characters in donor name allowed, please try again')
            continue
        else:
            break
    return donor


def list_donors():
    db = Mailroom()
    print('\n\tAll donors:\n')
    for i in db.get_all_donors():
        person = i[0]
        # print('\t{} {}'.format('Nice person:', person)) 
        print('\t{}'.format(person)) 


def list_donations():
    donor = enter_donor()
    db = Mailroom()
    print('\n\tDonations of {}:\n'.format(donor))
    for i in db.get_donations(donor):
        date = i[0]
        donation = i[1]
        print('\tDate: {}\tDonation: {}'.format(date, donation)) 
        

def add():
    donor = enter_donor()
    amount = input('Please enter donation amount: ')
    db = Mailroom()
    db.add_donation(donor, amount)


def get_average_donation():
    donor = enter_donor()
    db = Mailroom()
    num = db._get_average_donation(donor)
    # print('\n\t{} has given an average donation of {}. \n'.format(donor, num))
    print('\n\t', num, ' \n')
    

def menu(prompt, dispatcher):
    try:
        while True:
            response = input(prompt)
            if dispatcher[response]() == 'exiting':
                break
    except KeyError:
        print('\n\tSorry, unknown option:', response, '\n')
        menu(prompt, dispatcher)

