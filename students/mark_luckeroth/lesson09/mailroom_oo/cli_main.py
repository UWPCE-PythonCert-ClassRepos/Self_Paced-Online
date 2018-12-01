#!/usr/bin/env python3

import os
from donor_models import Donor, DonorCollection

MAIN_PROMPT = ("\nWould you like to:\n"
               "1 - Send a Thank You\n"
               "2 - Create a Report\n"
               "3 - Send letters to everyone\n"
               "4 - Quit\n")


def thanks():
    while True:
        first = input('Please enter the First Name of the donor')
        if first == 'list':
            print(donors.names)
            continue
        else:
            break
    last = input('Please enter the Last Name of the donor')
    while True:
        try:
            donation = float(input('Please enter the amount of the donation'))
        except ValueError:
            print('input for the amount must be a numerical value')
        else:
            break
    donors.update(first, last, donation)
    print(f'Dear {first} {last}:')
    print(f'Thank you for your donation of ${donation:.2f} to our charity.')
    print(f'Your contribution will do a great deal to help our worthy cause')


def create_report():
    title_str = '{:<20s}|{:^13}|{:^11}|{:>13}'
    bar_str = '-'*60
    entry_str = '{:<7s} {:<12s} ${:>12} {:>11} ${:>12}'
    donors.donorlist.sort(reverse=True)
    report = [title_str.format('Donor Name', 'Total Given',
                               'Num Gifts', 'Average Gift'), bar_str]
    for donor in donors.donorlist:
        report.append(entry_str.format(*(donor.first_name, donor.last_name,
                                         donor.total,
                                         donor.count, donor.average)))
    return report


def report():
    for row in create_report():
        print(row)


def letters():
    for donor in donors.donorlist:
        with open(donor.first_name+'_'+donor.last_name+'.txt', 'w') as outfile:
            outfile.write("Dear {:} {:}, \n".format(donor.first_name,
                                                    donor.last_name))
            outfile.write(f"Thank you for your accumulative donation of ${donor.total:.2f}. \n")
            outfile.write('Your contribution will do a great deal to help our worthy cause')


def quit():
    print("Quitting program")
    return "exit menu"


def menu_selection(prompt, dispatch_dict):
    while True:
        try:
            response = input(prompt)
            if dispatch_dict[response]() == "exit menu":
                break
        except KeyError:
            print('input must be one of the following: 1, 2, 3, or 4:')


MAIN_DISPATCH = {
    '1': thanks,
    '2': report,
    '3': letters,
    '4': quit
}

if __name__ == '__main__':
    donors = DonorCollection()
    donors.load_donors()
    menu_selection(MAIN_PROMPT, MAIN_DISPATCH)