# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:51:56 2018

@author: Laura.Fiorentino
"""

from mailroom_oo import *
import sys

#donor_list = Donor('Frank Reynolds', [10, 20, 50])
#donor_list.new_donation('Dee Reynolds', [25, 100])
#donor_list.new_donation('Dennis Reynolds', [10, 50])
#donor_list.new_donation('Mac McDonald', [25, 35, 20])
#donor_list.new_donation('Charlie Kelly', 0.25)

#donor = Donor('Frank Reynolds', [10, 20, 50])

donor_list = Donor_List()
donor_list.add_donation('Frank Reynolds', [10, 20, 50])
donor_list.add_donation('Dee Reynolds', [25, 100])
donor_list.add_donation('Dennis Reynolds', [10, 50])
donor_list.add_donation('Mac McDonald', [25, 35, 20])
donor_list.add_donation('Charlie Kelly', 0.25)


def view_donor(donor_list):
    name = input('Donor Name?>')
    while True:
        if donor_list.is_donor(name) is True:
            donor_list.donors[name].list_donations
            yn = input('Would you like to add a new donation? y/n>')
            if yn == 'y':
                new_donation = input('Donation Amount?>')
                donor_list.add_donation(name, new_donation)
                donor_list.donors[name].list_donations
            else:
                quit_program()
        else:
            print('no such donor')
            break


def add_donor(donor_list):
    while True:
        name = input('Type Donor Name or q to quit?>')
        if name == 'q':
            quit_program()
        else:
            donation = input('Donation Amount?>')
            donor_list.add_donation(name, donation)
            donor_list.donors[name].list_donations


def donor_data(donor_list):
    while True:
        arg_dict = {'1': list_donors, '2': view_donor, '3': add_donor, 
                    '4': quit_program}
        task = input('Choose an action: [1] List Donors; '
                     '[2] View Donor Information; '
                     '[3] Add Donor; [4] Quit>') 
        try:
            arg_dict[task](donor_list)
        except KeyError:
            print('Error: Please choose 1-4')


def create_letters(donor_list):
    pass


def quit_program(donor_list):
    sys.exit()


def main():
    print('----------Mailroom----------')
    print('WARNING: This is all CAPS senstive for now!!!!!!!!!!')
    arg_dict = {'1': donor_data, '2': create_letters,
                '3': create_report, '4': quit_program}
    task = input('Choose an action: [1] Donor Database; ' 
                 '[2] Create Thank You Letters; [3] Create a Full Report; ' 
                 '[4] Quit>')
    try:
        arg_dict[task](donor_list)
    except KeyError:
        print('Error: Please choose 1-4')


if __name__ == '__main__':
    main()
