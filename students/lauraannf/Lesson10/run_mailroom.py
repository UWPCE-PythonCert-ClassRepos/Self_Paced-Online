# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:23:17 2018

@author: Laura.Fiorentino
"""

import mailroom_fp as mfp
import sys
import datetime
import os
from functools import reduce


donor_list = mfp.Donor_List()
donor_list.add_donation('Frank Reynolds', [10, 20, 50])
donor_list.add_donation('Dee Reynolds', [25, 100])
donor_list.add_donation('Dennis Reynolds', [10, 50])
donor_list.add_donation('Mac McDonald', [25, 35, 20])
donor_list.add_donation('Charlie Kelly', 0.25)


def quit_program():
    sys.exit()


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


def create_letters():
    while True:
        letter_choice = input('Who would you like to write a donation letter '
                              'to? ([A] for all, [Q] to quit)>')
        if letter_choice.upper() == 'A':
            all_letters()
            quit_program()
        elif letter_choice.upper == 'Q':
            quit_program()
        elif donor_list.is_donor(letter_choice) is False:
            print('not a donor')
        else:
            donation_choice = input('What donation amount?  Choose [L] for '
                                    'latest donation,[A] for sum of all, '
                                    'or type the amount.')
            print('writing letter to {}'.format(letter_choice))
            if donation_choice.upper == 'L':
                donation = donor_list.donors[letter_choice].last_donation
            elif donation_choice.upper == 'A':
                donation = donor_list.donors[letter_choice].total_donation
            else:
                donation = float(donation_choice)
            write_letter(letter_choice, donation)


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


def create_folder():
    now = datetime.datetime.now()
    new_path = os.path.join(os.getcwd(), 'letters_' + now.strftime('%d%m%Y'))
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    return new_path, now


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


def list_donors():
    for key in donor_list.donors:
        print('{}'.format(key))


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


def challenge():
    global donor_list
    match_value = float(input('By how much would the philanthropist like '
                              'to match?>'))
    min_donation = float(input('Minimum donation eligible?>'))
    max_donation = float(input('Maximum donation eligible?>'))
    new_donor_list = mfp.Donor_List()
    for key in donor_list.donors:
            donations = multiplier(donor_list, match_value, min_donation,
                                   max_donation, key)
            new_donor_list.add_donation(key, donations)
    donor_list = new_donor_list


def projections():
    global donor_list
    match_value = float(input('By how much might you wish to match?>'))
    min_donation = float(input('Minimum donation eligible?>'))
    max_donation = float(input('Maximum donation eligible?>'))
    new_donor_list = mfp.Donor_List()
    for key in donor_list.donors:
            donations = multiplier(donor_list, match_value, min_donation,
                                   max_donation, key)
            new_donor_list.add_donation(key, donations)
    current_total = reduce(lambda x, y: x + y,
                           [donor_list.donors[key].total_donation for key in
                            donor_list.donors])
    new_total = reduce(lambda x, y: x + y, [new_donor_list.donors[key].
                                            total_donation for key in
                                            new_donor_list.donors])
    print('Our current total donations are: ${:.2f}'.format(current_total))
    print('If you match the donations above ${:.2f} and below ${:.2f} by '
          '{:.0f}%, our total donations will be ${:.2f}'
          .format(min_donation, max_donation, match_value * 100, new_total))


def multiplier(donor_list, match_value, min_donation, max_donation, key):
    donations_new = list(map(lambda x: x * match_value,
                             list(filter(lambda x: min_donation
                                         <= x <= max_donation,
                                         donor_list.donors[key]))))
    donations_orig = list(filter(lambda x: x < min_donation or x >
                                 max_donation, donor_list.donors[key]))
    donations = donations_new + donations_orig
    return donations


def main():
    print('----------Mailroom----------')
    print('WARNING: This is all CAPS senstive for now!!!!!!!!!!')
    arg_dict = {'1': donor_data, '2': create_letters,
                '3': create_report, '4': challenge,
                '5': projections, '6': quit_program}
    task = input('Choose an action: [1] Donor Database; '
                 '[2] Create Thank You Letters; [3] Create a Full Report; '
                 '[4] Match Donations; [5] Projections; [6] Quit>')
    try:
        arg_dict[task]()
    except KeyError:
        print('Error: Please choose 1-4')


if __name__ == '__main__':
    main()
