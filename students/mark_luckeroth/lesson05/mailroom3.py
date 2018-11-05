#!/usr/bin/env python3

import os

donations = {
    'Peter Pan': [10., 10., 10.],
    'Paul Hollywood': [5., 50000., 5., 5.],
    'Mary Berry': [100.],
    'Jake': [123., 456., 789.],
    'Raj': [60., 600000.]}

main_prompt = ("\nWould you like to:\n"
               "1 - Send a Thank You\n"
               "2 - Create a Report\n"
               "3 - Send letters to everyone\n"
               "4 - Quit\n")


def totals(donations):
    totals = {item: sum(donations[item]) for item in donations}
    return totals


def count(donations):
    count = {item: len(donations[item]) for item in donations}
    return count


def averages(d_totals, d_count):
    averages = {item: d_totals[item]/d_count[item] for item in donations}
    return averages


def thanks():
    while True:
        name = input('Please enter the Full Name of the donor')
        if name == 'list':
            print(donations.keys())
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
    if name not in donations:
        donations[name] = [donation]
    else:
        donations[name].append(donation)
    print(f'Dear {name}:')
    print(f'Thank you for your donation of ${donation:.2f} to our charity.')
    print(f'Your contribution will do a great deal to help our worthy cause')


def report():
    title_str = '{:<20s}|{:^13}|{:^11}|{:>13}'
    bar_str = '-'*60
    entry_str = '{:<20s} ${:>12} {:>11} ${:>12}'
    total_given = totals(donations)
    num = count(donations)
    avg = averages(total_given, num)
    total_sort = sorted(total_given.items(), key=lambda x: x[1], reverse=True)
    print(title_str.format('Donor Name', 'Total Given',
                           'Num Gifts', 'Average Gift'))
    print(bar_str)
    for donor, total in total_sort:
        print(entry_str.format(*(donor, total, num[donor], avg[donor])))


def letters():
    donors_list = [donor.replace(' ', '_') for donor in donations.keys()]
    existing_letters = [f[:-4] for f in os.listdir('.') if f.endswith('.txt')]
    acc_donation = totals(donations)
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


main_dispatch = {
    '1': thanks,
    '2': report,
    '3': letters,
    '4': quit
}

if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)
