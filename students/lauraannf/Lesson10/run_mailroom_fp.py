# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:51:56 2018

@author: Laura.Fiorentino
"""


import mailroom_fp as mfp
import sys
import datetime
import os


donor_list = mfp.Donor_List()
donor_list.add_donation('Frank Reynolds', [10, 20, 50])
donor_list.add_donation('Dee Reynolds', [25, 100])
donor_list.add_donation('Dennis Reynolds', [10, 50])
donor_list.add_donation('Mac McDonald', [25, 35, 20])
donor_list.add_donation('Charlie Kelly', 0.25)


def view_donor():
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


def add_donor():
    while True:
        name = input('Type Donor Name or q to quit?>')
        if name == 'q':
            quit_program()
        else:
            donation = input('Donation Amount?>')
            donor_list.add_donation(name, donation)
            donor_list.donors[name].list_donations


def donor_data():
    while True:
        arg_dict = {'1': list_donors, '2': view_donor, '3': add_donor,
                    '4': quit_program}
        task = input('Choose an action: [1] List Donors; '
                     '[2] View Donor Information; '
                     '[3] Add Donor; [4] Quit>')
        try:
            arg_dict[task]()
        except KeyError:
            print('Error: Please choose 1-4')


def create_letters():
    while True:
        letter_choice = input('Who would you like to write a donation letter '
                              'to? (type a for all, q to quit)>')
        if letter_choice == 'a':
            all_letters()
            quit_program()
        elif letter_choice == 'q':
            quit_program()
        elif donor_list.is_donor(letter_choice) is False:
            print('not a donor')
        else:
            donation_choice = input('What donation amount?  Choose [L] for '
                                    'latest donation,[A] for sum of all, '
                                    'or type the amount.')
            print('writing letter to {}'.format(letter_choice))
            if donation_choice == 'L':
                donation = donor_list.donors[letter_choice].last_donation
            elif donation_choice == 'A':
                donation = donor_list.donors[letter_choice].total_donation
            else:
                donation = float(donation_choice)
            write_letter(letter_choice, donation)


def create_folder():
    now = datetime.datetime.now()
    new_path = os.path.join(os.getcwd(), 'letters_' + now.strftime('%d%m%Y'))
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    return new_path, now


def all_letters():
    print('writing all thank you letters...')
    for key in donor_list.donors.keys():
        write_letter(key, donor_list.donors[key].total_donation)


def write_letter(name, donation):
    new_path, now = create_folder()
    with open(os.path.join(new_path, name + '_' + now.strftime('%d%m%Y') +
              '.txt'), 'w') as letter_file:
            letter_file.write('Dear {}, \n'
                              'Thank you so much for your generous '
                              'donation of ${:.2f} \n'
                              'Sincerely, \n'
                              'Laura F'.format(name, donation))


def quit_program():
    sys.exit()


def philanthropist():
#    global new_donor_list
    new_donor_list = mfp.Donor_List()
    match_value = float(input('By how much would the philanthropist like '
                              'to match?>'))
    min_donation = float(input('Minimum donation eligible?>'))
    max_donation = float(input('Maximum donation eligible?>'))
    for key in donor_list.donors:
        donations = list(map(lambda x: x * match_value,
                             donor_list.donors[key]))
        new_donor_list.add_donation(key, donations)


def create_report():
    print('-------List of Donors-------')
    print('{:<20}{:<20}{:<20}{:<20}'.format('Donor Name', 'Total Donated',
                                            '# of donations',
                                            'Average donation'))
    print('-----------------   '*4)
    for key in donor_list.donors.keys():
        print('{:<20}${:<20.2f}{:<20d}$'
              '{:<20.2f}'.format(key, donor_list.donors[key].total_donation,
                                 donor_list.donors[key].number_donation,
                                 donor_list.donors[key].avg_donation))


def list_donors():
    for key in donor_list.donors:
        print('{}'.format(key))


def main():
    print('----------Mailroom----------')
    print('WARNING: This is all CAPS senstive for now!!!!!!!!!!')
    arg_dict = {'1': donor_data, '2': create_letters,
                '3': create_report, '4': philanthropist,
                '5': quit_program}
    task = input('Choose an action: [1] Donor Database; '
                 '[2] Create Thank You Letters; [3] Create a Full Report; '
                 '[4] Match Donations; [5] Quit>')
    try:
        arg_dict[task]()
    except KeyError:
        print('Error: Please choose 1-4')


if __name__ == '__main__':
    main()


if 'new_donor_list' in globals():
    donor_list = new_donor_list
