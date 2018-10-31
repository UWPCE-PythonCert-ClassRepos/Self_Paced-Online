# Mailroom_fp.py Exercise by tfbanks

# !/usr/bin/env python3

"""fp update - I adjusted the donations for the donors to make the challenge and projection calculations
have something to work with. """

import os
# Donor Database containing names and donations
donor_names = {
    'Tim Cooker': [1500.50, 25050.50, 15680.75],
    'Elon Musket': [5250.25, 26500],
    'Frank Petersmankempt': [45, 75, 100],
    'Megan Morgan': [25, 45.75, 65, 82.5, 120.75, 150],
    'Marlene Wheeler': [45, 60, 75, 480, 820, 1250.80]}


def selection(option):
    switch_fun_dict = {1: thank_you, 2: report, 3: mass_mail, 4: challenge, 5: run_projections, 6: quit_option}
    return switch_fun_dict[option]


def thank_you():  # Code for selecting Donor and writing a Thank You Note
    ty_donor = input('Enter the Full Name of a donor (for list of previous donors type list): ').title()
    if ty_donor == 'List':  # If List, Prints Donor List and restarts the function
        for donor in donor_names.keys():
            print(donor)
        ty_donor = input('Enter the Full Name of a donor (for list of previous donors type list): ').title()

    while True:
        try:
            amount = float(input('Please enter the donation amount: '))
        except ValueError:
            print('Please enter a valid donation amount')
        else:
            break
    if ty_donor in donor_names:  # Actions if donor is already in donor_names
        donor_names[ty_donor].append(amount)  # Appends donation amount to donor's donation values
    else:
        donor_names[ty_donor] = [amount]
    return thank_you_letter(ty_donor, amount)


def thank_you_letter(ty_donor, amount):
    letter = ('''\n\nDear {},\n
Thank you for your generous donation of ${:,.2f}, your generosity is greatly appreciated.
These funds will help continue our efforts to teach Python to the next generation.\n
Sincerely,\n\n
Joesef Edword Bringingham''').format(ty_donor, amount)
    print(letter)
    return letter

    
def report():  # Defines parameters of the report of donors and prints it.
    donor_rpt = [[donor, sum(donations), len(donations), sum(donations) / len(donations)] for donor, donations in
                 donor_names.items()]
    sorted_rpt = sorted(donor_rpt, key=lambda x: x[1], reverse=True)
    print('\nDonor Name            |  Total Given | Num Gifts |  Average Gift')
    print('------------------------------------------------------------------\n')
    for donor_rpt in sorted_rpt:
        print('{:24s}''${:11,.2f}''{:^17}''${:11,.2f}'.format(donor_rpt[0], donor_rpt[1], donor_rpt[2], donor_rpt[3]))


def mass_mail():
    mm_letter = ('''\n\nDear {},\n
Thank you for your generous donations totaling ${:,.2f}, your generosity is greatly appreciated.
These funds will help continue our efforts to teach Python to the next generation.\n
Sincerely,\n\n 
Joesef Edword Bringingham\n\n''')
    for donor, donations in donor_names.items():
        with open(donor + '.txt', 'w') as output:
            output.write(mm_letter.format(donor, sum(donations)))
    print('\nLetters are located in your working directory folder\n\n')


def challenge():
    min_donation = float(input('Please input the donation minimum: '))
    max_donation = float(input('Please input the donation maximum: '))
    factor = int(input('Please input a challenge factor: '))
    filtered_donors = dict(list((key, list(filter(lambda x: x >= min_donation and x<= max_donation, value)))
                                for key, value in donor_names.items()))
    new_donor_data = dict(list((key, list(map(lambda y: y*factor, value))) for key, value in filtered_donors.items()))
    print('\n The new donor data set using a factor of {} for only those donations between ${:,.2f} and ${:,.2f} would '
          'be as follows: \n'.format(factor, min_donation, max_donation))
    print(new_donor_data)


def projection_functions(limit, factor):
    base_donations = dict(list((key, list(filter(lambda x: x >= limit, value))) for key, value in donor_names.items()))
    filtered_donations = dict(list((key, list(filter(lambda x: x < limit, value)))
                                   for key, value in donor_names.items()))
    adj_donation_calc = dict(list((key, list(map(lambda y: y*factor, value)))
                                  for key, value in filtered_donations.items()))

    for key in base_donations:
        base_donations[key].extend(adj_donation_calc[key])
    return base_donations


def run_projections():
    amount1 = float(input('Please input a minimum amount for projection scenario 1: '))
    factor1 = int(input('Please input a match factor for projecction scenario 1: '))
    print('\n')
    amount2 = float(input('Please input a minimum amount for projection scenario 2: '))
    factor2 = int(input('Please input a match factor for projecction scenario 2: '))
    print('\n\n')

    adj_donor_data1 = projection_functions(amount1, factor1)
    filtered_donations = dict(list((key, list(filter(lambda x: x < amount1, value)))
                                   for key, value in donor_names.items()))

    print('Individual donor results for projection scenario 1 are as follows:\n')
    for key in adj_donor_data1:
        if sum(donor_names[key]) == sum(adj_donor_data1[key]):
            print("{} has no donations under ${:,.2f}.  As a result, {}'s total donation amount would remain at "
                  "${:,.2f}\n".format(key, amount1, key, sum(adj_donor_data1[key])))
        else:
            print("{} has {} donation(s) under ${:,.2f}.  If each was adjusted the match factor of {}, then {}'s "
                  "total donation would increase from ${:,.2f} to ${:,.2f}\n.".format(key, len(filtered_donations[key]),
                                                                                      amount1, factor1, key,
                                                                                      sum(donor_names[key]),
                                                                                      sum(adj_donor_data1[key])))
    print('\n\n')
    
    adj_donor_data2 = projection_functions(amount2,factor2)
    filtered_donations = dict(list((key,list(filter(lambda x: x < amount2, value)))
                                   for key, value in donor_names.items()))
    print('Individual donor results for projection scenario 2 are as follows:\n')    
    for key in adj_donor_data2:
        if sum(donor_names[key]) == sum(adj_donor_data2[key]):
            print("{} has no donations under ${:,.2f}.  As a result, {}'s total donation amount would remain "
                  "at ${:,.2f}\n".format(key, amount2, key, sum(adj_donor_data2[key])))
        else:
            print("{} has {} donation(s) under ${:,.2f}.  If each was adjusted the match factor of {}, then {}'s "
                  "total donation would increase from ${:,.2f} to ${:,.2f}\n.".format(key, len(filtered_donations[key]),
                                                                                      amount2, factor2, key,
                                                                                      sum(donor_names[key]),
                                                                                      sum(adj_donor_data2[key])))


def quit_option():
    print('Have a nice day')
    os._exit(0)


if __name__ == '__main__':
    while True:
        answer = input('''\nPlease choose an action from the following options:
    1 - New Donation / Send a Thank You
    2 - Create a Report
    3 - Send thank you letters to everyone
    4 - Contribution Challenge
    5 - Run Projections
    6 - Quit\n''')

        try:
            answer = int(answer)
        except ValueError:
            print('''Enter the actions's associated number''')
 
        try:
            selection(answer)()
        except KeyError:
            pass
