# Mailroom_pt4.py Exercise by tfbanks

# !/usr/bin/env python3

# pt4 update - I made some changes to clean up some code as well as broke out thank_you_letter so more easily test that function
import os
# Donor Database containing names and donations
donor_names = {
    'Tim Cooker': [1500.50, 25050.50, 15680.75],
    'Elon Musket': [5250.25, 26500],
    'Frank Petersmankempt': [550.60],
    'Megan Morgan': [650.40, 1600, 20625.40],
    'Marlene Wheeler': [820, 1222.80]}


def selection(option):
    switch_fun_dict = {1: thank_you_donor, 2: report, 3: mass_mail, 4: quit_option}
    return switch_fun_dict[option]


def thank_you_donor():  # Code for selecting Donor and writing a Thank You Note
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
        donor_names[ty_donor].append(amount)  # Appends donation amount to donators donation values
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
    print('\nDonor Name            |  Total Given | Num Gifts |  Average Gift\n'
    '------------------------------------------------------------------')
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


def quit_option():
    print('Have a nice day')
    os._exit(0)


if __name__ == '__main__':
    while True:
        answer = input('''\nPlease choose an action from the following options:
    1 - Send a Thank You
    2 - Create a Report
    3 - Send letters to everyone
    4 - Quit\n''')

        try:
            answer = int(answer)
        except ValueError:
            print('''Enter the actions's associated number''')
 
        try:
            selection(answer)()
        except KeyError:
            pass
