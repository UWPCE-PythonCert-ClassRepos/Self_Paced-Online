#!/usr/bin/env python3

#uw python 210
#lesson 05
#max anderson

#mailroom_mk4.py
#general refactor

import os
import io
from collections import defaultdict
from datetime import date

donor = defaultdict(lambda: [0, 0, 0],
        {
        'Andrew Jackson': [10000, 5, 2000],
        'Benjamin Franklin': [253000, 2, 117500],
        'John Kennedy': [20, 1, 20],
        'Abraham Lincoln': [807, 2, 403.5],
        'Jim Jones': [918, 1, 918]
        })

# Defaulting Dictionary Value [0, 0, 0]
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
    name = get_name()
    donation = get_donation()
    entry_update(name, donation)
    prompt_thx(name)


def list_donors():
    for key in donor.keys():
        print(key)
    return list(donor.keys())


def entry_update(name, donation):
    entry = donor[name]
    entry[0] += donation
    entry[1] += 1
    entry[2] = entry[0]/entry[1]
    return entry


def prompt_thx(name):
    while True:
        letter = input('Create thank you letter? (y/n) ').title()
        if letter == 'Y':
            print(format_thx(name))
            break
        elif letter == 'N': return
        else: print('Please enter \'y\' or \'n\'...')


# Reading from external template file makes changes to formatting easier,
# however, a file stream is opened every time this function is called.
# In the case of generate_letters() for every key in the dict.
# Bad practice?
def format_thx(name):
    prntstr = ''
    with open('format_thx.txt', 'r') as instream:
      for line in instream:
        prntstr += line.format(date = ymdate, name = name,
                               total = donor.get(name)[0],
                               number = donor.get(name)[1])
    return prntstr


# print report by passing key from sorted list to dict.get()
def create_report():
    sorted_donors = sort_donations()
    heading = 'Donor Name             | Donation Total   | Num   | Average'
    print('\n', heading, '\n', ('-'*len(heading)))
    for entry in sorted_donors:
        k = entry[0]
        print(' {name:<23}$ {total:<17,.2f}{num:<8d}$ {avg:<0,.2f}'
              .format(name = k, total = donor.get(k)[0],
                      num = donor.get(k)[1], avg = donor.get(k)[2]))


# grab and return sort of biggest donors
def sort_donations():
    return sorted(donor.items(), key = lambda x : x[1][0], reverse = True)


def generate_letters():
    path = write_dir()
    for key in donor.keys():
        filename = ('{}_Thanks_{}.txt'.format(key, ymdate))
        filename = os.path.join(path, filename)
        try:
            with open(filename, 'w+') as outstream:
                outstream.write(format_thx(key))
        except(FileNotFoundError, OSError):
            print('Unable to write file...')


def write_dir():
    folder = input('Write to new folder? (y/n) ').title()
    if folder == 'Y':
        path = input('Folder name: ')
        try:
            os.makedirs(path)
        except(FileNotFoundError, OSError):
            print('Invalid path... ')
    elif folder == 'N':
        print(f'Writing to current directory: {os.getcwd()}')
        path = ''
    return path


def get_name():
    while True:
        try:
            name = input('Enter full name of donor: ').title()
            a, b = name.split()
            if a.isalpha() and b.isalpha(): break
            else: print('Please enter text only...')
        except ValueError:
            print('Please enter first and last name...')
    return name


def get_donation():
    while True:
        try:
            donation = float(input('Enter donation amount: '))
            break
        except ValueError:
            print('Please enter a numeric value...')
    return donation


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
