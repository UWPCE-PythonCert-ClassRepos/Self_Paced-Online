# Mailroom_pt5py Exercise by tfbanks

# !/usr/bin/env python3

import os
# Donor Database containing names and donations



class Donor:
    def __init__(self, donations=None):
        self.donations = donations if donations else []


donor_data = {
        'Tim Cooker': [1500.50, 25050.50, 15680.75],
        'Elon Musket': [5250.25, 26500],
        'Frank Petersmankempt': [550.60],
        'Megan Morgan': [650.40, 1600, 20625.40],
        'Marlene Wheeler': [820, 1222.80]} 


class Donor_Actions:

    def add_new_donor(donor, donations):
        donor_data.setdefault((donor),[]).append(donations)  

    def update_donor_donations(donor, donations):
        donor_data[donor].append(donations)

    #Returns sorted list of all donors

    def all_donors():
        donors = list(donor_data.keys())
        return sorted(donors)

    def thank_you_donor(): # inputting a new donor and/or new donations
        donor = donor_prompt()
        if donor == 'List':  # If List, Prints Donor List and restarts the function
            print(Donor_Actions.all_donors())
            donor = donor_prompt()

        while True:
            try:
                donations = float(donations_prompt())
            except ValueError:
                print('Please enter a valid donations amount')
            else:
                break

        if donor not in donor_data:
            Donor_Actions.add_new_donor(donor, donations)
        else:                
            Donor_Actions.update_donor_donations(donor, donations)
        return Donor_Actions.thank_you_letter(donor, donations)


    def thank_you_letter(donor, donations):
        letter = ('''\n\nDear {},\n
    Thank you for your generous donation of ${:,.2f}, your generosity is greatly appreciated.
These funds will help continue our efforts to teach Python to the next generation.\n
Sincerely,\n\n
Joesef Edword Bringingham''').format(donor, donations)
        print(letter)
        return letter

    def report():  # Defines parameters of the report of donors and prints it.
        donor_rpt = [[donor, sum(donations), len(donations), sum(donations) / len(donations)] for donor, donations in
                 donor_data.items()]
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
        for donor, donations in donor_data.items():
            with open(donor + '.txt', 'w') as output:
                output.write(mm_letter.format(donor, sum(donations)))
        print('\nLetters are located in your working directory folder\n\n')
 

## Main Options

def selection(option):
    switch_fun_dict = {1: Donor_Actions.thank_you_donor, 2: Donor_Actions.report, 3: Donor_Actions.mass_mail, 4: quit_option}
    return switch_fun_dict[option]


def quit_option():
    print('Have a nice day')
    os._exit(0)
    

def donor_prompt():
    return input('Enter the Full Name of a donor (for list of previous donors type list): ').title()          


def donations_prompt():
    return float(input('Please enter the donations amount: '))


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
