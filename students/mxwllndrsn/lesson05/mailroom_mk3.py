#!/usr/bin/env python3

#uw python 210
#lesson 05
#max anderson

#mailroom_mk3.py
#update w/ dictionary, comprehensions, exception handling

import os
import io
from datetime import date

donor = {
        'Andrew Jackson': [10000, 5, 2000],
        'Benjamin Franklin': [253000, 2, 117500],
        'John Kennedy': [20, 1, 20],
        'Abraham Lincoln': [807, 2, 403.5],
        'Jim Jones': [918, 1, 918]
        }

# Key: Donor Name
# Value: 3 item list
# Index 0 - Donation Totals
# Index 1 - Number of Donations
# Index 2 - Average Donation

ymdate = str(date.today())

#implementing dictionary function menu
def menu_select(prompt, menu):
    while(True):
        select = input(prompt)
        while(select not in menu.keys()):
            select = input('Please try again: ')
        if menu[select]() == 'exit':
            break


def exit_menu():
    print('Exiting...')
    return 'exit'


def manage_donors():
    menu_select(manage_prompt, manage_menu)


def enter_donation():
    prompt_thx(entry_update())


def list_donors():
    for key in donor.keys():
        print(key)


def entry_update():
    while True:
        try:
            name = input('Enter full name of donor: ').title()
            a, b = name.split()
            if a.isalpha() and b.isalpha(): break
            else: print('Please enter letters only...')
        except ValueError:
            print('Please enter first and last name...')
    while True:
        try:
            donation = float(input('Enter donation amount: '))
            break
        except ValueError:
            print('Please enter a numeric value...')

    entry = donor.setdefault(name, [0, 0, 0])
    entry[0] += donation
    entry[1] += 1
    entry[2] = entry[0]/entry[1]
    return name


def prompt_thx(name):
    while True:
        letter = input('Create thank you letter? (y/n) ').title()
        if letter == 'Y':
            print(format_thx(name))
            break
        elif letter == 'N': return
        else: print('Please enter \'y\' or \'n\'...')


def format_thx(name):
    prntstr = (f'{ymdate} \n\n')
    prntstr += (f'Dear {name}, \n\n')
    prntstr += ('Thank you for your generosity. '
                'Having donated {num:} times for a total of ${amount:,.2f}, '
                'your most recent gift enables us to continue our mission '
                'of serving vulnerable populations in your local community. '
                'We can not overstate how important contributions like this '
                'are to our organization and those we serve. \n\n'
                .format(num = donor.get(name)[1], amount = donor.get(name)[0]))
    prntstr += ('Sincerely, \n\n')
    prntstr += ('Automated Form letter')
    return prntstr


def create_report():
    print()
    print('Donor Name             | Donation Total   | Num   | Average')
    print('-----------------------------------------------------------')
    for key in donor.keys():
        print('{name:<23}$ {total:<17,.2f}{num:<8d}$ {avg:<0,.2f}'
              .format(name = key, total = donor.get(key)[0],
                      num = donor.get(key)[1], avg = donor.get(key)[2]))
    return


def generate_letters():
    path = write_dir()
    for key in donor.keys():
        filename = ('{}_Thanks_{}.txt'.format(key, ymdate))
        filename = os.path.join(path, filename)
        while True:
            try:
                with open(filename, 'w+') as f:
                    f.write(format_thx(key))
                break
            except FileNotFoundError:
                print('Unable to write file...')

def write_dir():
    folder = input('Write to new folder? (y/n) ').title()
    if folder == 'Y':
        while True:
            path = input('Folder name: ')
            try:
                os.makedirs(path)
                break
            except FileNotFoundError:
                print('Please enter a valid path name: ')
    elif folder == 'N':
        print(f'Writing to current directory: {os.getcwd()}')
        path = ''
    return path


main_menu = {
             '1': manage_donors,
             '2': create_report,
             '3': generate_letters,
             '4': exit_menu,
            }


main_prompt = (
               '\n'
               'Main Menu\n'
               '--------- \n'
               '1) Manage Donors \n'
               '2) Create Report \n'
               '3) Generate Letters \n'
               '4) Exit \n\n'
               'Enter a number: '
              )


manage_menu = {
               '1': enter_donation,
               '2': list_donors,
               '3': exit_menu,
              }

manage_prompt = (
                 '\n'
                 'Manage Donors \n'
                 '------------- \n'
                 '1) Enter Donation \n'
                 '2) List Current \n'
                 '3) Exit \n\n'
                 'Enter a number: '
                )


if __name__ == "__main__":

    print('\n'
          '---------------------- \n'
          'Welcome to Mail Room™ \n'
          '----------------------'
          )

    menu_select(main_prompt, main_menu)
