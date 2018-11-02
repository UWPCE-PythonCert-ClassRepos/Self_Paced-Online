# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 11:18:22 2018

@author: Laura.Fiorentino
"""
import datetime
import sys
import os

donor_list = {
    'Frank Reynolds': [10, 20, 50],
    'Dee Reynolds': [25, 100],
    'Dennis Reynolds': [10, 50],
    'Mac McDonald': [25, 35, 20],
    'Charlie Kelly': [0.25]
    }


def add_donation(name, donation):
    donor_list[name].append(donation)


def create_email():
    while True:
        name = input("Type full donor name, ''list'' for choices, or \
'quit' to quit>")
        if name.lower() == 'list':
            print(donor_list.keys())
        elif name.lower() == 'quit':
            quit_program()
        else:
            donation = float(input("Donation Amount?>"))
            try:
                add_donation(name, donation)
            except KeyError:
                donor_list[name] = []
                add_donation(name, donation)
            finally:
                print('writing the thank you letter...')
                write_email(name, donation)
            break


def create_report():
    print('-------List of Donors-------')
    print('{:<20}{:<20}{:<20}{:<20}'.format('Donor Name', 'Total Donated',
                                            '# of donations',
                                            'Average donation'))
    print('-----------------   '*4)
    for key in donor_list.keys():
        print('{:<20}${:<20.2f}{:<20d}${:<20.2f}'.format(key,
                                                         sum(donor_list[key]),
                                                         len(donor_list[key]),
                                                         sum(donor_list[key])
                                                         / len(donor_list[key]
                                                               )))


def create_folder():
    now = datetime.datetime.now()
    new_path = os.getcwd() + '\\' + 'letters_' + now.strftime('%d%m%Y')
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    return new_path, now


def all_letters():
    print('writing all thank you letters...')
    for key in donor_list.keys():
        write_email(key, sum(donor_list[key]))


def write_email(name, donation):
    new_path, now = create_folder()
    with open(new_path + '\\' + name + '_' + now.strftime('%d%m%Y') +
              '.txt', 'w') as letter_file:
            letter_file.write('Dear {}, \n'
                              'Thank you so much for your generous '
                              'donation of ${:.2f} \n'
                              'Sincerely, \n'
                              'Laura F'.format(name, donation))


def quit_program():
    sys.exit()


def main():
    print('----------Mailroom----------')
    arg_dict = {'1': create_email, '2': create_report, '3': all_letters,
                '4': quit_program}
    task = input("Choose an action: [1] Send a Thank You; [2] Create a \
Report; [3] Send a Thank You to Everyone; [4] Quit>")
    try:
        arg_dict[task]()
    except KeyError:
        print('Error: Please choose 1-4')


if __name__ == '__main__':
    main()
