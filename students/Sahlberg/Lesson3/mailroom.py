"""Ian Sahlberg
Assignment 3 mailroom
Python 210
12/28/2018"""


#Disctionary of donors name, dollar amount
donor = {'bob johnson': [150.00],
         'susan skoosan': [2000.00, 550.00],
         'tim tam':[10.50],
         'roxanne raffle':[13.00, 75.00, 123.00],
         'jon jacob':[5000.00, 5.00]
         }

def donate():
    """Appends a donation amount to a given donor."""
    amount = int(input('How much did they donate?'))
    return amount, donor[option].append(amount)

def print_list():
    """Prints our the donor list"""
    return print(list(donor.keys()))

def user_options():
    """Main user options menu choices."""
    user_action = input('Please choose from the following options: Send a Thank You, Create a Report, quit')
    return user_action

def email():
    return print(f'\n\nThank you {option} for the generous donation of $ {amount}. We appreciate your generosity.\n\nSincerely, \n\nThe Helping R Us Team\n\n')

print(list(donor.keys()))

user_action = user_options()

while user_action == 'Send a Thank You':
    option = input('Enter an option: List (to give a list of names), A donors name')
    if option.lower() == 'list':
        print_list()
    else:
        if option.lower() in donor:
            amount = donate()[0]
            print(donor)
            email()

        else:
            donor[option] = []
            amount = donate()[0]
            print(donor)
            email()




print(donor)
