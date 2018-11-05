#!/usr/bin/env python3

import os

DONATIONS = {
    'Peter Pan': [10., 10., 10.],
    'Paul Hollywood': [5., 50000., 5., 5.],
    'Mary Berry': [100.],
    'Jake': [123., 456., 789.],
    'Raj': [60., 600000.]}

MAIN_PROMPT = ("\nWould you like to:\n"
               "1 - Send a Thank You\n"
               "2 - Create a Report\n"
               "3 - Send letters to everyone\n"
               "4 - Quit\n")


def doner_dict():
    return DONATIONS


def totals(donations):
    totals = {item: sum(donations[item]) for item in donations}
    return totals


def count(donations):
    count = {item: len(donations[item]) for item in donations}
    return count


def averages(d_totals, d_count):
    averages = {item: d_totals[item]/d_count[item] for item in DONATIONS}
    return averages


def update_records(name, donation):
    if name not in DONATIONS:
        DONATIONS[name] = [donation]
    else:
        DONATIONS[name].append(donation)


def thanks():
    while True:
        name = input('Please enter the Full Name of the donor')
        if name == 'list':
            print(DONATIONS.keys())
            continue
        else:
            break
    while True:
        try:
            donation = float(input('Please enter the amount of the donation'))
        except ValueError:
            print('input for the amount must be a numerical value')
        else:
            break
    update_records(name, donation)
    print(f'Dear {name}:')
    print(f'Thank you for your donation of ${donation:.2f} to our charity.')
    print(f'Your contribution will do a great deal to help our worthy cause')


def create_report():
    title_str = '{:<20s}|{:^13}|{:^11}|{:>13}'
    bar_str = '-'*60
    entry_str = '{:<20s} ${:>12} {:>11} ${:>12}'
    total_given = totals(DONATIONS)
    num = count(DONATIONS)
    avg = averages(total_given, num)
    total_sort = sorted(total_given.items(), key=lambda x: x[1], reverse=True)
    report = [title_str.format('Donor Name', 'Total Given',
                               'Num Gifts', 'Average Gift'), bar_str]
    for donor, total in total_sort:
        report.append(entry_str.format(*(donor, total,
                                         num[donor], avg[donor])))
    return report


def report():
    for row in create_report():
        print(row)


def letters():
    donors_list = [donor.replace(' ', '_') for donor in DONATIONS.keys()]
    existing_letters = [f[:-4] for f in os.listdir('.') if f.endswith('.txt')]
    acc_donation = totals(DONATIONS)
    for donor in set(donors_list) - set(existing_letters):
        donor_key = donor.replace('_', ' ')
        with open(donor+'.txt', 'w') as outfile:
            outfile.write("Dear {:}, \n".format(donor_key))
            outfile.write(f"Thank you for your accumulative \
                         donation of ${acc_donation[donor_key]:.2f}. \n")
            outfile.write('Your contribution will do a great \
                          deal to help our worthy cause')


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
    menu_selection(MAIN_PROMPT, MAIN_DISPATCH)
