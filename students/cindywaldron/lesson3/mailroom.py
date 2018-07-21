#!/usr/bin/env python3

donors = [['William Gates, III', 653784.49, 2, 326744.24],
['Mark Zuckerberg', 16396.10, 3, 546437],
['Jeff Bezos', 877.33, 1, 877.33],
['Paul Allen', 708.42, 3, 236.14]]

def getKey(item):
    """
    key is total donation amount
    """
    return item[1]

def send_thank_you():
    """
    This function asks user to enter name and donation amount
    """
    full_name = 'Enter a full name (enter Q to main menu): '
    donation_amount = 'Enter donation amount(enter Q to main menu):'
    response = input(full_name)
    # display all donors' names if input is 'list'
    while response == 'list':
        display_donors()
        response = input(full_name)
    # if input is not 'Q' to quit
    if response.upper() != 'Q':
        # ask to enter donation amount
        amount_input = input(donation_amount)
        # if not quitting
        if amount_input.upper() != 'Q':
            amount = float(amount_input)
            for donor in donors:
                # existing donor
                if response == donor[0]:
                    donor[1] = donor[1] + amount
                    donor[2] = donor[2] + 1
                    donor[3] = donor[1]/donor[2]
                    break
            else:
                # new donor
                donors.append([response, amount, 1, amount])
            # thank you email
            print('Dear {}, Thank you for the donation amount of {}'.format(response, amount))

def create_report():
    """
    Generate report
    """
    print("--------------------------------------------------------------")
    print("{:20} | {:10} | {:5} | {:10}".format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print("--------------------------------------------------------------")
    for row in sorted(donors, key=getKey, reverse=True):
        a_row = '{:20}  $ {:>10.2f}  {:>10d}  $ {:>11.2f}'.format(row[0], row[1],row[2],row[3])
        print(a_row)

def display_donors():
    """
    Display donor names
    """
    for donor in donors:
        print(donor[0])

def display_main_menu():
    """
    Display main menu
    """
    options = [ '1. Send a Thank You', '2. Create a Report', '3. Quit']
    option_str = '\n'.join(['\t'+item for item in options])
    print(option_str)

if __name__ == '__main__':
    # Display main menu
    display_main_menu()
    selection = 'Select an option (1, 2 or 3) ===>'
    choice = input(selection)
    while choice != '3':
        if ( choice == '1'):
            send_thank_you()
        elif ( choice == '2'):
            create_report()
        display_main_menu()
        choice = input(selection)