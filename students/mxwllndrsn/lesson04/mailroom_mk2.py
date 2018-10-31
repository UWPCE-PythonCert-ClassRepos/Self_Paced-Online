#!/usr/bin/env python3

#uw python 210
#lesson 03
#max anderson

#mailroom.py

import os
import io
from datetime import date

donor_list = [
              ['Andrew Jackson', 10000, 5, 2000],
              ['Benjamin Franklin', 253000, 2, 117500],
              ['John Kennedy', 20, 1, 20],
              ['Abraham Lincoln', 807, 2, 403.5],
              ['Jim Jones', 918, 1, 918]
             ]

# Index 0 - Donor Name
# Index 1 - Donation Totals
# Index 2 - Number of Donations
# Index 3 - Average Donation

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
    print()
    name = input('Enter full name of \'Donor\': ').title()
    if in_list(name): donation_update(name)
    elif not in_list(name): donation_update(new_donor(name))

    letter = input('Create thank you letter? (y/n) ').title()
    if letter == 'Y': print(format_thx(name))
    elif letter == 'N': return


def list_donors():
    print()
    for donor in donor_list:
        print(donor[0])


def new_donor(name):
    donor_list.append([name, 0, 0, 0])
    print('New donor added. \n')
    return name


def donation_update(name):
    amount = float(input('Enter donation amount: '))
    i = get_index(name)
    #add amount to donation totals
    donor_list[i][1] += amount
    #increment number of donations
    donor_list[i][2] += 1
    #adjust average donation
    donor_list[i][3] = (donor_list[i][1] / donor_list[i][2])


def in_list(name):
    for i in range(len(donor_list)):
        if name == donor_list[i][0]:
            return 1
        elif name != donor_list[i][0] and i == len(donor_list):
            return 0


#returns the index of any known donor
def get_index(name):
    for i in range(len(donor_list)):
        if name == donor_list[i][0]:
            return i


def format_thx(name):
    i = get_index(name)
    prntstr = (f'{ymdate} \n\n')
    prntstr += (f'Dear {name}, \n\n')
    prntstr += ('Thank you for your generosity. '
                'Having donated {:} times for a total of ${:,.2f}, '
                'your most recent gift enables us to continue our mission '
                'of serving vulnerable populations in your local community. '
                'We can not overstate how important contributions like this '
                'are to our organization and those we serve. \n\n'
                .format(donor_list[i][2], donor_list[i][1]))
    prntstr += ('Sincerely, \n\n')
    prntstr += ('Automated Form letter')

    return prntstr

def create_report():
    print()
    print('Donor Name             | Donation Total   | Num   | Average')
    print('-----------------------------------------------------------')
    for i in range(len(donor_list)):
        print('{:<23}$ {:<17,.2f}{:<8d}$ {:<0,.2f}'.format(*donor_list[i]))
    return 1


def generate_letters():
    path = write_dir()
    for donor in donor_list:
        filename = ('{}_Thanks_{}.txt'.format(donor[0], ymdate))
        filename = os.path.join(path, filename)
        with open(filename, 'w+') as f:
            f.write(format_thx(donor[0]))


def write_dir():
    folder = input('Write to new folder? (y/n) ').title()
    if folder == 'Y':
        path = input('Folder name: ')
        os.makedirs(path)
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
