'''
file: functions_mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: functions for OOP mailroom program 
'''

from classes_mailroom import Collection

def efunc():
    return 'exiting'

def fakefunc():
    pass

def list_donors():
    db = Collection()
    for i in db.get_all_donors():
        print('\t{} {}'.format('Nice person:', i)) 

def list_donations():
    donor = input('Please enter name of donor: ') 
    db = Collection()
    print('\tOverview donations of {} (date, amount):'.format(donor))
    for i in db.get_donations(donor):
        # print('\t{} donated: {}'.format(donor, i)) 
        print('\t{}'.format(i)) 

def add():
    while True: 
        donor = input('Please enter donor name: ')
        if not donor.isalpha():
            print('>> only alphabetical characters in donor name allowed, please try again')
            continue
        else:
            break
    amount = input('Please enter donation amount: ')
    db = Collection()
    db.add_donation(donor, amount)

    #if db.check_existence(donor):   
    #    print('{} found in database'.format(donor))
    #    db.add_donation(donor, amount)
    #else:
    #    print('{} NOT FOUND in database, will be added'.format(donor))
    #    db.add_donation(donor, amount)
        
    
#def add():
#    while True: 
#        dname = input('>> Please give donor name: ')
#        if not dname.isalpha():
#            print('>> only alphabetical characters in donor name allowed, please try again')
#            continue
#        else:
#            break
#    if dname in donors:
#        print('>>', dname, 'already in list')
#        return add_amount(dname)
#        # add_amount(dname)
#        # return True
#    
#    else:
#        print('>>', dname, 'not in list, adding it')
#        return add_amount(dname)
#        # add_amount(dname)
#        # return True


def menu(prompt, dispatcher):
    try:
        while True:
            response = input(prompt)
            if dispatcher[response]() == 'exiting':
                break
    except KeyError:
        print('\n\tSorry, unknown option:', response, '\n')
        menu(prompt, dispatcher)

