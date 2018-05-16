'''
file: functions_mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: functions for OOP mailroom program 
'''

from classes_mailroom import Mailroom, Donor
from collections import defaultdict

db = Mailroom()

def efunc():
    return 'exiting'


def thankyou():
    db.mail()


def report():
    db.report()
    

def enter_donor():
    while True: 
        donor = input('Please enter donor name (<Firstname_Lastname>): ')
        try:
            parts = donor.split(sep = '_')
            fname = parts[0]
            lname = parts[1]
        except:
            print('\nName must be given as <Firstname_Lastname>, please try again\n')
            continue

        dobj = Donor(fname, lname)

        if dobj.check_existence(donor):
            # print('Donor / UID {} found in database...'.format(donor))
            break
        else:
            print('{} not found in database, creating it...'.format(donor))
            if dobj.create(donor, fname, lname, None):
                break
            else:
                continue
    return donor


def list_donors():
    print('\n\tAll donors:\n')
    for i in db.get_all_donors():
        person = i[0]
        print('\t{}'.format(person)) 


def list_donations():
    donor = enter_donor()
    print('\n\tDonations of {}:\n'.format(donor))
    for i in db.get_donations(donor):
        date = i[0]
        donation = i[1]
        print('\tDate: {}\tDonation: {}'.format(date, donation)) 
        

def add():
    donor = enter_donor()
    amount = input('Please enter donation amount: ')
    db.add_donation(donor, amount)


def get_average_donation():
    donor = enter_donor()
    num = db._get_average_donation(donor)
    print('\n\t', num, ' \n')
    

def menu(prompt, dispatcher):
    try:
        while True:
            response = input(prompt)


            if dispatcher[response]() == 'exiting':
                break
            # elif response == 'a':
            #     print('====Hier: Multiplying all donations...')
            # #     dispatcher(give_factor)
            # elif response == 'b':
            #     print('Multiplying only donations below...')
            # elif response == 'c':
            #     print('Multiplying only donations above...')

    except KeyError:
        print('\n\tSorry, unknown option:', response, '\n')
        menu(prompt, dispatcher)


def challenge():
    print("You're taking the CHALLENGE...")
    global factor
    factor = input('Please give a factor: ')
    print('\nCongratulations, you will multiply by {}...'.format(factor))
    # global preview
    # preview = input('\nPlease type "yes" if you want to see a preview first:')

    print('Which donations do you want to multiply?\
    \nPlease choose:')

    prompt = "\
    \n\ta: all\
    \n\tb: all below a certain value\
    \n\tc: all above a certain value\
    \n\t7: exit\n\n"

    dispatcher = {
        'a' : multiply_all,
        'b' : multiply_below,
        'c' : multiply_above,
        '7' : efunc,
        }
    
    menu(prompt, dispatcher)


def multiply_all():
    print('==== multiplying all by {}'.format(factor))
    if db.multiply(factor):
        print('\tAll donations have successfully been multiplied by {}'.format(factor))


def multiply_below():
    below = input('Please enter below threshold:')    
    if db.multiply(factor, below = below):
        print('\tAll donations below {} have successfully been multiplied by {}'.format(below, factor))


def multiply_above():
    above = input('Please enter above threshold:')    
    if db.multiply(factor, above = above):
        print('\tAll donations above {} have successfully been multiplied by {}'.format(above, factor))
