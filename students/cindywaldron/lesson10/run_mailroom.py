#!/usr/bin/env python3

from datetime import date
from mailroom import Donor, Donations

collection = Donations()

options = { 1: 'Send Thank You', 2: 'Create a Report', 3:'Send letters to everyone', 4: 'Projections', 5:'Quit'}

def send_thank_you():
    """This function asks user to enter name and donation amount"""
    full_name = 'Enter a full name (enter Q to main menu): '
    donation_amount = 'Enter donation amount(enter Q to main menu):'
    response = input(full_name)
    # display all donors' names if input is 'list'
    while response == 'list':
        print("\n".join(collection.donors))
        response = input(full_name)
    # if input is not 'Q' to quit
    if response.upper() != 'Q':
        amount_input = input(donation_amount)
        if amount_input.upper() != 'Q':
            try:
                amount = float(amount_input)
                donor = Donor(response, [amount])
                collection.add(donor)
                # thank you email
                print(donor.get_letter_text(response, amount))
            except ValueError:
                print('Input must be a float.  try again')

def send_letters():
    """Send letters to all donors"""
    for k, v in collection.donors.items():
        letter = v.get_letter_text(k, v.amount)
       # strip ','
        filename = k.replace(',','')
       # replace space with '_'
        filename = filename.replace(' ', '_')
        # open file to write
        with open('{}-{}{}'.format(filename, str(date.today()),'.txt'), 'w') as thefile:
            thefile.write(letter)


def create_report():
    print(collection.generate_report())

def projections():
    """User inputs to project total donations"""
    factor = 0
    min_donation = 0
    max_donation = 0
    while True:
        # ask for a factor
        factor = input('Enter a multiplier(factor):')
        try:
            factor = int(factor)
            if factor > 0:
                break
            else:
                print('Input must be greater than 0. try again')
        except ValueError:
            print('Input must be an integer.  try again')

    while True:
        # ask for minimum donation
        min_donation = input('Enter minimum donation (enter 0 if no minimum):')
        # ask for maximum donation
        max_donation = input('Enter maximum donation (enter 0 if no maximum):')
        try:
            min_donation = float(min_donation)
            max_donation = float(max_donation)
            # validate user inputs
            if min_donation < 0 or max_donation < 0:
                print("Inputs can not be negative. try again")
            elif min_donation > 0:
                if max_donation ==0 or max_donation > min_donation:
                    break
                else:
                    print("Maximum must be zero or greater than minimum, try again")
            elif max_donation > 0:
                if min_donation == 0 or min_donation < max_donation:
                    break
                else:
                    print("Minimum must be zero or less than maximum, try again")
            elif min_donation == 0 and max_donation == 0:
                break
            else:
                print("Inputs can not be negative, and Maxium must be greater than minimum. try again")
        except ValueError:
            print('Input must be a float. try again')
    if min_donation == 0:
        min_donation = None
    if max_donation == 0:
        max_donation = None
    sum = collection.projections(factor, min_donation, max_donation);
    print("Factor is {}, Minimum donation is {}, Maximum donation is {}".format(factor, min_donation, max_donation))
    print("Total projections is {}".format(sum))

def quit():
    return 'exit menu'

def display_main_menu():
    """Display main menu"""
    print('\nChoose an action:')
    options = ['1. Send Thank You', '2. Create a Report', '3. Send letters to everyone', '4. Projections', '5. Quit']
    option_str = '\n'.join(['\t'+item for item in options])
    print(option_str)

def main():
    choice = ''
    selection = 'Select an option (1, 2, 3, 4 or 5) ===>'
    switch_function_dict = {'1': send_thank_you, '2': create_report, '3': send_letters, '4': projections, '5': quit}
    while True:
        # Display main menu
        display_main_menu()
        choice = input(selection)
        try:
            if switch_function_dict[choice]() == 'exit menu':
                break
        except KeyError:
            print("Please enter 1, 2, 3, 4 or 5")

if __name__ == '__main__':
    main()
