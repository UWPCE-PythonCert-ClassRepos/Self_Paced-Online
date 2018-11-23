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
    totals = {}
    for item in donations:
        totals[item] = sum(donations[item])
    return totals

def count(donations):
    count = {}
    for item in donations:
        count[item] = len(donations[item])
    return count

def averages(d_totals, d_count):
    averages = {}
    for item in donations:
        averages[item] = d_totals[item]/d_count[item]
    return averages

def thanks():
    while True:
        name = input('Please enter the Full Name of the donor')
        if name == 'list':
            print(donations.keys())
            continue
        else:
            break
    donation = float(input('Please enter the amount of the donation'))
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
    print(title_str.format('Donor Name','Total Given','Num Gifts','Average Gift'))
    print(bar_str)
    for donor, total in total_sort:
        print(entry_str.format(*(donor, total, num[donor], avg[donor])))

def letters():
    donors_list = [donor.replace(' ','_') for donor in donations.keys()]
    existing_letters = [f[:-4] for f in os.listdir('.') if f.endswith('.txt')]
    acc_donation = totals(donations)
    for donor in set(donors_list) - set(existing_letters):
        donor_key = donor.replace('_',' ')
        outfile = open(donor+'.txt', 'w')
        outfile.write("Dear {:}, \n".format(donor_key))
        outfile.write(f"Thank you for your accumulative donation of ${acc_donation[donor_key]:.2f}. \n")
        outfile.write('Your contribution will do a great deal to help our worthy cause')
        outfile.close()

def quit():
    print("Quitting program")
    return "exit menu"

#selector dict
def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if dispatch_dict[response]() == "exit menu":
            break

main_dispatch = {
    '1':thanks,
    '2':report,
    '3':letters,
    '4':quit
}

if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)

