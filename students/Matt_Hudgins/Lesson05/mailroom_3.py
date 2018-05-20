#!/usr/bin/env python3

# chmod +x mailroom.py needs to be performed before executable

'''
    File Name: mailroom_3.py
    Author: Matt Hudgins
    Date created: 5/20/18
    Date last modified: 5/20/18
    Python Version 3.6.4
'''
import sys

# This is the donor list
donors = {}
donors['Rick Grimes'] = [5.00, 10.00, 2.00]
donors['Shane Walsh'] = [4.00, 10.00, 9.00]
donors['Carl Grimes'] = [72.00, 10.00, 88.00]
donors['Morgan Jones'] = [68.00, 10.00, 98.00]


def donor_list():
    '''This function prints a list of all current donors'''
    for i in donors:
        print(i)
    return


def adding_a_donor(newname):
    '''This function adds a name to the donor list'''
    donors[newname] = []
    adding_a_donation(newname)
    return


def adding_a_donation(newname):
    '''This function adds a donation to the the list'''
    donation_amount = round(float(input(f'Enter a Donation amount for\n'
    '{newname}\n')), 2)
    if newname in donors.keys():
        donors[newname].append(donation_amount)
    elif newname not in donors:
        donors[newname] = [donation_amount]
    print(donors)
    return


def send_letter(newname, amount):
        letter = 'Dear {},\n Thank you for your donation of ${}'
        print(letter.format(newname, amount))
        print('\n')
        return


def create_report():
    '''This function creates a report'''
    headers = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    print('{:20} | {:20} | {:20} | {:20}'.format(*headers))
    for name, donations in donors.items():
        total = sum(donations)
        num = len(donations)
        avg = total / num
        spacing = '{:20} | {:20} | {:20} | {:20}'
        print(spacing.format(name, total, num, avg))
    print('\n')
    return

def letter_to_all():
        big_letter = ('Dear {},\n\n Thank you for you donation of {}\n'
        'your money will go a long way\n')
        for donor, donations in donors.items():
            print(big_letter.format(donor, sum(donations)))
            filename = donor.replace(' ', ' ') + '.txt'
            save = open(filename, 'w')
            save.write(big_letter.format(donor, sum(donations)))
            save.close()
        return


def main_menu():
    """main block"""
    while True:
        prompt = 'Please enter a donor\'s name or type list:\n'
        entry = input(prompt)
        if entry.lower() == "list":
            donor_list()
        elif entry.lower() == "quit":
            break
        else:
            try:
                assert entry in donors
                adding_a_donation(entry)
            except AssertionError:
                print('{entry} is not in list')
                adding_a_donor(entry)


main_prompt = ('\nDonation Update\n'
               'Please enter a selection\n'
               '1. Send a Thank You\n'
               '2. Create a report\n'
               '3. Mail all donors\n'
               '0. Exit menu\n'
               )

main_dispatch = {'1': main_menu,
                 '2': create_report,
                 '3': letter_to_all,
                 '0': quit
                 }


def menu(prompt, dispatch):
    while True:
        entry = input(prompt).lower()
        try:
            if dispatch.get(entry)() == "exit menu":
                break
        except TypeError:
            print("Invalid response please enter a number 0-4")


def quit():
    """ This function exits the executable"""
    print("Thanks for your time!")
    return 'exit menu'
    sys.exit()


if __name__ == '__main__':
    menu(main_prompt, main_dispatch)
